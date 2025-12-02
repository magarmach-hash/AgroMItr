# 🌾 AgroMitr — AI-Powered Agriculture Assistant

AgroMitr is an **AI-driven, multi-agent agriculture assistant** built using the **Model Context Protocol (MCP)**.  
It uses **Telegram as the frontend** and a **modular backend of AI-powered microservices** to deliver real-time agricultural insights to farmers.

---

## 🚀 Features

### **1. Telegram-Based AI Assistant**
- Simple conversational interface  
- Lightweight for farmers  
- All processing done in backend servers  

### **2. Multi-Server MCP Ecosystem**
AgroMitr uses modular tool servers:

| Server | Purpose |
|--------|---------|
| **Weather** | Accurate regional weather data |
| **Mandi Prices** | Real-time govt crop prices |
| **RAG** | Search govt manuals, subsidies & PDFs |
| **Translation** | Multi-language support |
| **BS4 Scraper** | Static website scraping |
| **Playwright Scraper** | Dynamic site automation |
| **Client Controller** | Orchestrates all servers + GPT |

---

## 🧠 System Architecture
**User → Telegram Bot → MCP Client → Tool Servers → GPT → Response**

Flow:
1. User sends query  
2. GPT-powered client routes to correct server  
3. Weather, mandi, RAG, scraping or translation servers respond  
4. GPT composes the final answer  
5. Telegram returns it to the user  

---

## 🌐 Capabilities (Short)

- ✔ Weather info  
- ✔ Crop price lookup  
- ✔ Scheme/manual search (RAG)  
- ✔ Language translation  
- ✔ Static + dynamic scraping  
- ✔ Unified AI reasoning  

---

## 🛠 Tech Stack
- **Python**, **FastAPI**  
- **Telegram Bot API**  
- **MCP client-server architecture**  
- **BeautifulSoup**, **Playwright**  
- **OpenAI GPT models**  
- **Gov APIs**  
- **Embeddings + RAG**  

---

## 📦 Project Structure

agromitr/
│── client/                       # MCP client controller  
│── servers/  
│   ├── weather/  
│   ├── mandi/  
│   ├── rag/  
│   ├── translation/  
│   ├── bs4_scraper/  
│   └── playwright_scraper/  
│── telegram_bot/  
│── docs/                         # Manuals + embeddings  
│── README.md  

---

## 🎯 Project Goal
To build a **farmer-friendly AI platform** that provides essential agricultural insights instantly,   
without forcing users to navigate complex government portals — via a simple Telegram chat backed by modular AI servers.

---

## 🧑‍💻 Developer  
**Naveen**  
Cybersecurity & GenAI Enthusiast
