from telethon.sync import TelegramClient
import csv
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

key = '27167798'
hash_key = '4143366cf82b6eb9e7ec7f25a50dc205'
phone = '+79257096300'

client = TelegramClient(phone, key, hash_key)
client.start()
chats = []

result = client(GetHistoryRequest(
    offset_date=None,
    offset_id=0,
    limit=200,
    hash=0
))
chats.extend(result.chats)
target_group = chats[13]
for chat in chats:
    print(chat.title)

all_messages = []
offset_id = 0
limit = 100
total_messages = 0
total_count_limit = 0

history = client(GetHistoryRequest(
   peer="owl_yashina",
   offset_id=offset_id,
   offset_date=None,
   add_offset=0,
   limit=limit,
   max_id=0,
   min_id=0,
   hash=0
))


print("Сохраняем данные в файл...")  # Cообщение для пользователя о том, что начался парсинг сообщений.

with open("chats.csv", "w", encoding="UTF-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(["message"])
    for message in all_messages:
        writer.writerow([message])
print("Парсинг сообщений группы успешно выполнен.")