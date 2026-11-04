"""Execute one NLP lab notebook and save its real Jupyter outputs.

Used by the GitHub Actions workflow. Failed runs are not published.
"""
from __future__ import annotations

import json
import shutil
import sys
import traceback
from pathlib import Path

import nbformat
from nbclient import NotebookClient

REPO = Path(__file__).resolve().parents[2]
LAB = sys.argv[1]
folder = REPO / LAB
notebooks = list(folder.glob("*.ipynb"))
if len(notebooks) != 1:
    raise RuntimeError(f"Expected one notebook in {folder}, found {len(notebooks)}")

def download_kaggle_file(slug: str, filename: str, dest: Path) -> None:
    if dest.exists():
        return
    import kagglehub
    dataset_path = Path(kagglehub.dataset_download(slug))
    matches = list(dataset_path.rglob(filename))
    if not matches:
        raise FileNotFoundError(f"{filename} missing from {slug}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(matches[0], dest)
    print(f"Dataset ready: {dest} ({dest.stat().st_size} bytes)", flush=True)

# Some original lab examples use Colab's /content/ location for CSV files.
if LAB == "LAB4":
    download_kaggle_file(
        "arushchillar/disneyland-reviews", "DisneylandReviews.csv",
        Path("/content/DisneylandReviews.csv")
    )
if LAB == "LAB5":
    download_kaggle_file(
        "clmentbisaillon/fake-and-real-news-dataset", "True.csv",
        Path("/content/True.csv")
    )

notebook = nbformat.read(notebooks[0], as_version=4)

# Fix cells that otherwise fail during a non-interactive Run All.
if LAB == "LAB2":
    for cell in notebook.cells:
        if cell.cell_type == "code" and "nltk.download('punkt')" in cell.source:
            if "import nltk" not in cell.source:
                cell.source = "import nltk\n" + cell.source
if LAB == "LAB5":
    # The first TF-IDF example uses pd before the later import cell.
    for cell in notebook.cells:
        if cell.cell_type == "code" and "from sklearn.feature_extraction.text import TfidfVectorizer" in cell.source:
            if "import pandas as pd" not in cell.source:
                cell.source = "import pandas as pd\n" + cell.source
            break
if LAB == "LAB9":
    # Automated execution cannot wait for interactive user input.
    for cell in notebook.cells:
        if cell.cell_type == "code" and 'user_sentence = input("Enter a sentence: ")' in cell.source:
            cell.source = cell.source.replace(
                'user_sentence = input("Enter a sentence: ")',
                '# Example entered for the saved Run All output.\n'
                '# To enter a different sentence manually, use input("Enter a sentence: ").\n'
                'user_sentence = "Steve Jobs founded Apple in California."\n'
                'print("Entered sentence:", user_sentence)'
            )

print(f"Running {LAB}: {notebooks[0].name} ({sum(c.cell_type == 'code' for c in notebook.cells)} code cells)", flush=True)
status = {"lab": LAB, "notebook": str(notebooks[0].relative_to(REPO))}
report = REPO / "run_reports"
report.mkdir(exist_ok=True)
try:
    client = NotebookClient(
        notebook,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(folder)}},
        allow_errors=False,
    )
    result = client.execute()
    code_cells = [c for c in result.cells if c.cell_type == "code" and c.source.strip()]
    exceptions = [o for c in code_cells for o in c.get("outputs", []) if o.get("output_type") == "error"]
    if exceptions:
        raise RuntimeError(f"Notebook produced {len(exceptions)} error outputs")
    with_outputs = sum(bool(c.get("outputs")) for c in code_cells)
    executed = sum(c.get("execution_count") is not None for c in code_cells)
    if executed != len(code_cells) or with_outputs == 0:
        raise RuntimeError(f"Incomplete execution: {executed}/{len(code_cells)} cells, {with_outputs} with outputs")
    output_file = REPO / "executed" / LAB / notebooks[0].name
    output_file.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(result, output_file)
    status.update({"success": True, "executed_cells": executed, "cells_with_outputs": with_outputs})
    print(f"SUCCESS {LAB}: {executed} code cells executed, {with_outputs} cells have real outputs", flush=True)
except BaseException as exc:
    status.update({"success": False, "error": str(exc), "traceback": traceback.format_exc()[-8000:]})
    print(f"FAILED {LAB}: {exc}", file=sys.stderr, flush=True)
    (report / f"{LAB}.json").write_text(json.dumps(status, indent=2), encoding="utf-8")
    raise
(report / f"{LAB}.json").write_text(json.dumps(status, indent=2), encoding="utf-8")
