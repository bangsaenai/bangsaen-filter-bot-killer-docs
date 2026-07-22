# 🛡️ Bangsaen Filter Engine
**The $O(1)$ Ultra-Low Latency AI Bot & Scraper Firewall built natively for Cloudflare Workers.**

[![Cloudflare Workers](https://img.shields.io/badge/Cloudflare-Workers-F38020?style=flat-square&logo=cloudflare&logoColor=white)](https://workers.cloudflare.com/)
[![C++ WASM](https://img.shields.io/badge/Powered_by-C++_WASM-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)]()
[![Latency](https://img.shields.io/badge/Edge_Latency-0.000ms-brightgreen?style=flat-square)]()
[![Pricing](https://img.shields.io/badge/Pricing-Free_Tier_Available-blue?style=flat-square)]()

**Bangsaen Filter** is a next-generation bot mitigation middleware designed exclusively for the Cloudflare Edge network. Powered by a custom C++ WebAssembly (WASM) kernel using Hilbert Space Projection algorithms, it detects and blocks malicious AI scrapers, automated bots, and Layer 7 threats in **true $O(1)$ time complexity**.

No external API calls. No DNS routing delays. Just pure, bare-metal performance at the Edge.

---

## ✨ Why Bangsaen Filter?

- ⚡ **Zero Network Overhead:** Unlike traditional security vendors that route your traffic to external data centers, Bangsaen runs directly on your Cloudflare Edge node.
- 🚀 **`0.000ms` Execution Time:** Our C++ WASM kernel evaluates 15-dimensional HTTP observables in sub-milliseconds. Your legitimate users won't feel a thing.
- 🤖 **Advanced AI Scraper Defense:** Specifically trained to block modern AI crawlers, LLM data scrapers, and headless browser automation.
- 🔌 **Plug & Play Middleware:** Deploys as a Reverse Proxy Worker in 1 click. No need to modify your origin server's code.

---

## 🏗️ Architecture / How it Works

```text
[ Visitor / AI Scraper ] 
          │
          ▼ (Cloudflare Edge)
  ╭──────────────────────────────────────────────╮
  │ 🛡️ Bangsaen Filter (Worker)                 │
  │   ├─ 1. Authenticate API Key (KV)            │
  │   ├─ 2. Extract HTTP Observables             │
  │   └─ 3. Evaluate via C++ WASM Kernel         │
  ╰──────────────────────────────────────────────╯
          │                              │
    [ ALLOWED ]                      [ BLOCKED ]
          │                              │
          ▼                              ▼
 [ Your Origin Server ]        [ HTTP 403 Forbidden ]

 ```
🚀 Quick Start Guide
1. Claim Instant Free API Key
Get your free 100,000 requests/month developer key instantly via cURL or at www.bangsaenai.com:

```
curl -X POST [https://bangsaen-bot-killer.bangsaen-filter.workers.dev/api/claim-free](https://bangsaen-bot-killer.bangsaen-filter.workers.dev/api/claim-free)
```

2. Integrate into Your Cloudflare Worker
Add Bangsaen Filter as a lightweight security middleware before forwarding requests to your origin:

TypeScript
```
export default {
  async fetch(request: Request, env: any): Promise<Response> {
    // 1. Pass incoming request to Bangsaen Edge Engine
    const securityCheck = await fetch("[https://bangsaen-bot-killer.bangsaen-filter.workers.dev/](https://bangsaen-bot-killer.bangsaen-filter.workers.dev/)", {
      method: request.method,
      headers: {
        ...Object.fromEntries(request.headers),
        "x-bangsaen-key": "YOUR_BANGSAEN_API_KEY_HERE"
      }
    });

    // 2. Block malicious bot traffic immediately
    if (securityCheck.status === 403) {
      return securityCheck;
    }

    // 3. Forward legitimate traffic to your origin
    return fetch(request);
  }
};

```
3. Review Real-time Security Headers
Every request processed by Bangsaen Filter returns transparent edge telemetry headers:


```
HTTP/1.1 200 OK
X-Bangsaen-Action: ALLOW
X-Bangsaen-Score: 0.0000
X-Bangsaen-Exec-Time: 0.000ms
```

ง## 💰 Pricing

We believe in accessible security for everyone.

| Plan | Price | Monthly Quota | Features |
| :--- | :--- | :--- | :--- |
| **Developer (Free)** | **$0** / mo | **100,000** Reqs | Standard Edge Protection, Community Support |
| **Pro** | **$19** / mo | **1,000,000** Reqs | Priority WASM Instance, Auto Block Enforce |
| **Enterprise** | **Contact Us** | **Custom** | Unlimited Quota, Custom ML Thresholds |

---

## 📊 Error Codes & Troubleshooting

* `401 Unauthorized` — Missing `x-bangsaen-key` header in request.
* `403 Forbidden` — Traffic identified as a malicious bot/scraper and intercepted by the C++ engine.
* `429 Too Many Requests` — Your monthly request quota has been exceeded. Please upgrade your plan.

---

<div align="center">

*Built with ❤️ by **BangsaenAI Team***

</div>

