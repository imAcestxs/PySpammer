import time, pyautogui, requests
from turtle import delay
from discord import Webhook, RequestsWebhookAdapter

proxies = {
    'https': 'https://52.183.8.129:3128',
    'https': 'https://190.26.201.194:8080',
    'https': 'https://140.227.80.237:3180',
    'https': 'https://195.201.111.241:3128',
    'https': 'https://157.100.12.138:999',
    'https': 'https://115.96.208.124:8080'
}
print("""
 /$$$$$$$            /$$$$$$                                                                    
| $$__  $$          /$$__  $$                                                                   
| $$  \ $$/$$   /$$| $$  \__/  /$$$$$$  /$$$$$$  /$$$$$$/$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$/ $$  | $$|  $$$$$$  /$$__  $$|____  $$| $$_  $$_  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$
| $$____/| $$  | $$ \____  $$| $$  \ $$ /$$$$$$$| $$ \ $$ \ $$| $$ \ $$ \ $$| $$$$$$$$| $$  \__/
| $$     | $$  | $$ /$$  \ $$| $$  | $$/$$__  $$| $$ | $$ | $$| $$ | $$ | $$| $$_____/| $$      
| $$     |  $$$$$$$|  $$$$$$/| $$$$$$$/  $$$$$$$| $$ | $$ | $$| $$ | $$ | $$|  $$$$$$$| $$      
|__/      \____  $$ \______/ | $$____/ \_______/|__/ |__/ |__/|__/ |__/ |__/ \_______/|__/      
          /$$  | $$          | $$                                                               
         |  $$$$$$/          | $$                                                               
          \______/           |__/                                                               
    """)
webHooker = input("Webhook : ")
spamTime = input("Amount : ")
talk = input("Say : ")
webhook = Webhook.from_url(webHooker, adapter=RequestsWebhookAdapter())

while True:
    webhook.send(talk)
    print("Sent spam\n")