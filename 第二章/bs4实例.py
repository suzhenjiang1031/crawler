# import requests
# from bs4 import BeautifulSoup

# # 1. 拿到页面源代码
# # 2. 使用bs4进行解析，拿到数据

# url = "http://www.xinfadi.com.cn/getPriceData.html"

# dat = {
#     "kw": s
# }

# resp = requests.post(url)

# # 解析数据
# # 1. 把页面源代码交给BeatuifulSoup进行处理，生成bs对象
# page = BeautifulSoup(resp.text, "html.parser") # 指定html解析器

# # 2. 从bs对象中查找数据
# # find(标签，属性=值)
# # findall(标签，属性=值)
# page.find("table", attrs={"class": "hq_table"}) # class是python里的关键字

# # 拿到所有数据行
# trs = table.find_all("tr")[1:]

# for tr in trs:  # tr每一行数据
#     tds = tr.find_all("td") # 拿到每行中的所有td
#     name = tds[0].text # .text表示拿到被标签标记的内容
#     low = tds[1].text
#     avg = tds[2].text
#     high = tds[3].text
#     gui = tds[4].text
#     kind = tds[5].text
#     data = tds[6].text