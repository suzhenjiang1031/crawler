import asyncio
import time

async def func1():
    print("1")
    await asyncio.sleep(3)
    print("2")

async def func2():
    print("3")
    await asyncio.sleep(2)
    print("4")

async def func3():
    print("5")
    await asyncio.sleep(1)
    print("6")

async def main():
    t1 = time.time()

    tasks = [
        asyncio.create_task(func1()),  
        asyncio.create_task(func2()),  
        asyncio.create_task(func3())   
    ]
    await asyncio.wait(tasks)  # 等待所有任务完成

    t2 = time.time()
    print(f"总耗时: {t2 - t1:.2f} 秒")

if __name__ == '__main__':
    asyncio.run(main())  # 在 `main()` 内部管理事件循环
