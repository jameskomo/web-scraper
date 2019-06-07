from bs4 import BeautifulSoup
import lxml
import requests
import time
import csv


def get_page(url):
    response=requests.get(url)
   
    
    
    if not response.ok:
        print('server responded:', response.status_code)
    else:
        # Converting HTML to Python Object
        soup=BeautifulSoup(response.text, 'lxml')
        
def get_detail_data(soup):
   
    try:
        title=soup.find('h1', id='itemTitle').find('a').get('data-mtdes')
        
    except:
        title=''

    try:
        price=soup.find('hspan1', id='prcIsum').text.strip().spli(' ')
        currency, price=p.spli(' ')
        
    except:
        price=''
        currency=''
    
    try:
        sold=soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0].replace('xa0', '')
        # xa0 will be in the final output thus replacing 
    except:
        sold=''

    # data-mtdes is the target attribute in this tag and a the target tag

    # DICTIONARY TO STORE ITEMS
    data={
        'title':title,
        'price':price,
        'currency':currency,
        'total sold':sold
    }
    return data

def get_index_data(soup):
    try:
        links=soup.find_all('a', class_='s-tem__link')
    except:
        links=[]
    urls=[item.get('href')for item in links]
    return urls

def write_csv(data,url):
    with open('ebay.csv', 'a') as csvfile:
        writer=csv.writer(csvfile)
        row=[data['title'], data['price'], data['currency'], data['total sold'], url]
        writer.writerow(row)

def main():
    url="https://www.ebay.com/sch/i.html?_nkw=men+watches&_pgn=1"
    products=get_index_data(get_page(url))
    for link in products:
        data=get_detail_data(get_page(link))
        write_csv(data, link)






















if __name__ == "__main__":
    main()