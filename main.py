import PyPDF2

merger = PyPDF2.PdfFileMerger()

# ファイル数入力
print('ファイル数：')
file_num = int(input())

for i in range(file_num):
    # ファイルのパスを入力
    print('パス：')
    in_path = str(input())
    merger.append(in_path)

# 出力
print('出力先:')
out_path = str(input())
merger.write(out_path)
