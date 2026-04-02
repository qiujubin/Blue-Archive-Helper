import httpx
import asyncio
import time

async def get_game_data():
    # 1. 目标 URL
    url = "https://www.gamekee.com/v1/activity/page-list"
    
    # 2. 参数和请求头 (保持不变)
    params = {
        "importance": 0,
        "sort": -1,
        "keyword": "",
        "limit": 999,
        "page_no": 1,
        "serverId": 16,
        "status": 0
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.gamekee.com/ba/huodong/16",
        "Game-Alias": "ba"
    }

    # 3. 使用 async with 创建异步客户端
    # 这一步相当于初始化连接池，可以复用连接，速度更快
    async with httpx.AsyncClient() as client:
        try:
            # 4. 发送请求
            # 注意这里要加 await，意思是“等待这个网络请求完成”
            response = await client.get(url, params=params, headers=headers, timeout=10.0)
            
            if response.status_code == 200:
                data = response.json()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"{timestamp} 异步请求成功")
                print("-" * 30)
                
                if data.get("code") == 0 and "data" in data:
                    # 打印前 10 个活动
                    for i, item in enumerate(data["data"][:20]):
                        print(f"{i+1}. {item.get('title')}, {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item.get('begin_at')))}, {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item.get('end_at')))}, {item.get('activity_kind_id')}, {item.get('activity_kind_name')}, {item.get('activity_state')}")
                else:
                    print(f"业务错误: {data}")
            else:
                print(f"请求失败: {response.status_code}") 
                print(response.text)
                
        except Exception as e:
            print(f"发生异常: {type(e).__name__}: {e!r}")

# 5. 运行异步函数
# 异步代码不能直接运行，需要由事件循环来驱动
if __name__ == "__main__":
    asyncio.run(get_game_data())
