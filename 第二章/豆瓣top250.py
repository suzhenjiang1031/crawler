# 拿到页面源代码 requests
# 通过re或者正则表达式提取有效的信息 re
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
}

resp = requests.get(url, headers=headers)
page_content = resp.text

print(page_content)

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)
# 开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode = "w")
csvwriter = csv.writer(f)

for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("num")) 
    # print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic["year"].strip() 
    csvwriter.writerow(dic.vlaues())
f.close()
print("over!")