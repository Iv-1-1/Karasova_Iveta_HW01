
import json
soubor = 'alice.txt'

with open(soubor, 'r', encoding='utf-8') as text_obsah:
    text_porovnani = text_obsah.read()

slovnik = {}
text_vycistit = text_porovnani.replace(' ', '')
for pismeno in text_vycistit:
    if pismeno.isalpha:
        pismeno = pismeno.lower()
    if pismeno != '\n':
        if pismeno in slovnik:
            slovnik[pismeno] += 1
        else:
            slovnik[pismeno] = 1

with open('hw01_output.json.', mode='w', encoding='utf-8') as text_zapis:
    json.dump(dict(sorted(slovnik.items())), text_zapis)