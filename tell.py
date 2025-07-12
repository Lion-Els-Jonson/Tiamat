import json
import csv

with open('gjk9_chat.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('gjk9_chat.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['時間', '作者', '內容'])

    for item in data:
        time = item.get('time_text') or item.get('timestamp')
        author = item.get('author', {}).get('name') or item.get('author')
        message = item.get('message')
        writer.writerow([time, author, message])