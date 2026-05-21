"""Long-conversation consistency eval.

Builds synthetic multi-turn dialogues with a "fact planted at turn K"
structure, then asks at turn N (N >> K) whether the model can recall the
fact. Measures recall accuracy as a function of (N - K).

This is the second defensible claim: at turn 50, recall something stated
in turn 5 better than baselines whose context windows have been compacted.
"""

from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass
class ConversationProbe:
    turns: list[tuple[str, str]]  # (speaker, utterance)
    planted_fact: str
    fact_token: str  # unique string we look for in the recall response
    query_turn_idx: int  # which turn is the recall query
    plant_turn_idx: int


FILLER_TOPICS = [
    "the weather", "music", "books I've been reading", "what I had for breakfast",
    "my commute", "a movie I watched", "a recipe", "a hobby",
    "an old neighborhood", "a vacation", "a project at work",
]


def _random_filler(rng: random.Random) -> tuple[str, str]:
    topic = rng.choice(FILLER_TOPICS)
    a = f"<user> So, about {topic} — what do you think?"
    b = f"<reply> Honestly, {topic} hasn't been on my mind lately. Tell me more."
    return a, b


def build_probe(
    plant_turn: int,
    query_turn: int,
    fact_template: str,
    fact_token: str,
    rng: random.Random,
) -> ConversationProbe:
    assert query_turn > plant_turn
    turns: list[tuple[str, str]] = []
    for i in range(query_turn + 1):
        if i == plant_turn:
            turns.append(("<user>", f"<user> By the way, {fact_template.format(token=fact_token)}"))
            turns.append(("<reply>", "<reply> Got it."))
        elif i == query_turn:
            turns.append(("<user>", "<user> Quick check — do you remember the thing I mentioned earlier? What was it?"))
        else:
            a, b = _random_filler(rng)
            turns.append(("<user>", a))
            turns.append(("<reply>", b))
    return ConversationProbe(
        turns=turns,
        planted_fact=fact_template.format(token=fact_token),
        fact_token=fact_token,
        query_turn_idx=query_turn,
        plant_turn_idx=plant_turn,
    )


def make_probe_suite(seed: int = 0) -> list[ConversationProbe]:
    rng = random.Random(seed)
    fact_templates = [
        "my dog's name is {token}",
        "I bought a {token} last week",
        "the password for the safe is {token}",
        "I'm allergic to {token}",
        "we're meeting at {token} on Friday",
    ]
    tokens = ["zebricore", "quartzly", "fenmaple", "brillox", "skemvale", "drundle", "plovith", "klempron"]
    probes = []
    # gaps of 5, 10, 25, 50, 75 turns between plant and query
    for gap in (5, 10, 25, 50, 75):
        for j in range(3):
            plant = 2
            query = plant + gap
            tpl = fact_templates[j % len(fact_templates)]
            tok = tokens[(j + gap) % len(tokens)]
            probes.append(build_probe(plant, query, tpl, tok, rng))
    return probes


def serialize_probe(p: ConversationProbe) -> str:
    return "\n".join(t for _, t in p.turns)


def grade_response(probe: ConversationProbe, response: str) -> bool:
    return probe.fact_token.lower() in response.lower()


def evaluate(generate_fn: Callable[[str], str], probes: list[ConversationProbe]) -> dict:
    results = []
    for p in probes:
        ctx = serialize_probe(p)
        resp = generate_fn(ctx)
        ok = grade_response(p, resp)
        results.append({
            "gap": p.query_turn_idx - p.plant_turn_idx,
            "fact_token": p.fact_token,
            "response": resp,
            "recalled": ok,
        })
    by_gap: dict[int, list[bool]] = {}
    for r in results:
        by_gap.setdefault(r["gap"], []).append(r["recalled"])
    summary = {gap: sum(v) / len(v) for gap, v in sorted(by_gap.items())}
    return {"summary_accuracy_by_gap": summary, "results": results}


if __name__ == "__main__":
    probes = make_probe_suite(seed=0)
    print(f"built {len(probes)} probes")
    for p in probes[:2]:
        print("---")
        print(serialize_probe(p))
        print(f"planted: {p.planted_fact}  token: {p.fact_token}")
