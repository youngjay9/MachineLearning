import time
import asyncio

async def fetch_data(name, seconds):
    print(f"{name}: 送出請求")

    await asyncio.sleep(seconds)

    print(f"{name}: 收到回應")

    return f"{name}: 的資料"



start = time.perf_counter()

a = fetch_data("API A", 2)

b = fetch_data("API B", 3)

print(f"結果: {[a,b]}")

print(f"總耗時: {time.perf_counter() - start:.1f} 秒")