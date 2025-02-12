from telethon import TelegramClient
import os

client = TelegramClient("session_name", "", "")

async def download_media():
    async with client:
        try:
            group = await client.get_entity("HERE")  # Replace with your group ID
            messages = await client.get_messages(group, limit=10)

            save_path = "downloaded_media"
            os.makedirs(save_path, exist_ok=True)

            for msg in messages:
                if msg.photo or msg.video or msg.document:
                    file_path = await msg.download_media(file=save_path)
                    print(f"📥 Downloaded: {file_path}")
                else:
                    print(f"📝 Skipped (Not Media): {msg.text}")
        except Exception as e:
            print(f"❌ Error: {e}")

import asyncio
asyncio.run(download_media())



# from telethon import TelegramClient

# client = TelegramClient("session_name", "21887187", "de00960994f3ce6be55bb240fde02c21")

# async def check_access():
#     async with client:
#         try:
#             chat = await client.get_entity(-1002349465837)  # Replace with the group ID
#             print(f"✅ You have access to: {chat.title}")
#         except Exception as e:
#             print(f"❌ Error: {e}")

# import asyncio
# asyncio.run(check_access())
# This script checks if you have access to a specific group by its ID. Replace YOUR_API_ID with your API ID and YOUR_API_HASH with your API hash. Replace -1002349465837 with the group ID you want to check. Run the script to see if you have access to the group.    