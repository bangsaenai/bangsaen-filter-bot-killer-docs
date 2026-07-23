import asyncio
import time
import random
import string
from collections import Counter
import aiohttp

TARGET_URL = "https://bangsaen-bot-killer.bangsaen-filter.workers.dev/"
TOTAL_REQUESTS = 10000
CONCURRENCY = 300

# คลัง User-Agent แบบสุ่ม (มีทั้ง Browser จริง และ Bot แอบเนียน)
USER_AGENTS = [
    # Real Browsers
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/126.0.6478.35 Mobile/15E148 Safari/604.1",
    # Stealth Scrapers / AI Bots
    "Mozilla/5.0 (compatible; GPTBot/1.0; +https://openai.com/gptbot)",
    "Mozilla/5.0 (compatible; ClaudeBot/1.0; +https://anthropic.com)",
    "Bytespider",
    "Go-http-client/1.1",
]

def generate_random_headers():
    ua = random.choice(USER_AGENTS)
    headers = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": random.choice(["th-TH,th;q=0.9,en-US;q=0.8", "en-US,en;q=0.5"]),
        "Cache-Control": random.choice(["no-cache", "max-age=0"]),
    }
    # สุ่มใส่ Client Hints ปลอม
    if "Chrome" in ua:
        headers["Sec-Ch-Ua"] = '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"'
        headers["Sec-Ch-Ua-Mobile"] = "?0"
        headers["Sec-Ch-Ua-Platform"] = '"Windows"'
    return headers

async def fetch(session, semaphore, stats, latencies):
    async with semaphore:
        headers = generate_random_headers()
        # ทำ Cache-Busting สุ่ม URL ให้ไม่ซ้ำกัน
        random_query = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        url = f"{TARGET_URL}?test_id={random_query}"
        
        start_time = time.perf_counter()
        try:
            # สุ่ม Method ระหว่าง GET และ POST
            method = random.choice(["GET", "POST"])
            payload = {"data": random_query} if method == "POST" else None

            async with session.request(method, url, headers=headers, json=payload, timeout=10) as response:
                elapsed = (time.perf_counter() - start_time) * 1000
                latencies.append(elapsed)
                stats[response.status] += 1
        except asyncio.TimeoutError:
            stats["Timeout"] += 1
        except Exception:
            stats["Client_Error"] += 1

async def main():
    print(f"🔥 Starting ADVANCED Evasion Stress Test...")
    print(f"🎯 Target: {TARGET_URL}")
    print(f"⚙️ {TOTAL_REQUESTS} requests | {CONCURRENCY} concurrency | Randomized Headers & Methods\n")

    stats = Counter()
    latencies = []
    semaphore = asyncio.Semaphore(CONCURRENCY)
    connector = aiohttp.TCPConnector(limit=CONCURRENCY, ssl=False)

    start_total_time = time.perf_counter()

    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch(session, semaphore, stats, latencies) for _ in range(TOTAL_REQUESTS)]
        await asyncio.gather(*tasks)

    total_duration = time.perf_counter() - start_total_time
    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    rps = TOTAL_REQUESTS / total_duration

    print("=" * 60)
    print("📊 ADVANCED TEST BENCHMARK REPORT")
    print("=" * 60)
    print(f"⏱️ Total Time Elapsed  : {total_duration:.2f} seconds")
    print(f"🔥 Throughput          : {rps:.2f} Req/sec")
    print(f"⚡ Avg Latency         : {avg_latency:.2f} ms")
    print("-" * 60)
    print("🛡️ Breakdown Status Code:")
    for code, count in stats.items():
        percentage = (count / TOTAL_REQUESTS) * 100
        print(f"  Status [{code}] : {count:,} ({percentage:.2f}%)")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())