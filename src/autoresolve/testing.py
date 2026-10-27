
import subprocess
import sys
from pathlib import Path


class TestRunner:
    """Run the approved pytest suite and capture its output."""

    def __init__(self, repository_root: str):
        self.root = Path(repository_root).resolve()

    def run_tests(self) -> dict:
        """Run the project's approved calculator tests."""

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "tests/test_calculator.py",
                "-v",
            ],
            cwd=self.root,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

        return {
            "exit_code": result.returncode,
            "passed": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }


if __name__ == "__main__":
    runner = TestRunner(".")
    outcome = runner.run_tests()

    print("=== AutoResolve AI: Test Results ===")
    print(outcome["stdout"])

    if outcome["stderr"]:
        print(outcome["stderr"])

    print("Exit code:", outcome["exit_code"])
    print("All tests passed:", outcome["passed"])
