import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetForumTopicsRequest

# 🔹 Replace with your credentials
api_id = ""
api_hash = ""
group_id =   # Replace with your correct group ID

client = TelegramClient("session_name", api_id, api_hash)

async def fetch_topics():
    async with client:
        group = await client.get_entity(group_id)

        # 🔹 Fetch topics with required parameters
        topics = await client(GetForumTopicsRequest(
            channel=group,
            offset_date=0,  # No date offset
            offset_id=0,  # Start from the first topic
            offset_topic=0,  # Start from the first topic
            limit=50  # Adjust the limit as needed
        ))

        for topic in topics.topics:
            print(f"🔹 Topic ID: {topic.id} | Topic Name: {topic.title}")

import asyncio
asyncio.run(fetch_topics())
