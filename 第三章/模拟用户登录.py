# 登录 -> 得到cookie
# 通过cookie请求到对应的书架信息 -> 得到书架的内容

# 必须得把上面的两个操作连起来
# 我们可以使用session进行请求 -> session可以自动保持cookie
import requests
 
# 会话
session = requests.session()
data = {
    "loginName": "11111111111",
    "password": "11111111"
}

# 1. 登录
url = "https://passport.17k.com/ck/user/login"
session.get(url, data=data)

# 2. 请求书架信息
# 刚才的那个session中是有cookie的
resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")