import requests

#Текст сообщения
payload = {
    'content': "16:05"
}

#токен дискорда
header = {
    "authorization": ""
}

#ОТправка простого сообщения
# r = requests.post("https://discord.com/api/v9/channels/972793017012469790/messages", data = payload, headers=header)


#Получить список сообщений
r = requests.get("https://discord.com/api/v9/channels/972793017012469790/messages?limit=50", headers=header)
print(r.text)
