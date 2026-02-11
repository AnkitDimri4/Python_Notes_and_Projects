import requests
from bs4 import BeautifulSoup

class Pricetracer:
    def __init__(self, url):
        self.url = url 
        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/*******2"}
        self.response = requests.get(url = self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")
    
    def product_title(self):
        title = self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not FOUND"
    def product_price(self):
        # pass
        price = self.soup.find("span",{"class":"a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag not FOUND"

device = Pricetracer(url="https://www.amazon.in/Samsung-Burgundy-Storage-Additional-Exchange/dp/B09SH7FDKT/ref=sr_1_1_sspa?keywords=samsung%2Bgalaxy%2Bs22%2Bultra&qid=1673959099&sprefix=samsung%2Bgal%2Caps%2C440&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

print(device.product_title())
print(device.product_price())
