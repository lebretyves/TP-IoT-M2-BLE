"""Exécute le notebook officiel complété depuis son dossier de livrables."""
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def main():
    dossier = Path(__file__).resolve().parent / "analyses" / "m2_tp3"
    chemin = dossier / "TP_M2_3_BLE_decodeur.ipynb"
    notebook = nbformat.read(chemin, as_version=4)
    NotebookClient(
        notebook, timeout=120, kernel_name="python3",
        resources={"metadata": {"path": str(dossier)}},
    ).execute()
    nbformat.write(notebook, chemin)
    print(f"Notebook exécuté : {chemin}")
    print(f"CSV officiel : {dossier / 'trames_decodees.csv'}")


if __name__ == "__main__":
    main()
