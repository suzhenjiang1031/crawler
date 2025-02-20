import requests
query = input("请输入你要搜索的内容:")

url = f'https://www.bing.com/search?pglt=929&q={query}'

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"    
} 

resp = requests.get(url, headers = headers)

print(resp)
print(resp.text) #拿到页面源代码