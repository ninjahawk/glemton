# weekend_run.ps1 - unattended 3B-token training for the Glemton 350M v1.0-preview.
#
# Resilience:
#  - Resumes from the latest checkpoint if the training process dies.
#  - A background watcher writes STATUS.md and git-pushes it every ~10 min,
#    and prunes old checkpoints so the disk does not fill.
#
# Run from the project root:
#   powershell -ExecutionPolicy Bypass -File scripts\weekend_run.ps1

$ErrorActionPreference = "Continue"
$root = "C:\Users\jedin\Desktop\Glemton"
Set-Location $root
$env:PYTHONPATH = "src"

$py       = ".venv\Scripts\python.exe"
$cfg      = "configs\glemton-350m.yaml"
$ckptDir  = "checkpoints\glemton-350m"
$log      = "logs\glemton_350m_v1_preview.log"

New-Item -ItemType Directory -Force -Path $ckptDir | Out-Null
# Archive any prior log so ETA math is not polluted by the aborted run.
if (Test-Path $log) { Move-Item $log "$log.$(Get-Date -Format yyyyMMdd_HHmmss).old" -Force }

# ---- background watcher: status push + checkpoint pruning ----
$watcher = Start-Job -Name glemton-watcher -ScriptBlock {
    $root = "C:\Users\jedin\Desktop\Glemton"
    Set-Location $root
    $env:PYTHONPATH = "src"
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
Write-Host "[weekend_run] watcher job started (id $($watcher.Id))"

# ---- training resume loop ----
$attempt = 0
while ($true) {
    if (Test-Path (Join-Path $ckptDir "final.pt")) {
        Write-Host "[weekend_run] final.pt present - training complete."
        break
    }
    $attempt++
    $latest = Get-ChildItem (Join-Path $ckptDir "step_*.pt") -ErrorAction SilentlyContinue |
              Sort-Object LastWriteTime | Select-Object -Last 1

    if ($latest) {
        Write-Host "[weekend_run] attempt $attempt - resuming from $($latest.Name)"
        & $py -m glemton.train $cfg --resume $latest.FullName 2>&1 | Tee-Object -FilePath $log -Append
    } else {
        Write-Host "[weekend_run] attempt $attempt - fresh start"
        & $py -m glemton.train $cfg 2>&1 | Tee-Object -FilePath $log -Append
    }
    $code = $LASTEXITCODE
    Write-Host "[weekend_run] training process exited (code $code)"

    if (Test-Path (Join-Path $ckptDir "final.pt")) {
        Write-Host "[weekend_run] final.pt present - done."
        break
    }
    if ($attempt -ge 50) {
        Write-Host "[weekend_run] 50 failed attempts - giving up to avoid a crash loop."
        break
    }
    Write-Host "[weekend_run] will resume in 30s..."
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
Write-Host "[weekend_run] done."
