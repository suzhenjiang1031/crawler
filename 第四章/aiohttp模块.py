# requests.get() 同步的代码 -> 异步操作
import aiohttp
import asyncio

urls = [
    "https://img36.tp3001.com/wp-content/uploads/ti/fengjing/266.jpg",
    "https://img36.tp3001.com/wp-content/uploads/ti/fengjing/257.jpg",
    "https://img36.tp3001.com/wp-content/uploads/ti/fengjing/1097.jpg"
]

async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # resp.content.read() # == >resp.content
            # 请求回来了，写入文件
            with open(name, mode='wb') as f:
                f.write(await resp.content.read()) # 读取内容是异步的，需要await挂起

    print(name, "搞定")

    # s = aiohttp.ClientSession() <==> requests
    # requests.get() .post()
    # s.get() .post()
    # 发送请求
    # 得到图片内容
    # 保存到文件

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
