'''
python script to manually convert all markdown docs to html

usage:
python md2html.py <filename>.md

writes in a html file in the same dir
'''

import markdown
import sys

input_file = sys.argv[1]

output_file = input_file.split('.')[0]

output_file += ".html"

with open(input_file, 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open(output_file, 'w') as f:
    f.write(html)

