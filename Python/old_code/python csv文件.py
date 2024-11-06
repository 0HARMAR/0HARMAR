import csv
from pathlib import Path
headers = ['学号','姓名','分数']
rows = [('202001','张三','98'),
        ('202002','李四','95'),
        ('202003','王五','92'),
        ('202004','none','100')]
with open('myfile.csv','w',newline='') as m:    #创建csv文件
    writer=csv.writer(m)
    writer.writerow(headers)
    writer.writerows(rows)
path=Path('myfile.csv')
lines=path.read_text().splitlines()
reader=csv.reader(lines)
header_row=next(reader)
print(type(reader))