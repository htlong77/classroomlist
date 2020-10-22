import os
# Creating .tex file from within python
import sys
script, subject, class_code, num_of_credits = sys.argv
texfilename = "classlist.tex"
fout = open(texfilename, "w")
content = r"""\documentclass[a4paper, 12pt]{article}
\usepackage[left=0.2cm, right=0.2cm, top=1cm, bottom=2.00cm]{geometry} %%Set border
\begin{document}
\noindent\begin{minipage}[c]{10cm}
\begin{center}
 ĐẠI HỌC QUỐC GIA HÀ NỘI\\
 \textbf{TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN}
\end{center}
\end{minipage} 
\hfill
\begin{minipage}[c]{9cm}
\begin{center}
 CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM\\
 \textbf{Độc lập - Tự do - Hạnh phúc}
\end{center}
\end{minipage} 

\centerline{\textbf{HỌC KỲ 1 2020-2021}}

\noindent
\begin{minipage}[c]{11cm}
 Học phần: \textbf{%s}\\
 Thứ: 4
\end{minipage} 
\hfill
\begin{minipage}[c]{4.5cm}
 Lớp HP: \textbf{%s}\\
 Tiết: 9-10
\end{minipage} 
\hfill
\begin{minipage}[c]{4cm}
 Số tín chỉ: \textbf{%s}\\
 Giảng đường: 201-T5
\end{minipage} 
\vspace{0.2cm}
\noindent\begin{tabular}{*{9}{|c}|}
  \hline
    STT&Mã SV&Họ và tên&Ngày sinh&Lớp&Thường xuyên&Ký nộp&Giữa kỳ&Ghi chú\\
  \hline
    1&19000243&Đặng Quang Anh&27/07/2001&64 Toán tin&&&&\\
  \hline
\end{tabular}
\end{document}
""" % (subject, class_code, num_of_credits)
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
cmd = f"evince {pdffilename} &"
failure = os.system(cmd)
if failure:
    print(f'Viewing "{pdffilename}" failed!!!')

# Thử lần cuối xem còn bị đưa classlist.tex lên không
