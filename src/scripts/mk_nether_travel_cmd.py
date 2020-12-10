from pathlib import Path
import re

base_str = '!commands add !blindtravel $(eval {})'

import requests


js_code = Path.cwd().parent / 'commands' / 'blind_travel_cmd.js'
tmp_fil = Path.cwd() / 'tmp.js'
tmp_fil.touch()

inp_txt = js_code.read_text()

lines = []

for ln in inp_txt.split("\n"):
    lines.append(ln)
last_line = lines[-1]
# lines = lines[:-1]

tmp_fil.write_text("\n".join(lines))
# print(tmp_fil.read_text())

url = 'https://javascript-minifier.com/raw'
data = {'input': open(tmp_fil, 'rb').read()}
response = requests.post(url, data=data)

minified = response.text

tmp_fil.unlink()

# print(minified)

minified += last_line

# print(minified)

print(base_str.format(minified))