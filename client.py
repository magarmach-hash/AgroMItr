import os
import warnings
import logging
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# warnings.filterwarnings("ignore")
# logging.getLogger().setLevel(logging.WARNING)
# logging.getLogger("langchain").setLevel(logging.WARNING)
# logging.getLogger("langgraph").setLevel(logging.WARNING)

load_dotenv()

MAX_HISTORY = 5
chat_history = {}  # per-user history
agent = None  # global agent

# ---------------- Telegram Handlers ---------------- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Mewo Meow")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global chat_history, agent
    user_id = update.message.from_user.id
    user_input = update.message.text

    if user_id not in chat_history:               #chat history
        chat_history[user_id] = []

    chat_history[user_id].append({"role": "user", "content": user_input})                 #new user

    # trim history
    if len(chat_history[user_id]) > MAX_HISTORY:
        chat_history[user_id] = chat_history[user_id][-MAX_HISTORY:]

    try:
        response = await agent.ainvoke({"messages": chat_history[user_id]})
        agent_msg = response["messages"][-1].content

        #adding new chat to the history
        chat_history[user_id].append({"role": "assistant", "content": agent_msg})

        await update.message.reply_text(agent_msg)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

async def init_agent():
    global agent
    client = MultiServerMCPClient(
        {
            "mandi-price-server": {
                "command": "python",
                "args": ["mandi_server.py"],
                "transport": "stdio"
            },
            "translation-server":{
                "command": "python",
                "args": ["TranslationServer.py"],
                "transport": "stdio"
            },
             "rag-server": {
                "command": "python",
                "args": ["ragServer.py"],
                "transport": "stdio"
            },
            "Weather_Server": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            }
        }
    )
    tools = await client.get_tools()

    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    agent = create_react_agent(model, tools)


def main():
    import asyncio

    asyncio.run(init_agent())

    # Setup Telegram bot
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_API")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()  # not asyncio.run() ?

if __name__ == "__main__":
    main()
