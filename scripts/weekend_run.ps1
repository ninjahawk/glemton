# weekend_run.ps1 - unattended 3B-token training for the Glemton 350M v1.0-preview.
#
# Designed to run headless as a Windows Scheduled Task (no console, immune to
# terminal / Claude-Code close). Do NOT launch this from an interactive shell
# for the real run - a harness-launched process is not detached and dies when
# the launching tool call ends (see WAKE_UP.md).
#
# Resilience:
#  - FOR_DISABLE_CONSOLE_CTRL_HANDLER=1 stops the Intel Fortran runtime (pulled
#    in via numpy/MKL) from aborting the process on a window-CLOSE event - this
#    is what killed the earlier relaunch attempt.
#  - Resumes from the latest checkpoint if the training process dies.
#  - A background watcher writes STATUS.md and git-pushes it every ~10 min,
#    and prunes old checkpoints so the disk does not fill.
#
# Manual headless launch (if not using the scheduled task):
#   powershell -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File scripts\weekend_run.ps1

$ErrorActionPreference = "Continue"
$root = "C:\Users\jedin\Desktop\Glemton"
Set-Location $root

# Detach hardening: keep the Fortran runtime from aborting on console events.
# Set before any child process spawns so the training process and the watcher
# job both inherit it.
$env:FOR_DISABLE_CONSOLE_CTRL_HANDLER = "1"
$env:PYTHONPATH = "src"
$env:PYTHONUNBUFFERED = "1"

$py       = ".venv\Scripts\python.exe"
$cfg      = "configs\glemton-350m.yaml"
$ckptDir  = "checkpoints\glemton-350m"
$log      = "logs\glemton_350m_v1_preview.log"
$wrapLog  = "logs\weekend_run_wrapper.log"

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] [weekend_run] $msg"
    Write-Host $line
    Add-Content -Path $wrapLog -Value $line -ErrorAction SilentlyContinue
}

New-Item -ItemType Directory -Force -Path $ckptDir | Out-Null
New-Item -ItemType Directory -Force -Path "logs"   | Out-Null
Log "starting up (pid $PID)"

# Archive any prior training log so ETA math is not polluted by an aborted run.
if (Test-Path $log) {
    $archived = "$log.$(Get-Date -Format yyyyMMdd_HHmmss).old"
    Move-Item $log $archived -Force
    Log "archived prior log -> $archived"
}

# ---- background watcher: status push + checkpoint pruning ----
$watcher = Start-Job -Name glemton-watcher -ScriptBlock {
    $root = "C:\Users\jedin\Desktop\Glemton"
    Set-Location $root
    $env:PYTHONPATH = "src"
    $env:FOR_DISABLE_CONSOLE_CTRL_HANDLER = "1"
    $ckptDir = Join-Path $root "checkpoints\glemton-350m"
    while ($true) {
        Start-Sleep -Seconds 600
        try { & ".venv\Scripts\python.exe" "scripts\gen_status.py" | Out-Null } catch {}
        try {
            git add STATUS.md 2>&1 | Out-Null
            git commit -m "status: automated training update" 2>&1 | Out-Null
            git push 2>&1 | Out-Null
        } catch {}
        # Prune: keep the 4 newest checkpoints + every 500M-token milestone.
        # Only touch files older than 5 min so we never race a mid-write save.
        try {
            $ckpts = Get-ChildItem (Join-Path $ckptDir "step_*.pt") -ErrorAction SilentlyContinue
            $info = foreach ($c in $ckpts) {
                if ($c.Name -match "_tokens_(\d+)M") {
                    [pscustomobject]@{ File = $c; Tok = [int]$Matches[1] }
                }
            }
            $sorted = $info | Sort-Object Tok
            $keepNewest = ($sorted | Select-Object -Last 4).File.FullName
            foreach ($x in $sorted) {
                $isMilestone = ($x.Tok % 500) -eq 0
                $isNewest    = $keepNewest -contains $x.File.FullName
                $ageMin      = ((Get-Date) - $x.File.LastWriteTime).TotalMinutes
                if (-not $isMilestone -and -not $isNewest -and $ageMin -gt 5) {
                    Remove-Item $x.File.FullName -Force -ErrorAction SilentlyContinue
                }
            }
        } catch {}
    }
}
Log "watcher job started (id $($watcher.Id))"

# ---- training resume loop ----
$attempt = 0
while ($true) {
    if (Test-Path (Join-Path $ckptDir "final.pt")) {
        Log "final.pt present - training complete."
        break
    }
    $attempt++
    $latest = Get-ChildItem (Join-Path $ckptDir "step_*.pt") -ErrorAction SilentlyContinue |
              Sort-Object LastWriteTime | Select-Object -Last 1

    if ($latest) {
        Log "attempt $attempt - resuming from $($latest.Name)"
        & $py -m glemton.train $cfg --resume $latest.FullName 2>&1 | Tee-Object -FilePath $log -Append
    } else {
        Log "attempt $attempt - fresh start"
        & $py -m glemton.train $cfg 2>&1 | Tee-Object -FilePath $log -Append
    }
    $code = $LASTEXITCODE
    Log "training process exited (code $code)"

    if (Test-Path (Join-Path $ckptDir "final.pt")) {
        Log "final.pt present - done."
        break
    }
    if ($attempt -ge 50) {
        Log "50 failed attempts - giving up to avoid a crash loop."
        break
    }
    Log "will resume in 30s..."
    Start-Sleep -Seconds 30
}

# ---- final status push ----
try { & $py "scripts\gen_status.py" | Out-Null } catch {}
try {
    git add STATUS.md 2>&1 | Out-Null
    git commit -m "status: training run finished" 2>&1 | Out-Null
    git push 2>&1 | Out-Null
} catch {}
Stop-Job $watcher -ErrorAction SilentlyContinue
Remove-Job $watcher -Force -ErrorAction SilentlyContinue
Log "done."
