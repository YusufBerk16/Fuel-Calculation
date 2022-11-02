import requests
from bs4 import BeautifulSoup
test="21.53 TL/LT "
print(test.strip(" TL/LT "))
v = int(input("Benzin İçin 1, Dizel İçin 2, Lpg için 3: "))
v1 = int(input("Aracınızın Güncel Deposunu Giriniz (LİTRE): "))
v2 = int(input("Kat Edilen Kilometreyi Giriniz: "))

SELECTOR = "#fuelPricesTableDesktop > tbody > tr:nth-child(1) > td:nth-child(1)"
SELECTOR1 = "#fuelPricesTableDesktop > tbody > tr:nth-child(1) > td:nth-child(2)"
SELECTOR2 = "#fuelPricesTableDesktop > tbody > tr:nth-child(1) > td:nth-child(3)"
SELECTOR3 = "#fuelPricesTableDesktop > tbody > tr:nth-child(1) > td:nth-child(4)"
SELECTOR4 = "#fuelPricesTableDesktop > tbody > tr:nth-child(1) > td:nth-child(5)"

URL = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari/bursa-akaryakit-fiyatlari"


html = requests.get(
    URL,
    headers={
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
    }
).text
soup = BeautifulSoup(html, "html.parser")
sehir = soup.select_one(SELECTOR).text
vmaxkursunsuz95 = soup.select_one(SELECTOR1).get_text("")
vmaxdiesel = soup.select_one(SELECTOR2).text
vprodiesel = soup.select_one(SELECTOR3).text
lpg = soup.select_one(SELECTOR4).text
vtop=v1/v2*100

if(v==1):
    print("100km de",float(vmaxkursunsuz95[:5])*vtop,"TL",vtop,"LT yakar.")
elif(v==2):
    print("100km de",float(vmaxdiesel[:5])*vtop,"TL",vtop,"LT yakar.")
elif(v==3):
    print("100km de",float(lpg[:5])*vtop,"TL",vtop,"LT yakar.")
