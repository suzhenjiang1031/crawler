# 1. 拿到主页面的源代码，然后提取到子页面的链接地址
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址，img -> src
# 3.下载图片

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'

# 把源代码交给BeautifulSoup处理
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_ = "item_list infinite_scroll").find_all("a") 
# print(alist)
for a in alist:
    href = 'www.umei.cc' + a.get('href') # 直接通过get就可以拿到属性的值
     # 拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 从子页面中提取到图片的下载路径，然后下载到本地
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("")
    img = p.find("img")
    src = img.get("src")
    # 下载图片
    img_resp = requests.get(src)
    img_resp.content # 这里拿到的是字节
    img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    with open("img/"+img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
    
    print("over!", img_name)
    time.sleep(1) # 通过sleep函数可以控制爬取速度
print("all over!")