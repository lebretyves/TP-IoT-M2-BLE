"""Exécute le notebook officiel complété depuis son dossier de livrables."""
import argparse
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bonus", action="store_true", help="Exécuter les bonus séparés")
    args = parser.parse_args()
    dossier = Path(__file__).resolve().parent / "analyses" / "m2_tp3"
    if args.bonus:
        dossier = dossier / "bonus"
    chemin = dossier / ("TP_M2_3_BLE_bonus.ipynb" if args.bonus else "TP_M2_3_BLE_decodeur.ipynb")
    notebook = nbformat.read(chemin, as_version=4)
    NotebookClient(
        notebook, timeout=120, kernel_name="python3",
        resources={"metadata": {"path": str(dossier)}},
    ).execute()
    nbformat.write(notebook, chemin)
    print(f"Notebook exécuté : {chemin}")
    if not args.bonus:
        print(f"CSV officiel : {dossier / 'trames_decodees.csv'}")


if __name__ == "__main__":
    main()
