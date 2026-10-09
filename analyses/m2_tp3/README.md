# TP M2-3 Bluetooth basse consommation

## État du travail

Voie réalisée : **A**, Garmin Forerunner 265 diffusant la fréquence cardiaque vers nRF Connect sur Samsung Galaxy S24 FE. Le journal du 9 octobre 2026 confirme la connexion, le service Heart Rate `0x180D` et la réception de notifications de Heart Rate Measurement `0x2A37`. Les trois relevés de distance/RSSI et le tableau des cinq appareils scannés sont renseignés.

Le fichier `trames_decodees.csv` contient les six trames fictives du PDF, exportées par la cellule « Livrable » du notebook officiel [TP_M2_3_BLE_decodeur.ipynb](TP_M2_3_BLE_decodeur.ipynb). Le décodeur autonome `decode_hrm.py` reste un complément et exporte désormais vers `trames_decodees_local.csv`, ignoré par Git, pour préserver le CSV officiel.

## Manipulations à réaliser

1. Installer/ouvrir nRF Connect, autoriser Bluetooth et les permissions demandées pour le scan.
2. Relever cinq appareils et anonymiser leurs noms. Observer uniquement les annonces des appareils tiers.
3. Sur un appareil appartenant à l’équipe, relever le RSSI à 30 cm, à 3 m et derrière une porte.
4. Activer la diffusion cardiaque de la montre si elle la propose. Fermer au besoin l’application sportive déjà connectée.
5. Avec l’accord du propriétaire, se connecter dans nRF Connect ; chercher le service Heart Rate 0x180D, puis Heart Rate Measurement 0x2A37.
6. Activer les notifications et relever cinq trames hexadécimales. Ne pas utiliser les fonctions de mise à jour DFU ni modifier les caractéristiques de l’appareil.
7. Enregistrer une capture du scan ou du service sous `capture_nrfconnect.png`, avec les noms personnels masqués avant dépôt.
8. Vérifier les trois calculs de `trames_decodees.md`, puis exécuter le notebook officiel dès qu’il est disponible.

Si aucun service Heart Rate n’est disponible après dix minutes, le sujet autorise la voie C : conserver le scan et travailler avec les trames fournies. Mettre alors à jour la voie effectivement utilisée.

## Relevés réels

Ne pas remplacer une observation manquante par une valeur fictive.

| Appareil | Nom anonymisé | RSSI dBm | Services annoncés UUID | Données fabricant | Ce que l’annonce révèle |
|---|---|---|---|---|---|
| 1 | Montre de l’équipe (Forerunner) | -50 | `0x180D` (liste incomplète de services 16 bits) ; Service Data associé à `0xFE1F` | Aucun champ Manufacturer Data affiché ; Service Data : `0x020208C18114` | Le nom révèle la gamme de la montre ; `0x180D` révèle une fonction de fréquence cardiaque. |
| 2 | Appareil inconnu 1 (N/A) | -59 | `0xFE78` (liste complète de services 16 bits) ; Service Data associé à `0xFDF7` | Oui : « HP, Inc. » affiché par nRF Connect, identifiant `0x0065`, données `0x01F005` | Aucun nom affiché ; l’annonce révèle un identifiant fabricant et des UUID, sans permettre d’identifier précisément le modèle ou le propriétaire. |
| 3 | Balise anonyme (N/A, iBeacon) | -64 | Aucun UUID de service affiché ; UUID de balise dans le champ Beacon : `2686f39c-bada-4658-854a-a62e7e5e8b8d` | Oui : champ Beacon, « Apple, Inc. » `0x004C`, type `0x02`, longueur 21 octets, Major 1, Minor 0 | Aucun nom affiché ; l’annonce expose un identifiant de balise et ses valeurs Major/Minor. L’identifiant Apple affiché ne suffit pas à identifier le modèle matériel. |
| 4 | Appareil à nom personnel (anonymisé) | -68 | `0x180A` ; `3e1d50cd-7e3e-427d-8e1c-b78aa87fe624` (listes complètes affichées, 16 et 128 bits) | Aucun champ Manufacturer Data affiché | Le nom local complet contient un prénom, susceptible d’identifier le propriétaire ; l’application indique « CLASSIC and LE ». |
| 5 | Appareil à identifiant technique (préfixe NBLT, suffixe anonymisé) | -88 | `6e400001-0000-0000-e070-6a6f66637075` (liste complète de services 128 bits, confirmée dans RAW) | Oui : « Reserved ID » `0x434E`, données `0x0100020000FC` | Le nom local complet expose un identifiant technique ; l’application indique « LE only ». Le champ fabricant affiché ne permet pas d’attribuer un constructeur. |

Sources : captures des annonces dépliées fournies dans la conversation, horloge du téléphone à 15:10 pour l’appareil 1, 15:11 pour l’appareil 2, 15:13 pour l’appareil 3, 15:15 pour l’appareil 4 et 15:17 pour l’appareil 5. Ce sont des RSSI ponctuels à des distances inconnues, pas les mesures à 30 cm, 3 m et derrière une porte. Pour le cinquième appareil, le tableau final retient l’appareil NBLT dont l’annonce détaillée a été fournie, à la place de la seconde balise iBeacon initialement envisagée. La capture de 15:10 confirme directement la présence de `0x180D` dans l’annonce de la montre.

Vérification de l’appareil 5 : la capture RAW à 15:19 montre un champ de type `0x07`, longueur 17 (type + 16 octets), de valeur `757063666F6A70E0000000000100406E`. La lecture des 16 octets en little-endian donne `6e400001-0000-0000-e070-6a6f66637075`, vérifié avec Python. Le champ fabricant de type `0xFF` contient `4E430100020000FC` : identifiant `0x434E`, puis données `0100020000FC`.

Pour la balise anonyme, l’application affiche également « RSSI at 1m: 11 dBm » dans le champ Beacon. Cette valeur annoncée est distincte du signal effectivement reçu de −64 dBm ; aucune mesure à 1 m de cette balise n’a été réalisée. Son UUID de balise n’est pas à confondre avec un UUID de service GATT.

Détail de l’annonce de la montre : type d’appareil « LE only », annonce « Legacy », flags « LE General Discoverable, BR/EDR Not Supported », nom local abrégé « Forerunner ». Le champ Service Data (`0xFE1F`, données `0x020208C18114`) est distinct d’un champ Manufacturer Data : ne pas les confondre.

RSSI de l’appareil de l’équipe (Garmin Forerunner 265) : **30 cm = −60 dBm** (mesure lue et distance confirmée par l’utilisateur) ; **environ 3 m = −76 dBm** (valeur communiquée après la consigne de mesure à 3 m) ; **derrière une porte = −65 dBm** (valeur communiquée après la consigne de placer les appareils de part et d’autre d’une porte fermée ; distance non précisée).

Le signal est plus faible à 3 m qu’à 30 cm (écart de −16 dB). La mesure derrière la porte est plus forte que celle à 3 m, mais la distance et l’orientation ne sont pas contrôlées : ces relevés ponctuels ne permettent pas d’isoler l’effet de la porte ni de convertir le RSSI en distance précise.

### Cinq trames réelles de la Garmin

Les cinq premières notifications cardiaques du journal fourni sont conservées ci-dessous, y compris les valeurs répétées : ce sont cinq réceptions distinctes.

| Heure du journal | Trame hexadécimale | FC (bpm) | Contact |
|---|---|---:|---|
| 14:57:50.617 | `06 5B` | 91 | Détecté |
| 14:57:51.151 | `06 5C` | 92 | Détecté |
| 14:57:51.512 | `06 5C` | 92 | Détecté |
| 14:57:52.056 | `06 5B` | 91 | Détecté |
| 14:57:52.596 | `06 5B` | 91 | Détecté |

Décodage : `06` = `00000110`. Le bit 0 vaut 0 : FC codée sur un octet (uint8). Les bits 1 et 2 valent 1 : détection du contact prise en charge et contact détecté. Les bits 3 et 4 valent 0 : énergie et intervalles RR absents. `5B` = 5 × 16 + 11 = **91 bpm** ; `5C` = 5 × 16 + 12 = **92 bpm**. Aucun calcul de RR ni de FC à partir de RR n’est possible avec ces trames.

Le journal contient **160 notifications cardiaques**, de 14:57:50.617 à 14:59:12.242, entre **88 et 95 bpm**. Toutes ont les flags `06`. Le décodeur local a vérifié les 160 valeurs contre les valeurs en bpm affichées dans le journal nRF Connect : elles concordent.

Les notifications horodatées, sans adresse Bluetooth, sont enregistrées dans [notifications_garmin_2026-10-09.txt](notifications_garmin_2026-10-09.txt). Leur décodage complet est dans [mesures_garmin.json](mesures_garmin.json). Les trames des autres caractéristiques Garmin ont été exclues.

La capture du service partagée dans la conversation affiche également **89 bpm**, contact détecté et notifications activées. Pour le fichier de rendu demandé, l’équipe a fourni la capture du scan à 15:17 : [capture_nrfconnect.png](capture_nrfconnect.png), avec le prénom masqué par un rectangle opaque. Le PNG conserve les dimensions originales (945 × 2048) et tous les pixels hors de ce rectangle, vérifiés par comparaison avec le JPEG décodé. Le premier journal ne contenait aucune notification `0x2A37` ; la réception a fonctionné après l’arrêt forcé de Garmin Connect et une nouvelle connexion. Cette succession ne suffit pas à établir avec certitude la cause du blocage.

## Questions du scan

### a. Pourquoi le RSSI ne donne-t-il pas une distance précise ?

Le signal dépend aussi des obstacles, de l’orientation, du corps humain, des réflexions radio et de la puissance d’émission. Une même distance peut donc produire plusieurs RSSI ; ces mesures donnent une tendance, pas une distance précise.

### b. Que peut révéler un nom diffusé ?

Un prénom, un numéro de chambre ou un type d’équipement peuvent permettre d’associer une personne à un appareil et à un contexte de soins. Un identifiant neutre évite de diffuser directement ces informations dans le nom.

### c. Des adresses changent-elles et pourquoi ?

Observation de nos captures : la montre conserve la même adresse entre les observations disponibles. Un même prénom apparaît avec deux adresses différentes entre les scans de 14:41 et 14:57 ; cela ne suffit pas à confirmer qu’il s’agit du même appareil ayant changé d’adresse. Des adresses privées renouvelées peuvent limiter le suivi d’un appareil au fil des scans ; leur présence dépend de l’appareil et de son mode de fonctionnement.

## Comprendre GATT et le lien avec le projet 1

La montre joue le rôle de serveur GATT : elle fournit les données. Le téléphone, client GATT, s’abonne aux mesures. Le service Heart Rate `0x180D` regroupe les caractéristiques cardiaques ; Heart Rate Measurement `0x2A37`, de propriété NOTIFY, contient la mesure. L’abonnement passe par le descripteur CCCD `0x2902`. Une notification permet au serveur d’envoyer la nouvelle valeur sans lecture répétée demandée par le client.

À l’étape 6, l’énoncé demande une lecture du squelette ESP32, pas une réalisation matérielle aujourd’hui. Au projet 1, l’ESP32 remplacera la montre et enverra la FC calculée depuis le MAX30102. La ligne `trame[0] = 0x16;` annonce une FC sur un octet, le contact pris en charge et détecté, et un intervalle RR présent. Le squelette déduit un RR d’une FC simulée ; ce n’est pas une mesure réelle d’intervalle RR. Les trames Garmin observées commencent par `0x06`, sans RR.

## Notebook officiel complété

Le notebook principal conserve les 17 cellules de la partie obligatoire. Dans le code, seules les valeurs de `MES_FC` pour les trames 2, 3 et 5 (90, 62 et 75 bpm) ont été renseignées. Les fonctions et les tests du professeur restent inchangés. Les réponses ci-dessous figurent aussi dans la cellule Markdown des questions. Les sept cellules facultatives ont été déplacées dans [le sous-dossier bonus](bonus/README.md), où le décodeur fourni est repris pour une exécution autonome. Le bonus A contient les cinq trames Garmin ; le bonus B utilise 75 bpm et un RR de 0,78125 s ; le bonus C conserve les données fictives fournies.

Depuis la racine du dépôt : `python -m pip install -r requirements.txt`, puis `python executer_tp.py`. Le script exécute le notebook dans `analyses/m2_tp3/`, enregistre ses sorties et produit le CSV officiel à cet emplacement.

## Réponses aux cinq questions du notebook

1. **Pourquoi prévoir une FC sur deux octets ?** Un octet ne représente que 0 à 255 ; le format uint16 permet de coder des valeurs au-delà de 255 sans changer de caractéristique. Le bit 0 précise le format employé : 255 est une limite d’encodage, pas une limite physiologique universelle.

2. **Que faire de `04 3E` ?** Le capteur sait détecter le contact, mais indique son absence. L’application doit afficher « contact absent / mesure non fiable » et ne pas présenter les 62 bpm au soignant comme une mesure valide ; si la valeur est conservée ou transmise, elle doit rester explicitement marquée invalide.

3. **Pourquoi deux RR dans la trame 6 ?** Une notification peut regrouper plusieurs intervalles entre battements, du plus ancien au plus récent. La FC annoncée (78 bpm) est une valeur distincte, potentiellement lissée, qui ne remplace pas les deux RR de 734,375 et 765,625 ms.

4. **RR de la trame 5 lu en big-endian ?** `20 03` devient `0x2003` = 8195, soit 8195 / 1024 = **8,00293 s** (8002,93 ms), au lieu de 0,78125 s. Cela correspond à environ **7,50 bpm**, très incohérent avec les 75 bpm annoncés : la comparaison FC/RR et un contrôle de plausibilité auraient signalé l’erreur de lecture.

5. **Pourquoi un format normalisé ?** Des capteurs et des clients de fabricants différents peuvent interpréter les mêmes champs, unités et indicateurs de qualité. Cela facilite les tests et réduit les ambiguïtés d’intégration, sans garantir à lui seul la sécurité ou la validation du dispositif.

## Vérification locale

Depuis ce dossier : `python decode_hrm.py`.
Les tests vérifient les six FC attendues, l’énergie, les RR, les états de contact, une FC uint16 supérieure à 255 et le rejet de trames incomplètes ou incohérentes.

## Avant de rendre

- [x] Calculs expliqués des trames 3, 5 et 2 préparés.
- [x] Décodeur local et export des six trames fictives préparés.
- [x] Tableau des cinq appareils et mesures de RSSI complétés.
- [x] Connexion voie A et cinq trames cardiaques réelles décodées.
- [x] Capture anonymisée enregistrée et vérifiée.
- [x] Notebook officiel exécuté et ses cinq questions traitées.
- [x] Livrables préparés pour le dépôt de l’équipe.
- [ ] Relecture des résultats par l’équipe et transmission du lien au professeur.
