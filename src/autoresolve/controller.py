import subprocess
import json
from pathlib import Path

from repository import RepositoryInspector
from testing import TestRunner


class AutoResolveAgent:
    """Coordinate repository inspection and test execution."""

    def __init__(self, repository_root: str = "."):
        self.root = Path(repository_root).resolve()
        self.inspector = RepositoryInspector(str(self.root))
        self.test_runner = TestRunner(str(self.root))

    def investigate(self) -> dict:
        """Inspect the calculator, run its tests, and report evidence."""

        source_path = "tasks/buggy_project/calculator.py"

        try:
            source_code = self.inspector.read_file(source_path)
        except (OSError, ValueError) as exc:
            return {
                "status": "INVESTIGATION_FAILED",
                "error": str(exc),
            }

        try:
            test_result = self.test_runner.run_tests()
        except (OSError, subprocess.TimeoutExpired) as exc:
            return {
                "status": "TEST_EXECUTION_FAILED",
                "error": str(exc),
            }

        status = (
            "TESTS_PASSED"
            if test_result["passed"]
            else "BUG_DETECTED"
        )

        return {
            "project": "AutoResolve AI",
            "status": status,
            "file_inspected": source_path,
            "source_code": source_code,
            "test_exit_code": test_result["exit_code"],
            "tests_passed": test_result["passed"],
            "test_output": test_result["stdout"],
        }


if __name__ == "__main__":
    import subprocess

    agent = AutoResolveAgent(".")
    report = agent.investigate()

    print(json.dumps(report, indent=2))
