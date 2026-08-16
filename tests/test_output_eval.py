from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class OutputEvalTests(unittest.TestCase):
    def test_output_contract_report(self):
        script = ROOT / "scripts/output_eval.py"
        self.assertTrue(script.is_file(), "scripts/output_eval.py")

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.json"
            result = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--cases",
                    str(ROOT / "evals/output_cases.json"),
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(report["ok"])
            self.assertEqual(report["summary"]["failed"], 0)
            self.assertEqual(report["summary"]["missing_evidence"], 1)
            self.assertIn("keyword", report["method_limitations"][0].lower())
            self.assertEqual(
                report["evidence"]["runtime_visual_review"], "missing evidence"
            )


if __name__ == "__main__":
    unittest.main()
