import os
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetForumTopicsRequest, CreateForumTopicRequest

api_id = ""
api_hash = ""
group_id =   #GROUP ID
topics_file = "topicName.txt"

client = TelegramClient("session_name", api_id, api_hash)

async def create_topics_from_file():
    async with client:
        group = await client.get_entity(group_id)

        # 🔹 Fetch existing topics
        topics = await client(GetForumTopicsRequest(
            channel=group,
            offset_date=0,
            offset_id=0,
            offset_topic=0,
            limit=100
        ))

        # 🔹 Create a set of existing topic names
        existing_topics = {topic.title.lower() for topic in topics.topics}
        print(f"✅ Existing Topics: {existing_topics}")

        # 🔹 Read topic names from `topics.txt`
        if not os.path.exists(topics_file):
            print(f"❌ Error: {topics_file} not found. Create this file with topic names.")
            return
        
        with open(topics_file, "r", encoding="utf-8") as f:
            new_topics = [line.strip() for line in f if line.strip()]

        # 🔹 Create topics that don’t exist yet
        for topic_name in new_topics:
            if topic_name.lower() in existing_topics:
                print(f"⚠️ Topic '{topic_name}' already exists. Skipping.")
            else:
                try:
                    await client(CreateForumTopicRequest(channel=group, title=topic_name))
                    print(f"✅ Created new topic: {topic_name}")
                except Exception as e:
                    print(f"❌ Failed to create topic '{topic_name}': {e}")

if __name__ == "__main__":
    print("🚀 Creating topics from the text file...")
    asyncio.run(create_topics_from_file())
    print("\n🎉 Done!")
