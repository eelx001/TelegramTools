from telethon import TelegramClient

# Use the saved session
client = TelegramClient("session_name", "", "")

async def list_groups():
    async with client:
        dialogs = await client.get_dialogs()
        for chat in dialogs:
            if chat.is_group:
                print(f"✅ Group Name: {chat.name} | 📌 Group ID: {chat.id}")

import asyncio
asyncio.run(list_groups())
