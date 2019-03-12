from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url ='http://books.toscrape.com'
#Downloading the webpage with urlopen from requests
uClient = uReq(my_url)
#Getting the raw html and storing it in a variable
page_html = uClient.read()
#Close the client 
uClient.close()
#Parse the html with BeautifulSoup
page_soup = soup(page_html, 'html.parser')

#Just testing – I can access every HTML element now 
#print(page_soup.h1)
#print(page_soup.p)

#Grabs each price based on the container it's lying in 
#1. go to price on Website, click "inspect"
#2. Look for the div-class that's one above the tag 
#3. Copy the name of the div tag class
containers= page_soup.findAll("li",{'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

#How many elements did he find? or: How many product containers do we have?
print(len(containers)) #out: 20

#Contains one Book-Info, because [0] is the first element of the 12 containers
container = containers[0]
print(container.article.div.p)

#https://www.youtube.com/watch?v=XQgXKtPSzUI

