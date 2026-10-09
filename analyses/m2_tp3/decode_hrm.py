"""Décodeur pédagogique autonome basé sur le format du PDF du TP.

Ce script complète le notebook officiel sans remplacer son export CSV.
Exécution : python decode_hrm.py
"""
import csv
import json
from pathlib import Path

TRAMES = ['00 48', '01 5A 00', '06 3E', '0E 55 E8 03',
          '16 4B 20 03', '1E 4E C8 00 F0 02 10 03']


def decode_hrm(hexadecimal):
    data = bytes.fromhex(hexadecimal.replace('-', ' '))
    if not data:
        raise ValueError('Trame vide')
    flags = data[0]
    if flags & 0xE0:
        raise ValueError('Bits réservés non nuls')
    offset = 1

    def read(size):
        nonlocal offset
        if offset + size > len(data):
            raise ValueError('Trame tronquée')
        result = int.from_bytes(data[offset:offset + size], 'little')
        offset += size
        return result

    heart_rate = read(2 if flags & 1 else 1)
    contact = ('détecté' if flags & 2 else 'non détecté') if flags & 4 else 'non pris en charge'
    energy = read(2) if flags & 8 else None
    rr = []
    if flags & 16:
        if offset == len(data) or (len(data) - offset) % 2:
            raise ValueError('Champ RR absent ou incomplet')
        while offset < len(data):
            rr.append(read(2))
    if offset != len(data):
        raise ValueError('Octets supplémentaires non annoncés')
    return dict(trame=data.hex(' ').upper(), flags=f'{flags:08b}',
                format_fc='uint16' if flags & 1 else 'uint8', contact=contact,
                fc_bpm=heart_rate, energie_kj=energy, rr_bruts=rr,
                rr_ms=[x * 1000 / 1024 for x in rr],
                fc_instantanee_bpm=[60 * 1024 / x if x else None for x in rr])


def tests():
    rows = [decode_hrm(t) for t in TRAMES]
    assert [r['fc_bpm'] for r in rows] == [72, 90, 62, 85, 75, 78]
    assert rows[2]['contact'] == 'détecté'
    assert rows[1]['contact'] == 'non pris en charge'
    assert rows[3]['energie_kj'] == 1000
    assert rows[4]['rr_ms'] == [781.25]
    assert rows[5]['rr_bruts'] == [752, 784]
    assert rows[5]['energie_kj'] == 200
    assert decode_hrm('01 2C 01')['fc_bpm'] == 300
    assert decode_hrm('04 48')['contact'] == 'non détecté'
    for invalid in ['', '01 5A', '08 48 01', '10 48', '10 48 01', '00 48 00', 'E0 48']:
        try:
            decode_hrm(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f'Trame invalide acceptée : {invalid}')
    return rows


if __name__ == '__main__':
    rows = tests()
    output = Path(__file__).with_name('trames_decodees_local.csv')
    with output.open('w', newline='', encoding='utf-8-sig') as stream:
        writer = csv.DictWriter(stream, fieldnames=['numero'] + list(rows[0]))
        writer.writeheader()
        for i, row in enumerate(rows, 1):
            writer.writerow({'numero': i, **{k: json.dumps(v) if isinstance(v, list) else v for k, v in row.items()}})
    print('Tous les tests du décodeur local sont passés.')
    print(f'Export : {output}')
    for i, row in enumerate(rows, 1):
        print(i, row)
