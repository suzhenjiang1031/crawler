# 拿到页面源代码 requests
# 通过re或者正则表达式提取有效的信息 re
import requests
import re

url = "https://movie.douban.com/top250"
headers = {
    "user-agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
}

resp = requests.get(url, headers=headers)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)
# 开始匹配
result = obj.finditer(page_content)
for it in result:
    print(it.group("name"))