import urllib.request
import re
import ssl
import os

# 目标URL
url = "https://tieba.baidu.com/p/5059180075?red_tag=0069685467"

# 取消SSL证书验证
ssl._create_default_https_context = ssl._create_unverified_context

def baidu(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
    return data

def parse(html, folder_name):
    # 正则表达式匹配图片URL
    pat = r'<img class="BDE_Image".*?src="([^"]*\.jpg)"'
    imagelist = re.compile(pat).findall(html)
    
    # 创建新文件夹
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for idx, each in enumerate(imagelist, start=1):
        print(each)
        # 保存文件到本地
        file = os.path.join(folder_name, f"{idx}.jpg")
        urllib.request.urlretrieve(each, filename=file)

if __name__ == "__main__":
    # 定义文件夹名称
    folder_name = "downloaded_images"
    html = baidu(url)
    parse(html, folder_name)
