import re

# # findall：匹配字符串中所有符合正则的内容
# lst = re.findall(r"\d+", "我的电话号是：10086，我朋友的电话时是：10001")
# print(lst)

# # finditer：匹配字符串中所有的内容【返回的是迭代器】，从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+", "我的电话号是：10086，我朋友的电话时是：10001")
# for i in it:
#     print(i.group()) 

# # search，找到一个结果就返回，返回的的结果是match对象，拿数据需要.group()
# s = re.search(r"\d+", "我的电话号是：10086，我朋友的电话时是：10001")
# print(s.group())

# match,从头开始匹配
# s = re.match(r"\d+", "我的电话号是：10086，我朋友的电话时是：10001")
# print(s.group())

# 预加载正则表达式
obj = re.compile(r"\d+")

s = """
<div class='jay'><span id='1'>过秦岭</span></div>
<div class='jj'><span id='2'>宋体</span></div>
<div class='jolin'><span id='3'>大场面</span></div>
<div class='sylar'><span id='4'>发生在</span></div>
<div class='tory'><span id='5'>乱七八糟</span></div>
"""

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>.*?)'>(?P<wahaha>.*?)</span></div>", re.S) # re.S：让.能匹配换行符

result = obj.finditer(s)

for i in result:
    print(i.group("wahaha"))
    print(i.group("id"))
