# TP M2-3 — Bluetooth basse consommation — Équipe 02

TP du 9 octobre 2026, Digi5, module 2, Epitech MBA Santé, IA & IoT, à partir de l’énoncé étudiant de Nicolas Laurio.

Équipe GitHub : [lebretyves](https://github.com/lebretyves), [Faucourt](https://github.com/Faucourt) et [aglnix](https://github.com/aglnix).

## Travail réalisé

La voie A utilise une Garmin Forerunner 265 et nRF Connect sur Samsung Galaxy S24 FE. Le service Heart Rate `0x180D` et la caractéristique `0x2A37` ont été observés ; 160 notifications cardiaques ont été reçues et décodées. Les cinq premières sont détaillées dans le compte rendu.

- [Compte rendu](analyses/m2_tp3/README.md) : cinq appareils scannés, annonces anonymisées, trois relevés RSSI, questions a–c, mesures Garmin et explications GATT.
- [Décodage expliqué des trames 3, 5 et 2](analyses/m2_tp3/trames_decodees.md).
- [CSV des six trames fictives](analyses/m2_tp3/trames_decodees.csv), généré par le décodeur local.
- [Décodeur Python](analyses/m2_tp3/decode_hrm.py), avec ses vérifications.
- [Notifications Garmin horodatées](analyses/m2_tp3/notifications_garmin_2026-10-09.txt) et [mesures décodées](analyses/m2_tp3/mesures_garmin.json), sans nom du porteur ni adresse Bluetooth.
- [Énoncé du TP](TP_M2_3_BLE_nRFConnect_etudiant.pdf).

## Vérification locale

Python 3.10 ou plus récent ; aucune dépendance externe.

```powershell
python analyses/m2_tp3/decode_hrm.py
```

Le script vérifie les décodages puis régénère `analyses/m2_tp3/trames_decodees.csv` pour les six trames fictives du sujet. Les mesures réelles de la montre sont conservées séparément.

## À terminer avant le rendu

- Récupérer `TP_M2_3_BLE_decodeur.ipynb` sur Teams / Moodle, l’exécuter, compléter ses cinq questions et remplacer le CSV local par l’export de sa cellule « Livrable ».
- Enregistrer `analyses/m2_tp3/capture_nrfconnect.png` à partir d’une capture réelle de nRF Connect, avec les noms personnels masqués. Les captures ont été consultées pendant le travail mais le fichier n’est pas encore présent dans le dépôt.
- Relire les calculs et le compte rendu en équipe.

Le décodeur local ne remplace pas le notebook officiel manquant. Ce dépôt contient un travail pédagogique en cours ; il ne constitue pas un dispositif de diagnostic.
