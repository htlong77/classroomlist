import os
# Creating .tex file from within python

texfilename = "lastclasslist.tex"
fout = open(texfilename, "w")
fout.close()

# Creating .pdf file from .tex file with xelatex
cmd = "xelatex classlist.tex"
failure = os.system(cmd)
if failure:
    print('Creating "classlist.pdf" failed!!!')
# Viewing classlist.pdf
cmd = "evince classlist.pdf &"
#failure = os.system(cmd)
#if failure:
#    print('Viewing "classlist.pdf" failed!!!')

