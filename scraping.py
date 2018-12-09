import requests
import pandas as pd
import pickle
from time import sleep
mainpage = 'https://www.immobiliare.it'

from bs4 import BeautifulSoup
 

def get_announcement(ann):
    title = ann.find('p', class_ = 'titolo text-primary').a['title']
    link = ann.find('p', class_ = 'titolo text-primary').a['href']

    locali, superficie, bagni, piano = 'NA','NA','NA','NA'

    if not link.startswith('https://www.immobiliare.it'):
        link = mainpage + link
    subcontent = requests.get(link)
    subsoup = BeautifulSoup(subcontent.text, "html.parser")
    infos = subsoup.find('div', class_='im-property__features')


    price = infos.find('span', class_='features__price--double')
    if price is None:
        price = infos.find('ul', class_='features__price-block').find('li', class_='features__price').span
    price = price.getText()

    subinfos = infos.find('ul', class_='list-inline list-piped features__list')

    for list_item in subinfos.find_all('li'):
        feature = list_item.find('div', class_='features__label')

        if feature is not None:
            if feature.getText() == 'locali':
                locali = list_item.find('div').find('span').getText()
            elif feature.getText() == 'superficie':
                superficie = list_item.find('div').find('span').getText()
            elif feature.getText() == 'bagni':
                bagni = list_item.find('div').find('span').getText()
            elif feature.getText() == 'piano':
                
                piano = list_item.find('div').find('span')
                if piano is None:
                    piano = list_item.find('div').find('abbr')
                    
                piano = piano.getText()


    description = subsoup.find('div', class_='left-side')
    description = description.find('div', class_='col-xs-12 description-text text-compressed').div.getText()

    attr_list=[title, price, locali, superficie, bagni, piano, description]
    sleep(1)
    return attr_list




def scraping_function():
    counter=0

    ann_list = []

    for i in range(1,1700):

        # request the html page
        content = requests.get("https://www.immobiliare.it/vendita-case/roma/?criterio=rilevanza&pag=%i"%i)
        # soupify it
        soup = BeautifulSoup(content.text, "lxml")



        # find all the tags li with class 'listing-item vetrina js-row-detail'
        announcements = soup.find_all('li', class_ = 'listing-item vetrina js-row-detail')
        if len(announcements) == 0:
            announcements = soup.find_all('li', class_ = 'listing-item js-row-detail')

        #print('%d ann in page %d'%(len(announcements),i))


        for ann in announcements:

            try:
                attr_list = get_announcement(ann)
                ann_list.append(attr_list)
                counter=counter+1
                print(i,counter)
            except:
                print('error in scraping announcement, moving to next one')
                
            columns = ['title', 'price', 'locali', 'superficie', 'bagni', 'piano', 'description']
            df = pd.DataFrame(ann_list,columns=columns)
            df.to_csv('data/raw_data.csv')

            if counter==10000:
                
                columns = ['title', 'price', 'locali', 'superficie', 'bagni', 'piano', 'description']
                df = pd.DataFrame(ann_list,columns=columns)
                df.to_csv('data/raw_data.csv')
                return





