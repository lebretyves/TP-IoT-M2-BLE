# TP M2-3 — Bluetooth basse consommation — Équipe 02

TP du 9 octobre 2026, Digi5, module 2, Epitech MBA Santé, IA & IoT, à partir de l’énoncé étudiant de Nicolas Laurio.

Équipe GitHub : [lebretyves](https://github.com/lebretyves), [Faucourt](https://github.com/Faucourt) et [aglnix](https://github.com/aglnix).

## Travail réalisé

La voie A utilise une Garmin Forerunner 265 et nRF Connect sur Samsung Galaxy S24 FE. Le service Heart Rate `0x180D` et la caractéristique `0x2A37` ont été observés ; 160 notifications cardiaques ont été reçues et décodées. Les cinq premières sont détaillées dans le compte rendu.

- [Notebook officiel complété et exécuté](analyses/m2_tp3/TP_M2_3_BLE_decodeur.ipynb) : 24 cellules conservées, réponses manuelles vérifiées, cinq questions traitées, cinq trames Garmin décodées et sorties des bonus visibles.
- [Compte rendu](analyses/m2_tp3/README.md) : cinq appareils scannés, annonces anonymisées, trois relevés RSSI, questions a–c et cinq réponses du notebook, mesures Garmin et explications GATT.
- [Décodage expliqué des trames 3, 5 et 2](analyses/m2_tp3/trames_decodees.md).
- [CSV des six trames fictives](analyses/m2_tp3/trames_decodees.csv), exporté par la cellule « Livrable » du notebook officiel.
- [Décodeur Python](analyses/m2_tp3/decode_hrm.py), avec ses vérifications.
- [Notifications Garmin horodatées](analyses/m2_tp3/notifications_garmin_2026-10-09.txt) et [mesures décodées](analyses/m2_tp3/mesures_garmin.json), sans nom du porteur ni adresse Bluetooth.
- [Énoncé du TP](TP_M2_3_BLE_nRFConnect_etudiant.pdf).

## Vérification locale

Python 3.10 ou plus récent. Pour réexécuter le notebook et régénérer son CSV officiel :

```powershell
python -m pip install -r requirements.txt
python executer_tp.py
```

Le script lance le notebook depuis son dossier de livrables et enregistre les sorties dans le fichier `.ipynb`. Les fonctions du professeur sont conservées ; seuls `MES_FC` et `MES_TRAMES_CAPTUREES` ont été complétés dans les cellules de code. Les réponses et une précision sur les données réelles du bonus A ont été ajoutées aux cellules Markdown.

Le décodeur autonome reste utilisable sans dépendance externe :

```powershell
python analyses/m2_tp3/decode_hrm.py
```

Ce décodeur complémentaire écrit désormais `analyses/m2_tp3/trames_decodees_local.csv` (ignoré par Git), pour ne pas écraser l’export officiel. Les mesures réelles de la montre sont conservées séparément.

## À terminer avant le rendu

- Enregistrer `analyses/m2_tp3/capture_nrfconnect.png` à partir d’une capture réelle de nRF Connect, avec les noms personnels masqués. Les captures ont été consultées pendant le travail mais le fichier n’est pas encore présent dans le dépôt.
- Relire les calculs et le compte rendu en équipe.

Les tests du notebook fourni passent, et les trames 2, 3 et 5 affichent « OK ». Ces vérifications portent sur les exemples du TP, sans constituer une validation exhaustive du décodeur. Ce dépôt est un travail pédagogique ; il ne constitue pas un dispositif de diagnostic.
