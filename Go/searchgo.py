import os


path=r'C:\Just-For-Fun\Go\\'

go_files = [path+f for f in os.listdir(path) if f.endswith('.go')]

indexmain=go_files.index(path+"main.go")

go_files[0],go_files[indexmain]=go_files[indexmain],go_files[0]  #  main.go at first

# def nextfile():
#     n=0
#     while True:
#         yield go_files[n]
#         n+=1

for i, file in enumerate(go_files):
    go_files[i] = '"' + str(file) + '"'


print(' '.join(go_files))
