"""EVEZ Ω WHERE-COUNT restoration spine.

Canonical event = WHERE + WHAT + COUNT + CHANGE
Every event is SHA-256 hash-chained (prev → hash).
Agent decision logs become deterministic puzzle cipher keys.

No model output becomes canon without a sealed receipt.
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import asdict, dataclass
from typing import Any

GENESIS = "evez-omega-genesis-2026-09-12"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass
class Event:
    where: dict[str, Any]
    what: str
    count: dict[str, Any]
    change: str
    agent: str
    confidence: str  # verified | inferred | unknown | contradicted | stale
    evidence: str
    ts: str
    prev: str = ""
    hash: str = ""

    def seal(self, prev: str) -> "Event":
        self.prev = prev
        body = json.dumps(
            {
                "where": self.where,
                "what": self.what,
                "count": self.count,
                "change": self.change,
                "agent": self.agent,
                "confidence": self.confidence,
                "evidence": self.evidence,
                "ts": self.ts,
                "prev": prev,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        self.hash = sha256(body)
        return self


class Spine:
    """Append-only control plane. CARTOGRAPHER / ACCOUNTANT / ARCHAEOLOGIST / SPINE write here."""

    def __init__(self, genesis: str = GENESIS) -> None:
        self.genesis = genesis
        self.chain: list[Event] = []
        self.entities: dict[str, dict[str, Any]] = {}
        self.unknowns: list[dict[str, Any]] = []
        self.opportunities: list[dict[str, Any]] = []
        self.puzzle_keys: list[dict[str, Any]] = []

    def tip(self) -> str:
        return self.chain[-1].hash if self.chain else sha256(self.genesis)

    def emit(
        self,
        *,
        where: dict[str, Any],
        what: str,
        count: dict[str, Any],
        change: str,
        agent: str,
        confidence: str,
        evidence: str,
        ts: str | None = None,
    ) -> Event:
        ts = ts or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        ev = Event(
            where=where,
            what=what,
            count=count,
            change=change,
            agent=agent,
            confidence=confidence,
            evidence=evidence,
            ts=ts,
        ).seal(self.tip())
        self.chain.append(ev)
        eid = f"{where.get('provider', 'x')}:{where.get('id', what)}"
        self.entities[eid] = {
            "what": what,
            "where": where,
            "count": count,
            "change": change,
            "confidence": confidence,
            "last_hash": ev.hash,
            "agent": agent,
        }
        key_material = f"{agent}|{ev.hash}|{change}|{len(self.chain)}"
        cipher = sha256(key_material)
        self.puzzle_keys.append(
            {
                "seq": len(self.chain),
                "agent": agent,
                "event_hash": ev.hash[:16],
                "cipher_key": cipher,
                "puzzle_seed": int(cipher[:8], 16) % 10_000_000,
            }
        )
        return ev

    def mark_unknown(self, field: str, reason: str, value: str = "HIGH") -> None:
        self.unknowns.append(
            {
                "field": field,
                "reason": reason,
                "value": value,
                "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
        )

    def opportunity(
        self, title: str, gain: float, cost: float, confidence: float
    ) -> None:
        score = (gain * confidence) / max(cost, 0.01)
        self.opportunities.append(
            {
                "title": title,
                "score": round(score, 3),
                "gain": gain,
                "cost": cost,
                "confidence": confidence,
            }
        )
        self.opportunities.sort(key=lambda x: -x["score"])

    def verify_chain(self) -> bool:
        prev = sha256(self.genesis)
        for ev in self.chain:
            if ev.prev != prev:
                return False
            body = json.dumps(
                {
                    "where": ev.where,
                    "what": ev.what,
                    "count": ev.count,
                    "change": ev.change,
                    "agent": ev.agent,
                    "confidence": ev.confidence,
                    "evidence": ev.evidence,
                    "ts": ev.ts,
                    "prev": ev.prev,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            if sha256(body) != ev.hash:
                return False
            prev = ev.hash
        return True

    def export(self) -> dict[str, Any]:
        return {
            "tip": self.tip(),
            "length": len(self.chain),
            "chain_valid": self.verify_chain(),
            "entities": len(self.entities),
            "entity_map": self.entities,
            "unknowns": self.unknowns,
            "opportunities": self.opportunities,
            "puzzle_keys": self.puzzle_keys,
            "chain": [asdict(e) for e in self.chain],
        }


def restore_from_fleet() -> Spine:
    """Seed spine from verified EvezArt fleet facts (session-sealed)."""
    s = Spine()
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    s.emit(
        where={"provider": "github", "org": "EvezArt", "id": "evez-spectrum", "path": "main"},
        what="repository:HQ",
        count={"files": 4, "issues_open": 1},
        change="mapped",
        agent="CARTOGRAPHER",
        confidence="verified",
        evidence="STATUS.md + ROADMAP.md + DOCTRINE.md sealed 2026-09-12",
        ts=now,
    )
    s.emit(
        where={"provider": "github", "org": "EvezArt", "id": "openclaw-fork", "path": "PR/68"},
        what="pull_request:ci-runner-fix",
        count={"files_changed": 3},
        change="created",
        agent="CARTOGRAPHER",
        confidence="verified",
        evidence="https://github.com/EvezArt/openclaw-fork/pull/68",
        ts=now,
    )
    s.emit(
        where={"provider": "github", "org": "EvezArt", "id": "openclaw-fork", "path": "PR/67"},
        what="pull_request:nextclaw-federation",
        count={"swarm_modules": 22},
        change="observed",
        agent="CARTOGRAPHER",
        confidence="verified",
        evidence="truth_gate + control_plane present; CI red",
        ts=now,
    )
    s.emit(
        where={"provider": "stripe", "account": "acct_1TaxJQDBhYAyYlOh", "mode": "test"},
        what="product:evez-os-skills-lifetime",
        count={"unit_amount_cents": 100, "livemode": 0},
        change="created",
        agent="ACCOUNTANT",
        confidence="verified",
        evidence="prod_VFUy37dkMkNWUN / price_1UEzz7DBhYAyYlOhmFWkHRPF",
        ts=now,
    )
    s.emit(
        where={"provider": "vercel", "scope": "EvezArt"},
        what="deploy_status",
        count={"blocked_projects": 2},
        change="failed",
        agent="CAIN",
        confidence="verified",
        evidence="Account is blocked",
        ts=now,
    )
    s.emit(
        where={"provider": "github", "org": "EvezArt", "id": "openclaw-fork", "path": "swarm/control_plane.py"},
        what="module:control_plane",
        count={"bytes": 17681},
        change="mapped",
        agent="ARCHAEOLOGIST",
        confidence="verified",
        evidence="PR#67 substrate",
        ts=now,
    )

    s.mark_unknown("github_actions_minutes_remaining", "Not queried", "HIGH")
    s.mark_unknown("vercel_unblock_path", "Human billing required", "CRITICAL")
    s.mark_unknown("live_stripe_paylink", "Test mode only", "HIGH")
    s.mark_unknown("clawdhub_publish_state", "32 skills unverified", "HIGH")

    s.opportunity("Merge openclaw-fork#68", 9.0, 0.2, 0.95)
    s.opportunity("Promote Stripe $1 to livemode", 8.5, 1.0, 0.9)
    s.opportunity("Green nextclaw contract on #67", 9.5, 2.5, 0.7)
    s.opportunity("Unblock Vercel", 8.0, 3.0, 0.6)

    s.emit(
        where={"provider": "evez", "id": "spine", "path": "priority"},
        what="priority:merge-pr-68",
        count={"opportunities": len(s.opportunities)},
        change="prioritized",
        agent="SPINE",
        confidence="inferred",
        evidence=s.opportunities[0]["title"],
        ts=now,
    )
    return s


if __name__ == "__main__":
    spine = restore_from_fleet()
    report = spine.export()
    assert report["chain_valid"], "chain integrity failed"
    print(json.dumps({
        "tip": report["tip"],
        "length": report["length"],
        "chain_valid": report["chain_valid"],
        "entities": report["entities"],
        "top_opportunity": report["opportunities"][0],
        "last_cipher": report["puzzle_keys"][-1]["cipher_key"],
        "unknown_count": len(report["unknowns"]),
    }, indent=2))
