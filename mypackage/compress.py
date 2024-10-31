import os
import platform

if(platform.system()=="Windows"): path=r"C:\Just-For-Fun\mypackage\add"  #portable path
else: path="./add"

outfile=open(r'C:\Just-For-Fun\mypackage\mnplitedhex.txt','r+',encoding='utf-8')

with open(path, 'rb') as file:                                                                #simple preprocess
    while True:
        rawstr=file.readline().decode('utf-8')
        if not rawstr:
            break
        substr=rawstr[10:-19]
        writechar=outfile.write(str(substr)+'\n')
        #print(str(substr)+str(writechar))

def transtobin():
    outfile.seek(0)  #move file point to file start
    while True:
        char = outfile.read(1)
        '''if char != '0':
            dec = int(char,16)
            bin = bin(dec[2:])  #delete '0b' prefix'''

transtobin()


def writecmpfile():
    with open(r'C:\Just-For-Fun\mypackage\cmpedfile.cmp','x',encoding='utf-8') as cmpedfile:
        cmpedfile.writelines("000 /20 /03 /31 /04 /06")
        
writecmpfile()
"""
while True:
    char=outfile.read(1)
    count0 = 0
    count1 = 0
    if char == ' ':
        continue
    elif char=='0':
        count0+=1
    else :
        count1+=1
"""