import os
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetForumTopicsRequest

# 🔹 Replace with your credentials
api_id = ""
api_hash = ""
group_id =   # Replace with your correct group ID

client = TelegramClient("session_name", api_id, api_hash)

async def download_media_by_topic():
    async with client:
        group = await client.get_entity(group_id)

        # 🔹 Fetch all topics in the group
        topics = await client(GetForumTopicsRequest(
            channel=group,
            offset_date=0,
            offset_id=0,
            offset_topic=0,
            limit=50
        ))
        topic_dict = {topic.id: topic.title for topic in topics.topics}  # Store topic ID → Name
        print(f"✅ Retrieved Topics: {topic_dict}")

        messages = await client.get_messages(group, limit=1000)  # Fetch latest 1000 messages

        for msg in messages:
            if msg.photo or msg.video or msg.document:
                # 🔹 Default folder is "General"
                topic_name = "General"

                # 🔹 Check if the message is part of a topic/thread
                if msg.reply_to and hasattr(msg.reply_to, "reply_to_msg_id"):
                    reply_msg = await client.get_messages(group, ids=msg.reply_to.reply_to_msg_id)
                    
                    # 🔹 Ensure reply_msg is not a MessageService (system message)
                    if reply_msg and not isinstance(reply_msg, type(None)):  
                        if hasattr(reply_msg, "forum_topic_id"):
                            topic_id = reply_msg.forum_topic_id  # Get topic ID from the replied message
                            topic_name = topic_dict.get(topic_id, "Unknown Topic")  # Get topic name

                # 🔹 Create a folder with the topic name
                save_path = os.path.join("downloaded_media", topic_name)
                os.makedirs(save_path, exist_ok=True)

                # 🔹 Download media inside the topic folder
                file_path = await msg.download_media(file=save_path)
                print(f"📥 Downloaded to {topic_name}: {file_path}")

import asyncio
asyncio.run(download_media_by_topic())
