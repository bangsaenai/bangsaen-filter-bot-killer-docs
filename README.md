# 🛡️ Bangsaen Filter Engine
**Ultra-Low Latency AI Bot & Scraper Firewall built natively for Cloudflare Workers.**

[![Cloudflare Workers](https://img.shields.io/badge/Cloudflare-Workers-F38020?style=flat-square&logo=cloudflare&logoColor=white)](https://workers.cloudflare.com/)
[![C++ WASM](https://img.shields.io/badge/Powered_by-C%2B%2B_WASM-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)](https://webassembly.org/)
[![Latency](https://img.shields.io/badge/Edge_Latency-%3C1ms-brightgreen?style=flat-square)]()
[![Pricing](https://img.shields.io/badge/Pricing-Free_Tier_Available-blue?style=flat-square)]()

**Bangsaen Filter** is a high-performance bot mitigation engine designed for the Cloudflare Edge network. Powered by a custom C++ WebAssembly (WASM) kernel using Hilbert Space Projection algorithms, it detects and blocks malicious AI scrapers, automated bots, and Layer 7 threats in **$O(1)$ time complexity**.

Designed to execute at the Edge before traffic touches your origin infrastructure.

---

## ✨ Key Features

- ⚡ **Minimal Overhead:** Optimized C++ WASM compilation ensures near-instant evaluation at the Cloudflare Edge node.
- 🚀 **Sub-Millisecond Execution:** Evaluates 15-dimensional HTTP observables in sub-milliseconds without slowing down valid requests.
- 🤖 **AI Scraper Defense:** Engineered to mitigate unauthorized AI crawlers, LLM data harvesters, and headless browser automation.
- 🔌 **Seamless Integration:** Easily drops into your existing Cloudflare Worker pipeline.

---

## 🏗️ Architecture

```text
[ Visitor / AI Scraper ] 
          │
          ▼ (Cloudflare Edge)
  ╭──────────────────────────────────────────────╮
  │ 🛡️ Bangsaen Filter (Worker)                  │
  │   ├─ 1. Authenticate API Key (KV)            │
  │   ├─ 2. Extract HTTP Observables             │
  │   └─ 3. Evaluate via C++ WASM Kernel         │
  ╰──────────────────────────────────────────────╯
          │                               │
    [ ALLOWED ]                       [ BLOCKED ]
          │                               │
          ▼                               ▼
 [ Your Origin Server ]         [ HTTP 403 Forbidden ]

```

🚀 Quick Start Guide
1. Claim a Free Developer Key
Get your free 100,000 requests/month developer key via cURL:

Bash 

```
curl -X POST [https://bangsaen-bot-killer.bangsaen-filter.workers.dev/api/claim-free](https://bangsaen-bot-killer.bangsaen-filter.workers.dev/api/claim-free)
```

2. Integrate into Your Cloudflare Worker
Add Bangsaen Filter as a security evaluation step before proxying to your origin:

```
export default {
  async fetch(request: Request, env: any): Promise<Response> {
    // 1. Pass incoming request headers to Bangsaen Edge Engine
    const securityCheck = await fetch("[https://bangsaen-bot-killer.bangsaen-filter.workers.dev/](https://bangsaen-bot-killer.bangsaen-filter.workers.dev/)", {
      method: request.method,
      headers: {
        ...Object.fromEntries(request.headers),
        "x-bangsaen-key": "YOUR_BANGSAEN_API_KEY_HERE"
      }
    });

    // 2. Intercept blocked traffic immediately
    if (securityCheck.status === 403) {
      return securityCheck;
    }

    // 3. Forward legitimate traffic to your origin
    return fetch(request);
  }
};

```

3. Telemetry Headers
Every processed request returns real-time edge performance metrics:

HTTP

```
HTTP/1.1 200 OK
X-Bangsaen-Action: ALLOW
X-Bangsaen-Score: 0.0000
X-Bangsaen-Exec-Time: 0.24ms
```

🧪 Benchmark & Feedback
We actively welcome community stress-testing! If you run load tests or benchmarking against our edge endpoint, please feel free to share your findings in the Issues tab.


## 💰 Pricing

| Plan | Price | Monthly Quota | Features |
| :--- | :--- | :--- | :--- |
| **Developer** | **$0** / mo | **100,000** Reqs | Standard Edge Protection, Community Support |
| **Pro** | **$19** / mo | **1,000,000** Reqs | Dedicated WASM Instance, Custom Rules |
| **Enterprise** | **Custom** | **Custom** | Unlimited Quota, Custom ML Thresholds |

---

## 📊 Status Codes

* `401 Unauthorized` — Missing or invalid `x-bangsaen-key` header.
* `403 Forbidden` — Request flagged as automated threat / malicious scraper.
* `429 Too Many Requests` — Monthly request quota limit reached.

---

<div align="center">

*Built with ❤️ by **BangsaenAI Team***

Get your key at bangsaenai.com 
</div> 

## ⚡ Performance Benchmark: ~1.11ms at the Edge

Most traditional bot filtering solutions evaluate traffic on the application layer, forcing your origin server to spin up PHP processes and burn CPU cycles just to reject bad actors. 

**Bangsaen Filter** executes C++ compiled to WebAssembly directly inside Cloudflare Workers, eliminating malicious traffic in **~1.11ms** before it ever touches your server.

### 📊 Metric Breakdown

| Metric | Bangsaen Filter (C++ WASM) | Traditional PHP / Origin Filter |
| :--- | :--- | :--- |
| **CPU Execution Time** | **~1.11 ms** ⚡ | ~20 ms – 100+ ms |
| **Origin Server CPU Load** | **0%** *(Blocked at Edge)* | High *(Drained by incoming requests)* |
| **Cloudflare Free Quota Used** | **~11%** *(10ms CPU limit)* | N/A |
| **Execution Context** | Edge V8 / WASM Isolation | Host System / Web Server |

---

### 🧪 Want to Break / Stress-Test This Benchmark?

We encourage performance engineers, DevSecOps folks, and WASM enthusiasts to stress-test this engine under real-world conditions.

Feel free to spin up your favorite load-testing tools (`k6`, `wrk`, or `autocannon`) against a protected endpoint:

```bash
# Example load test with wrk (12 threads, 400 connections, 30s)
wrk -t12 -c400 -d30s [https://bangsaen-bot-killer.bangsaen-filter.workers.dev/](https://bangsaen-bot-killer.bangsaen-filter.workers.dev/)

```

Key Metrics to Monitor During Stress Testing:

Cloudflare Worker Metrics: Observe CPU execution time remaining tightly bound around ~1.1ms.

Origin Metrics: Verify that origin CPU load remains flat at 0% during incoming bot floods.

💬 Got an interesting benchmark result, bottleneck finding, or edge-case bypass? Open an Issue or share your flamegraph in Discussions! 

Send us a report at drtanet@bangsaenai.com 

--- 

## 📊 Live Benchmark & Stress Test Results

We ran an aggressive layer-7 bot attack simulation using `autocannon` (400 concurrent connections for 30s) to stress-test the C++ WASM edge engine.

### 📈 Test Execution Log (`autocannon`)

