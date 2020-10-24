from pathlib import Path
import re

base_str = '!commands edit !testcalc $(eval {})'

js_code = Path.cwd().parent / 'commands' / 'test_calc_cmd.js'

inp_txt = js_code.read_text()

minified = re.sub('\n+', ' ', inp_txt)

# print(minified)

print(base_str.format(minified))