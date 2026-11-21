from pathlib import Path
import json

import nbformat
from nbclient import NotebookClient

lab = Path("LAB13")
for path in sorted(lab.glob("*.ipynb")):
    print("Running:", path, flush=True)
    notebook = nbformat.read(path, as_version=4)
    result = NotebookClient(
        notebook, timeout=600, kernel_name="python3",
        resources={"metadata": {"path": str(lab)}}, allow_errors=False
    ).execute()

    cells = [c for c in result.cells if c.cell_type == "code" and c.source.strip()]
    executed = sum(c.get("execution_count") is not None for c in cells)
    with_outputs = sum(bool(c.get("outputs")) for c in cells)
    errors = sum(o.output_type == "error" for c in cells for o in c.get("outputs", []))
    if executed != len(cells) or with_outputs == 0 or errors:
        raise RuntimeError(f"Incomplete: {path}: {executed}/{len(cells)} executed, {with_outputs} outputs, {errors} errors")

    nbformat.write(result, path)
    print("OK:", path, "executed:", executed, "outputs:", with_outputs, flush=True)
