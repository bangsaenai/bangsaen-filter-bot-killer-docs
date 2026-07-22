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
  │ 🛡️ Bangsaen Filter (Worker)                │
  │   ├─ 1. Authenticate API Key (KV)            │
  │   ├─ 2. Extract HTTP Observables             │
  │   └─ 3. Evaluate via C++ WASM Kernel         │
  ╰──────────────────────────────────────────────╯
          │                             │
    [ ALLOWED ]                     [ BLOCKED ]
          │                             │
          ▼                             ▼
 [ Your Origin Server ]       [ HTTP 403 Forbidden ]
```
🚀 Quick Start Guide
1. Get your API Key
Claim your free 100,000 requests/month API Key by registering at Bangsaenai.com.

2. Integration
Once you install the Bangsaen Integration via the Cloudflare Marketplace, you can pass your API key via HTTP Headers to activate the protection.

cURL Example:
```
curl -i -H "x-bangsaen-key: your-api-key-here" [https://your-domain.com/](https://your-domain.com/)
```

3. Review the Security Headers
For every request processed, Bangsaen Filter injects security headers into the response so you can monitor its performance in real-time:

HTTP
```
X-Bangsaen-Action: ALLOW
X-Bangsaen-Score: 0.0000
X-Bangsaen-Exec-Time: 0.000ms
```


## 💰 Pricing

We believe in accessible security for everyone. 

| Plan | Price | Monthly Quota | Features |
| :--- | :--- | :--- | :--- |
| **Developer (Free)** | $0 / mo | 100,000 Reqs | Standard Edge Protection |
| **Pro** | $19 / mo | 5,000,000 Reqs | Priority WASM Instance, Custom Thresholds |
| **Enterprise** | Contact Us | Unlimited | Dedicated Account Manager, Custom ML Training |

---

## 📊 Error Codes & Troubleshooting

* `401 Unauthorized`: Missing `x-bangsaen-key` header.
* `403 Forbidden` (JSON Payload): Traffic identified as a malicious bot and blocked by the engine.
* `429 Too Many Requests`: Your monthly free tier quota has been exceeded.

*Built with ❤️ by BangsaenAI Team.*
