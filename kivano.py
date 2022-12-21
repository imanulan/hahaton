from bs4 import BeautifulSoup as BS
import requests
import csv


def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html,'lxml')
    return soup

def get_data(soup):
    phones = soup.find_all('div',class_='product_listbox')        
    
    for phone in phones:
        title = phone.find('div',class_='listbox_title').text.strip()
        
        try:
            price = phone.find('div',class_='listbox_price').text
            
        except AttributeError:
            price = None

        image = phone.find('img').get('src')


        write_csv({
            'title': title,
            'image': price,
            'price': image
        })      

def write_csv(data):
    with open('phones.csv','a') as file:
        names = ['title','price','image'] 
        write = csv.DictWriter(file,delimiter=',',fieldnames=names)
        write.writerow(data)       


def main():
    BASE_URL = 'https://www.kivano.kg/mobilnye-telefony'

    html = get_html(BASE_URL)
    soup = get_soup(html)
    get_data(soup)

main()    

