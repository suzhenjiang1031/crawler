import requests

url = "https://movie.douban.com/j/chart/top_list"

#重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36" 
}

resp = requests.get(url=url, params=param, headers=headers)
print(resp.json())
resp.close() # 关掉resp
