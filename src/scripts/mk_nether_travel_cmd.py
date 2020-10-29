from pathlib import Path
import re

base_str = '!commands edit !blindtravel $(eval {})'

import requests


js_code = Path.cwd().parent / 'commands' / 'blind_travel_cmd.js'

url = 'https://javascript-minifier.com/raw'
data = {'input': open(js_code, 'rb').read()}
response = requests.post(url, data=data)



inp_txt = js_code.read_text()

minified = response.text

# print(minified)

print(base_str.format(minified))