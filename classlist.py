import os
# Creating .tex file from within python

texfilename = "classlist.tex"
fout = open(texfilename, "w")
content = r"""\documentclass[a4paper,12pt]{book}
\begin{document}
\centerline{\textbf{HỌC KỲ 1 2020-2021}}
\begin{tabular}{*{9}{|c}|}
  \hline
    STT&Mã SV&Họ và tên&Ngày sinh&Lớp&Thường xuyên&Ký nộp&Giữa kỳ&Ghi chú\\
  \hline
    1&19000243&Đặng Quang Anh&27/07/2001&64 Toán tin&&&&\\
  \hline
\end{tabular}
\end{document}
"""
fout.write(content)
fout.close()

# Creating .pdf file from .tex file with xelatex
cmd = f"xelatex {texfilename}"
failure = os.system(cmd)
pdffilename = f"{texfilename[0:-4]}.pdf"
if failure:
    print(f'Creating "{pdffilename}"  failed!!!')
else:
    print(f'Creating "{pdffilename}" successfully!!!')
    
# Viewing classlist.pdf
cmd = "evince classlist.pdf &"
#failure = os.system(cmd)
#if failure:
#    print('Viewing "classlist.pdf" failed!!!')

