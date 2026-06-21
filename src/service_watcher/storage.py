import json
from pathlib import Path

RESULT_FILE = Path("data/checks.json")


def save_results(results: list[dict]) -> None:
    RESULT_FILE.parent.mkdir(exist_ok=True)

    with RESULT_FILE.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)