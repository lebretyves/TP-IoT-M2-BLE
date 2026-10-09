# Bonus A, B et C — TP M2-3 — Équipe 02

Les trois bonus facultatifs du notebook fourni sont regroupés dans [TP_M2_3_BLE_bonus.ipynb](TP_M2_3_BLE_bonus.ipynb), séparément du TP obligatoire. Le notebook est autonome : il reprend le décodeur du professeur sans modifier sa fonction, puis les sept cellules de la section Bonus. Toutes ses cellules de code sont exécutées, avec leurs sorties conservées.

Depuis la racine du dépôt : `python executer_tp.py --bonus`.

## A — Trames réelles

Les cinq premières notifications de la Garmin sont `06 5B`, `06 5C`, `06 5C`, `06 5B`, `06 5B`. Le décodeur renvoie respectivement **91, 92, 92, 91 et 91 bpm**, avec contact détecté, sans énergie ni RR. Les répétitions correspondent à des notifications distinctes ; les horodatages sont dans le compte rendu principal.

## B — Fabriquer une trame

Les paramètres sont renseignés avec **75 bpm**, **contact détecté** et **RR = 0,78125 s**. L’encodeur produit **`16 4B 20 03`**, la trame 5 de l’exercice. Sa relecture confirme 75 bpm, contact détecté, RR affiché 781,2 ms et FC instantanée 76,8 bpm. Il s’agit d’un exercice d’encodage, pas d’un RR mesuré par la Garmin.

## C — Fréquence battement par battement

La série fictive de 12 intervalles fournie est conservée. Le graphique montre les valeurs `60 / RR`, de **73,0 à 78,4 bpm** environ, avec une moyenne arithmétique de **75,6 bpm**. Une moyenne unique masque les variations d’un battement à l’autre. Aucun RR réel n’a été transmis dans les trames Garmin recueillies : cette expérience reste explicitement fictive.
