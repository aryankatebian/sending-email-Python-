import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.co.uk/Boosted-Mini-X-Skateboard/dp/B07J9PJYBL?pf_rd_p=777c132f-cd3a-4baa-b999-4c401cbe5903&pd_rd_wg=kKBNK&pf_rd_r=JAX0AVMN4WMG0M2KWEMZ&ref_=pd_gw_unk&pd_rd_w=ENTxV&pd_rd_r=fec0d507-e3fe-46fd-a202-5f0e6f03065a"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:7])

    if(converted_price < 1000.00):
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587 )
    server.ehlo() # Can be omitted
    server.starttls() # Secure the connection
    server.ehlo() # Can be omitted
    server.login("aryan.katebian@gmail.com", "mayqmjhhfzovcfou")
    
    subject = " price is under 1000.00"
    body = "check the link  :     https://www.amazon.co.uk/Boosted-Mini-X-Skateboard/dp/B07J9PJYBL?pf_rd_p=777c132f-cd3a-4baa-b999-4c401cbe5903&pd_rd_wg=kKBNK&pf_rd_r=JAX0AVMN4WMG0M2KWEMZ&ref_=pd_gw_unk&pd_rd_w=ENTxV&pd_rd_r=fec0d507-e3fe-46fd-a202-5f0e6f03065a "

    msg = f"subject: {subject}\n\n{body}"
    server.sendmail("aryan.katebian@gmail.com", "aryan_simpskin@yahoo.com", msg)
    print('email has been sent')

    server.quit()


while(True):
    check_price()
    time.sleep(1000000)