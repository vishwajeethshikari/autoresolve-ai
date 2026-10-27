
from pathlib import Path


class RepositoryInspector:
    """Read files from an approved repository directory."""

    def __init__(self, root: str):
        self.root = Path(root).resolve()

    def read_file(self, relative_path: str) -> str:
        """Read a text file without allowing paths outside the repository."""
        target = (self.root / relative_path).resolve()

        if not target.is_relative_to(self.root):
            raise ValueError("Access outside the repository is not allowed.")

        if not target.is_file():
            raise FileNotFoundError(f"File not found: {relative_path}")

        return target.read_text(encoding="utf-8")


if __name__ == "__main__":
    repository = RepositoryInspector(".")

    source = repository.read_file(
        "tasks/buggy_project/calculator.py"
    )

    print("=== Source code inspected by AutoResolve AI ===")
    print(source)
