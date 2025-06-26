from openai import OpenAI as ai
from dotenv import get_key
import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

##API_KEY=get_key(".env","API_KEY")
client=ai(api_key="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",base_url="https://openrouter.ai/api/v1")

bot=Bot(token="8162812235:AAFXyPIEzixv7x6SxWA2QTg5Df7X6fv0e9I",default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp=Dispatcher()
@dp.message(Command("start"))
async def welcome_message(message:Message):
    username=message.from_user.full_name
    await message.answer(f"Hello {username}! 👋\nWelcome to Deepseek Chatbot")
@dp.message()
async def handle_message(message:Message):
    user_text=message.text
    response=client.chat.completions.create(model="deepseek/deepseek-r1-0528",max_tokens=1000,messages=[{"role":"system","content":"you are powerful hacker"},{"role":"user","content":user_text}])
    await message.answer(f"<b>Deeepseek:\n</b><code>{response.choices[0].message.content}</code>")
async def main():
    print("Bot is running....")
    await dp.start_polling(bot)
if __name__=="__main__":
    asyncio.run(main())
   

