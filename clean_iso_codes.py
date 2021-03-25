'''
    flip the keys and values from http://country.io/iso3.json, found in country_codes.txt
'''

import json

codes = {}
with open("country_codes.txt") as f:
    for line in f.readlines():
        if len(line) > 2:
            iso2 = line[3:5]
            iso3 = line[9:12]
            codes[iso3] = iso2

with open("iso3_to_iso2.json", "w") as f:
    f.write(json.dumps(codes))
