import requests
import bs4
import urllib
import json

def bse():
    search = "https://www.financialexpress.com/market/stock-market/bse-top-gainers/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    result = requests.get(search, headers=headers,proxies=urllib.request.getproxies())
    soup = bs4.BeautifulSoup(result.text,'lxml')
    text = soup.select('tr td')
    arr = []
    name_arr = []
    close_price = []
    prev_close_price = []
    change_percent = []
    change_rs = []
    volume = []
    for txt in text:
        arr.append(txt.getText())

    for i in range(9,99,6):
        name_arr.append(arr[i])
    
    for i in range(10,99,6):
        close_price.append(arr[i])

    for i in range(11,99,6):
        prev_close_price.append(arr[i])

    for i in range(12,99,6):
        change_percent.append(arr[i])

    for i in range(13,99,6):
        change_rs.append(arr[i])

    for i in range(14,99,6):
        volume.append(arr[i])

    data = {"name" : name_arr,
    "close" : close_price,
    "prev_close" : prev_close_price,
    "percentChange" : change_percent,
    "RupeeChange" : change_rs,
    "volume": volume}

    with open( 'stocks_bse.json' , 'w') as stock:
        json.dump(data,stock)

def nse():
    search = "https://www.financialexpress.com/market/stock-market/nse-top-gainers/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    result = requests.get(search, headers=headers,proxies=urllib.request.getproxies())
    soup = bs4.BeautifulSoup(result.text,'lxml')
    text = soup.select('tr td')
    arr = []
    name_arr = []
    close_price = []
    prev_close_price = []
    change_percent = []
    change_rs = []
    volume = []
    for txt in text:
        arr.append(txt.getText())

    for i in range(9,99,6):
        name_arr.append(arr[i])
    
    for i in range(10,99,6):
        close_price.append(arr[i])

    for i in range(11,99,6):
        prev_close_price.append(arr[i])

    for i in range(12,99,6):
        change_percent.append(arr[i])

    for i in range(13,99,6):
        change_rs.append(arr[i])

    for i in range(14,99,6):
        volume.append(arr[i])

    data = {"name" : name_arr,
    "close" : close_price,
    "prev_close" : prev_close_price,
    "percentChange" : change_percent,
    "RupeeChange" : change_rs,
    "volume": volume}
    with open( 'stocks_nse.json' , 'w') as stock:
        json.dump(data,stock)

bse()
nse()
