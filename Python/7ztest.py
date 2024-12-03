import py7zr

# 要压缩的文件路径或文件夹路径
file_to_compress = r'C:\Just-For-Fun\Python\client.py'  # 替换为您要压缩的文件路径
output_file = r'C:\Just-For-Fun\Python\client.7z'  # 目标 7z 文件名

"""# 使用 SevenZipFile 来压缩文件
with py7zr.SevenZipFile(output_file, mode='w') as archive:
    archive.write(file_to_compress, arcname='.')  # 使用 arcname 将文件放在压缩包根目录"""

with py7zr.SevenZipFile(output_file, mode='r') as z:
        z.extractall(path=r'C:\Just-For-Fun\Python\client1.py')
        print("Extraction successful.")