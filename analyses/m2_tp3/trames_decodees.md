# Décodage expliqué des trois trames

Calculs préparés à partir des trames fictives de l’énoncé, à comprendre et vérifier par l’équipe. Ils ne proviennent pas de la montre.

## Trame 3 : 06 3E

06 = 0000 0110 : bit 0 nul, donc FC sur un octet ; bits 1 et 2 à 1, donc détection de contact prise en charge et contact détecté. Énergie et RR absents.

3E = 3 × 16 + 14 = **62 bpm**. Deux octets consommés sur deux.

## Trame 5 : 16 4B 20 03

16 = 0001 0110 : FC sur un octet ; contact pris en charge et détecté ; énergie absente ; RR présent.

4B = 4 × 16 + 11 = **75 bpm**.

20 03 se lit 0x0320 en little-endian : 3 × 256 + 32 = 800.
RR = 800 / 1024 = **0,78125 s = 781,25 ms**.
FC instantanée = 60 / 0,78125 = **76,8 bpm**.
Quatre octets consommés sur quatre. La FC annoncée et la FC calculée sur un RR ne sont pas nécessairement identiques.

## Trame 2 : 01 5A 00

01 = 0000 0001 : FC sur deux octets. La détection de contact n’est pas prise en charge : ne pas conclure à une absence de contact. Énergie et RR absents.

5A 00 se lit 0x005A : 0 × 256 + 90 = **90 bpm**.
Trois octets consommés sur trois.

| Trame | Flags | Format FC | Contact | FC bpm | Énergie kJ | RR ms | FC instantanée bpm |
|---|---|---|---|---:|---|---|---|
| 3 | 00000110 | uint8 | Détecté | 62 | Absent | Absent | Non calculable |
| 5 | 00010110 | uint8 | Détecté | 75 | Absent | 781,25 | 76,8 |
| 2 | 00000001 | uint16 | Non pris en charge | 90 | Absent | Absent | Non calculable |
