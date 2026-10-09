# TP M2-3 — Bluetooth basse consommation — Équipe 02

TP du 9 octobre 2026, Digi5, module 2, Epitech MBA Santé, IA & IoT, à partir de l’énoncé étudiant de Nicolas Laurio.

Équipe GitHub : [lebretyves](https://github.com/lebretyves), [Faucourt](https://github.com/Faucourt) et [aglnix](https://github.com/aglnix).

## Travail réalisé

La voie A utilise une Garmin Forerunner 265 et nRF Connect sur Samsung Galaxy S24 FE. Le service Heart Rate `0x180D` et la caractéristique `0x2A37` ont été observés ; 160 notifications cardiaques ont été reçues et décodées. Les cinq premières sont détaillées dans le compte rendu.

- [Notebook obligatoire complété et exécuté](analyses/m2_tp3/TP_M2_3_BLE_decodeur.ipynb) : les 17 cellules de la partie obligatoire, réponses manuelles vérifiées, cinq questions traitées et export officiel.
- [Bonus A, B et C séparés](analyses/m2_tp3/bonus/README.md) : notebook autonome exécuté dans `analyses/m2_tp3/bonus/`.
- [Compte rendu](analyses/m2_tp3/README.md) : cinq appareils scannés, annonces anonymisées, trois relevés RSSI, questions a–c et cinq réponses du notebook, mesures Garmin et explications GATT.
- [Décodage expliqué des trames 3, 5 et 2](analyses/m2_tp3/trames_decodees.md).
- [CSV des six trames fictives](analyses/m2_tp3/trames_decodees.csv), exporté par la cellule « Livrable » du notebook officiel.
- [Capture réelle du scan nRF Connect](analyses/m2_tp3/capture_nrfconnect.png), avec le prénom masqué.
- [Décodeur Python](analyses/m2_tp3/decode_hrm.py), avec ses vérifications.
- [Notifications Garmin horodatées](analyses/m2_tp3/notifications_garmin_2026-10-09.txt) et [mesures décodées](analyses/m2_tp3/mesures_garmin.json), sans nom du porteur ni adresse Bluetooth.
- [Énoncé du TP](TP_M2_3_BLE_nRFConnect_etudiant.pdf).

## Vérification locale

Python 3.10 ou plus récent. Pour réexécuter le notebook et régénérer son CSV officiel :

```powershell
python -m pip install -r requirements.txt
python executer_tp.py
```

Le script lance le notebook depuis son dossier de livrables et enregistre les sorties dans le fichier `.ipynb`. Les fonctions et tests du professeur sont conservés ; seul `MES_FC` a été renseigné dans le code obligatoire. Les réponses sont ajoutées à la cellule Markdown des questions. Les sept cellules facultatives du fichier fourni ont été déplacées dans un notebook autonome séparé, avec le décodeur nécessaire à leur exécution.

Pour exécuter les trois bonus :

```powershell
python executer_tp.py --bonus
```

Le décodeur autonome reste utilisable sans dépendance externe :

```powershell
python analyses/m2_tp3/decode_hrm.py
```

Ce décodeur complémentaire écrit désormais `analyses/m2_tp3/trames_decodees_local.csv` (ignoré par Git), pour ne pas écraser l’export officiel. Les mesures réelles de la montre sont conservées séparément.

## État du rendu

Les fichiers demandés à la section 6 de l’énoncé sont présents dans `analyses/m2_tp3/`. La capture provient du fichier réel fourni par l’utilisateur ; seul un rectangle opaque recouvre le prénom. Ses dimensions (945 × 2048) et tous les pixels extérieurs au rectangle sont conservés. L’original non masqué est exclu de Git.

Il reste à l’équipe à relire le rendu et à transmettre le lien du dépôt selon les consignes du professeur.

Les tests du notebook fourni passent, et les trames 2, 3 et 5 affichent « OK ». Ces vérifications portent sur les exemples du TP, sans constituer une validation exhaustive du décodeur. Ce dépôt est un travail pédagogique ; il ne constitue pas un dispositif de diagnostic.
