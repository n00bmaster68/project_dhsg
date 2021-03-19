import requests  
from selenium import webdriver
from bs4 import BeautifulSoup

def get_html_source_by_selenium(url):
    driver_chrome = webdriver.Chrome("chromedriver.exe")
    driver_chrome.get(url)
    return driver_chrome.page_source


def get_url (filePath):
	searchUrl = 'http://www.google.com/searchbyimage/upload'
	# encode the image from filePath, use method post in requests lib to get the response, get the url from that response  
	multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
	response = requests.post(searchUrl, files = multipart, allow_redirects = False)
	fetchUrl = response.headers['Location'] 
	return fetchUrl

def get_titles(url):
	real_titles = []
	page = get_html_source_by_selenium(url)
	soup = BeautifulSoup(page, 'html.parser')
	#the titles are in h3 tags with class = "LC20lb DKV0Md"
	titles = soup.find_all("h3", {"class": "LC20lb DKV0Md"})

	for title in titles:
		#for instance the title is <h3 class = "LC20lb DKV0Md"> abcdnwiobw </h3>
		#; however, we only the text "abcdnwiobw", so I use the attribute text to get the parts I want in those h3 tag 
		real_titles.append(title.text)

	return real_titles

if __name__ == "__main__":

	filePath = "1.png"
	url = get_url(filePath)
	page = get_html_source_by_selenium(url)
	soup = BeautifulSoup(page, 'html.parser')

	try:
		title_link_part = soup.find_all("div", {"class": "hdtb-mitem hdtb-imb"})
		title_page_link = 'http://www.google.com' + title_link_part[0].a['href']
		
		print(title_page_link)

		titles = get_titles(title_page_link)
		print(titles)
	except Exception:
		print("Could not crawl")