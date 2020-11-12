import os
# Creating .tex file from within python
import sys

def import_student_data(filename):
    """This function will import student data from a csv file (classlist.dat)"""
    print(f"Importing student data from file '{filename}'")
    datafile = open(filename,'r')
    lines = datafile.readlines()
    print(lines)
    for line in lines:
        print(line)
        student_id, student_name, student_date_of_birth, student_training_program = line.split(',')
        student_id = student_id.strip() 
        student_name = student_name.strip()
        student_date_of_birth = student_date_of_birth.strip()
        student_training_program = student_training_program.strip()
        print(f"Mã sinh viên '{student_id}', Họ và tên '{student_name}', Ngày sinh '{student_date_of_birth}', Chương trình đào tạo '{student_training_program}'")
        
    datafile.close()
    return

def main():
#    script, subject, class_code, num_of_credits, day_of_week, class_hours, class_room = sys.argv

    # default values of input parameters:
    subject = "Thực tập tin học vật lý"
    class_code = "PHY3376 QTL"
    num_of_credits = "2"
    day_of_week = "5"
    class_hours = "2-5"
    class_room = "408-T5"
# read variables from the command line, one by one:
    while len(sys.argv) > 1:
        option = sys.argv[1]; del sys.argv[1]
        if option == '-s':
            subject = sys.argv[1]; del sys.argv[1]
        else:
            print(f"{sys.argv[0]} : invalid option {option}")
            sys.exit(1)
#
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
\begin{minipage}[c]{10cm}
 Học phần: \textbf{%s}\\
 Thứ: %s
\end{minipage} 
\hfill
\begin{minipage}[c]{5.5cm}
 Lớp HP: \textbf{%s}\\
 Tiết: %s
\end{minipage} 
\hfill
\begin{minipage}[c]{4cm}
 Số tín chỉ: \textbf{%s}\\
 Giảng đường: %s
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
""" % (subject, day_of_week, class_code, class_hours, num_of_credits, class_room)
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
# Có vẻ đã giải quyết xong https://stackoverflow.com/questions/3833561/why-doesnt-git-ignore-my-specified-file/3833675#:~:text=gitignore%20files%20don't%20work,matching%20rules%20will%20be%20skipped.

    filename = 'classlist.dat'
    import_student_data(filename)

if __name__ == '__main__':
    main()
