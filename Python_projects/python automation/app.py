from credentials import mobile_number # pip install phonenumbers
import requests
import schedule
import time 

def send_message():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '7668455126',
    'message': 'Hello Ritik, I hope you got the text',
    'key': 'textbelt',
    })  
    print(resp.json())
# schedule.every().day.at('06:00').do(send_message)
schedule.every(10).second.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
