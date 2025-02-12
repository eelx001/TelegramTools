from telethon import TelegramClient

# 🔹 Replace with your credentials
api_id =  ""
api_hash = ""
phone_number = ""  # Include country code

client = TelegramClient("session_name", api_id, api_hash)

async def login():
    await client.start(phone_number)
    print("✅ Login successful! Session saved.")

with client:
    client.loop.run_until_complete(login())
