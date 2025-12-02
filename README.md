# 🌾 AgroMitr — AI-Powered Agriculture Assistant

AgroMitr is an **AI-driven multi-agent agriculture assistant** built using the **Model Context Protocol (MCP)**.  
It uses **Telegram as the frontend** and a **modular backend of AI-powered tool servers** to provide real-time, actionable agricultural insights to farmers.

---

## 🚀 Features

### **1. Telegram-Based AI Assistant**
- Easy-to-use conversational interface  
- Farmers interact via a lightweight Telegram bot  
- All intelligence and processing handled in backend servers  

### **2. Multi-Server MCP Ecosystem**
AgroMitr uses multiple specialized tool servers, designed for modularity and scalability:

| Server | Purpose |
|--------|---------|
| **Weather Server** | Fetch accurate weather forecasts for specific regions |
| **Mandi Price Server** | Real-time crop prices from official Indian government APIs |
| **RAG Server** | Retrieves answers from agricultural manuals, subsidies, and govt documents |
| **Translation Server** | Translates messages into local Indian languages |
| **BS4 Server** | Scrapes static websites using BeautifulSoup |
| **Playwright Server** | Handles dynamic website scraping and automation |
| **Client Controller** | Central orchestrator connecting the bot, servers, and GPT reasoning |

---

## 🧠 System Architecture

User → Telegram Bot → MCP Python Client → Tool Servers → GPT Model → Response

### Backend Flow:
1. User sends a query via Telegram  
2. Python client interprets using GPT reasoning  
3. Calls relevant tool servers (API, scraping, RAG, translation, etc.)  
4. Aggregates data using GPT  
5. Sends structured, natural-language output back to Telegram  

---

## 🌐 Capabilities

### ✔ Weather forecasting  
### ✔ Government mandi prices (real-time)  
### ✔ Subsidy / government manual RAG search  
### ✔ Local language translation  
### ✔ Dynamic web automation (Playwright)  
### ✔ Static scraping (BeautifulSoup)  
### ✔ Unified conversation flow (MCP Client)

---

## 🛠 Tech Stack

- **Python** (core logic + MCP client)  
- **Telegram Bot API**  
- **MCP Server Architecture**  
- **OpenAI GPT models**  
- **BeautifulSoup**  
- **Playwright**  
- **FastAPI** (for servers)  
- **Gov APIs for crop prices**  
- **RAG with embeddings for documents**  

---

## 📦 Project Structure (High-Level)

agromitr/
│── client/ # Main MCP client controlling all tools
│── servers/
│ ├── weather_server/
│ ├── mandi_price_server/
│ ├── rag_server/
│ ├── translation_server/
│ ├── bs4_server/
│ └── playwright_server/
│── telegram_bot/
│── docs/ # Government manuals + processed embeddings
│── README.md

---

## 🎯 Goal of the Project

To build a **farmer-friendly AI system** that:  
- removes the need to navigate complex government portals  
- provides instant agricultural intelligence  
- works entirely through a simple Telegram chat  
- scales modularly using multiple AI-enabled MCP servers  

---

## 🧑‍💻 Developer

**Naveen**  
Cybersecurity & GenAI enthusiast

