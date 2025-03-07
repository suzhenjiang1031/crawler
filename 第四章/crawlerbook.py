import requests
import asyncio
import aiohttp
import aiofiles
import json
import os

# 确保文件存储在 novel/ 目录
SAVE_DIR = "novel"
os.makedirs(SAVE_DIR, exist_ok=True)

def format_content(text, max_length=40):
    """按 max_length 进行换行，确保阅读体验"""
    return '\n'.join([text[i:i + max_length] for i in range(0, len(text), max_length)])

async def aiodownload(cid, b_id, title):
    """异步下载章节内容"""
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            content = dic.get('data', {}).get('novel', {}).get('content', '')

            if content:
                formatted_content = format_content(content, max_length=40)  # 按 40 字换行
                file_path = os.path.join(SAVE_DIR, f"{title}.txt")
                
                async with aiofiles.open(file_path, mode='w', encoding="utf-8") as f:
                    await f.write(formatted_content)

                print(f"{title} 下载完成")
            else:
                print(f"⚠️ 警告: {title} 章节内容为空")

async def getCatalog(b_id):
    """获取章节目录，并下载内容"""
    url = f'https://dushu.baidu.com/api/pc/getCatalog?data={{"book_id":"{b_id}"}}'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            tasks = []
            for item in dic.get('data', {}).get('novel', {}).get('items', []):
                title = item.get('title', '未知章节')
                cid = item.get('cid', None)
                if cid:
                    tasks.append(aiodownload(cid, b_id, title))
            
            if tasks:
                await asyncio.gather(*tasks)  # 并发执行所有下载任务
            else:
                print("❌ 未找到章节目录")

if __name__ == "__main__":
    b_id = "4306063500"
    asyncio.run(getCatalog(b_id))
