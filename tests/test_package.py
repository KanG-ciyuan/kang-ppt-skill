from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def package_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".json"}:
            continue
        if any(part in {"docs", "tests", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        yield path


class PackageContractTests(unittest.TestCase):
    def test_required_files(self):
        required = [
            "SKILL.md", "README.md", "manifest.json", "agents/interface.yaml",
            "references/task-and-process-routing.md",
            "references/visual-direction-method.md",
            "references/narrative-and-evidence.md",
            "references/quality-gates.md",
            "evals/trigger_cases.json", "evals/output_cases.json",
        ]
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_single_identity_and_delegate(self):
        skill_path = ROOT / "SKILL.md"
        self.assertTrue(skill_path.is_file(), "SKILL.md")
        skill = skill_path.read_text(encoding="utf-8")
        self.assertIn("name: kang-ppt-skill", skill)
        self.assertIn("author: Kang", skill)
        self.assertIn("Presentations", skill)
        self.assertRegex(skill, r"Do not (copy|duplicate).*(engine|renderer|template)")

    def test_no_fixed_universal_style(self):
        text = "\n".join(
            p.read_text(encoding="utf-8", errors="ignore")
            for p in package_text_files()
        )
        self.assertIn("Do not hard-code", text)
        self.assertNotIn("always use Inter", text)
        self.assertNotIn("always use #", text)

    def test_trigger_fixture_balance(self):
        cases = json.loads((ROOT / "evals/trigger_cases.json").read_text())
        self.assertGreaterEqual(len(cases["should_trigger"]), 5)
        self.assertGreaterEqual(len(cases["should_not_trigger"]), 5)
        self.assertGreaterEqual(len(cases["near_neighbor"]), 3)

    def test_no_secret_values(self):
        text = "\n".join(
            p.read_text(errors="ignore") for p in package_text_files()
        )
        secret_pattern = re.compile(
            r"(?:\bsk-[A-Za-z0-9_-]{20,}\b|\bBearer\s+[A-Za-z0-9._-]{20,}\b)"
        )
        self.assertNotRegex(text, secret_pattern)


if __name__ == "__main__":
    unittest.main()
