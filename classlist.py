import os
# Create .pdf file from .tex file with xelatex
cmd = "xelatex classlist.tex"
failure = os.system(cmd)
if failure:
    print('Creating "classlist.pdf" failed!!!')
# Viewing classlist.pdf
cmd = "evince classlist.pdf &"
failure = os.system(cmd)
if failure:
    print('Viewing "classlist.pdf" failed!!!')

