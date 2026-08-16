#!/usr/bin/env python3
"""Evaluate the Skill's recorded output contract without claiming visual quality."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


MECHANISMS: dict[str, list[tuple[str, tuple[str, ...]]]] = {
    "communication_job": [
        ("references/narrative-and-evidence.md", ("communication_job", "audience", "outcome")),
    ],
    "three_full_size_directions": [
        ("references/task-and-process-routing.md", ("three full-size directions",)),
        ("references/visual-direction-method.md", ("readable, full-size scale",)),
    ],
    "evidence_ledger": [
        ("references/narrative-and-evidence.md", ("evidence ledger", "verified", "historical", "to_verify", "do_not_publish")),
    ],
    "presentations_delegate": [
        ("SKILL.md", ("installed `presentations` skill", "implementation authority")),
        ("references/task-and-process-routing.md", ("`presentations` owns pptx implementation",)),
    ],
    "full_slide_review": [
        ("references/quality-gates.md", ("inspect every slide individually at full size", "technical pass cannot override")),
    ],
    "direct_execution": [
        ("references/task-and-process-routing.md", ("selective edit", "edit directly")),
    ],
    "scope_lock": [
        ("references/task-and-process-routing.md", ("scope lock", "do not restyle unrelated slides")),
    ],
    "template_is_authoritative": [
        ("references/task-and-process-routing.md", ("template is authoritative",)),
    ],
    "no_style_mix": [
        ("references/task-and-process-routing.md", ("without mixing another style system",)),
    ],
    "remove_qualify_or_to_verify": [
        ("references/narrative-and-evidence.md", ("remove_qualify_or_to_verify", "remove them", "narrow the language")),
    ],
    "no_invented_metrics": [
        ("references/narrative-and-evidence.md", ("never invent metrics",)),
    ],
    "missing_evidence": [
        ("references/visual-direction-method.md", ("missing evidence",)),
    ],
}


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return payload


def relative_or_absolute(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def check_mechanism(name: str) -> tuple[bool, list[str]]:
    checks = MECHANISMS.get(name)
    if not checks:
        return False, [f"unknown mechanism: {name}"]

    evidence: list[str] = []
    for relative, phrases in checks:
        path = ROOT / relative
        if not path.is_file():
            return False, [f"missing file: {relative}"]
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        missing = [phrase for phrase in phrases if phrase.lower() not in text]
        if missing:
            return False, [f"{relative} missing: {', '.join(missing)}"]
        evidence.append(relative)
    return True, sorted(set(evidence))


def check_forbidden(case_id: str, name: str) -> tuple[bool, str]:
    if case_id == "small-edit" and name == "three_full_size_directions":
        text = (ROOT / "references/task-and-process-routing.md").read_text(encoding="utf-8").lower()
        selective_row = next(
            (line for line in text.splitlines() if "| selective edit |" in line),
            "",
        )
        forbidden = "three full-size directions" in selective_row
        return not forbidden, "selective-edit routing row"
    return False, f"unknown forbidden mechanism: {name}"


def runtime_status(runtime_report: Path | None) -> tuple[str, list[str]]:
    if runtime_report is None or not runtime_report.is_file():
        return "missing evidence", []
    text = runtime_report.read_text(encoding="utf-8", errors="ignore").lower()
    required = (
        "rendered every slide",
        "full-size visual review",
        "overflow check",
        "technical gate: pass",
        "visual gate: pass",
    )
    missing = [phrase for phrase in required if phrase not in text]
    if missing:
        return "failed", missing
    return "verified", []


def evaluate(cases_path: Path, runtime_report: Path | None) -> dict[str, Any]:
    payload = load_json(cases_path)
    results: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []

    for case in payload.get("cases", []):
        case_id = str(case.get("id", ""))
        checks: list[dict[str, Any]] = []
        for name in case.get("required", []):
            passed, evidence = check_mechanism(str(name))
            record = {"mechanism": name, "kind": "required", "passed": passed, "evidence": evidence}
            checks.append(record)
            if not passed:
                failures.append({"case": case_id, **record})
        for name in case.get("forbidden", []):
            passed, evidence = check_forbidden(case_id, str(name))
            record = {"mechanism": name, "kind": "forbidden", "passed": passed, "evidence": [evidence]}
            checks.append(record)
            if not passed:
                failures.append({"case": case_id, **record})
        results.append({"id": case_id, "input": case.get("input", ""), "passed": all(c["passed"] for c in checks), "checks": checks})

    visual_state, runtime_missing = runtime_status(runtime_report)
    if visual_state == "failed":
        failures.append({"case": "runtime_visual_review", "kind": "runtime", "missing": runtime_missing})

    passed_cases = sum(1 for result in results if result["passed"])
    return {
        "ok": not failures,
        "summary": {
            "total_cases": len(results),
            "passed": passed_cases,
            "failed": len(results) - passed_cases + (1 if visual_state == "failed" else 0),
            "missing_evidence": 1 if visual_state == "missing evidence" else 0,
        },
        "results": results,
        "failures": failures,
        "evidence": {
            "rule_contract": "recorded fixture",
            "runtime_visual_review": visual_state,
            "runtime_report": str(runtime_report) if runtime_report else None,
        },
        "method_limitations": [
            "Keyword and file-presence checks verify recorded rule coverage, not presentation beauty or model compliance.",
            "A runtime visual pass requires a real deck, individual full-size slide inspection, and a technical overflow check.",
            "No provider-backed, cross-model, customer-preference, or business-impact evidence is claimed.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the presentation-standard output contract.")
    parser.add_argument("--cases", default="evals/output_cases.json")
    parser.add_argument("--runtime-report")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    cases_path = relative_or_absolute(args.cases)
    output_path = relative_or_absolute(args.output)
    runtime_report = relative_or_absolute(args.runtime_report) if args.runtime_report else None
    report = evaluate(cases_path, runtime_report)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["ok"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
