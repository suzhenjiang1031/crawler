# 原理，通过第三方的一个机器去发送请求
import requests

# 140.210.196.193:6969
proxies = {
    "https":"https://140.210.196.193:6969"
}

resp = requests.get("http://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
