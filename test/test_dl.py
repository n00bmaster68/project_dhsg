import os, re
import json 
import requests 
import urllib.request
from bs4 import BeautifulSoup 


GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def main():
    download_images()
    get_image_urls_fr_gs()
    
def download_images():
    # ask for user input
    data = input('What are you looking for? ')

    print('Start searching...')
    
    searchurl = GOOGLE_IMAGE + 'q=' + data
    print(searchurl)

    response = requests.get(searchurl, headers=usr_agent)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all("img", class_="rg_i")
    print(len(results))
    
    # extract the link from the div tag
    # imagelinks = []
    # for re in results:
    #     try:
    #         imagelinks.append(re['src'])
    #     except:
    #         imagelinks.append(re['data-src'])

    # print(f'found {len(imagelinks)} images')
    # print('Start downloading...')
    # count = 0
    # path = './' + 'folder_name' + '/'
    # os.mkdir('D:/project/test/{}'.format('folder_name'))

    # for imagelink in (imagelinks):
    #     urllib.request.urlretrieve(imagelink, path + str(count) + ".jpg")
    #     count += 1
    #     print("Image no." + str(count) + " downloaded successfully")

    print('Done')


if __name__ == '__main__':
    main()