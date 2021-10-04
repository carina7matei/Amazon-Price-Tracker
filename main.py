from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
my_email="USER'S EMAIL"
my_pass="USER'S EMAIL PASSWORD"
email_to_receive_the_message=""
URL=input("Enter the link of a product(from amazon) you are interested in: ")
# URL="https://www.amazon.com/BT21-Figure-Wireless-Keyboard-Royche/dp/B07LGHSJ3C/ref=psdc_12879431_t3_B082RCJR88"
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9",

}
response=requests.get(url=URL,headers=header)
webpage=response.text
soup=BeautifulSoup(webpage,"lxml")
price=float(soup.find(name="span",id="priceblock_ourprice").getText()[1:])
# (price)
desired_price=int(input("Enter the price you would like the chosen product to have: "))
if price<=desired_price:
    message=f"You should consider buying this!!! {URL} RJ KEYBOARD at the price of ${price}"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        connection.sendmail(from_addr=my_email,
        to_addrs="carinavaleriam@gmail.com",msg=f"Subject:Keyboard\n\n{message}")
else:
    message=f"The product you are looking for ({URL}) has a higher price than the one you would like to have"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        connection.sendmail(from_addr=my_email,
        to_addrs=email_to_receive_the_message,msg=f"Subject:I'm Sorry:(\n\n{message}")


