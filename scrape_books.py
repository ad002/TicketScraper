from urllib.request import urlopen 
from bs4 import BeautifulSoup

my_url ='http://books.toscrape.com'
#Downloading the webpage with urlopen from requests
page = urlopen(my_url)
#Getting the raw html and storing it in a variable
page_html = page.read()
#Close the client 
page.close()
#Parse the html with BeautifulSoup
page_soup = BeautifulSoup(page_html, 'html.parser')

#Uncomment if interested in bursting the Console: 
#print(page_soup.prettify())

#Extracting all links found within a page's <a> tag
#for link in page_soup.find_all('a'):
#    print(link.get('href'))

#Getting all the text from the page 
#print(page_soup.get_text())

#We can access all HTML elements via . and then zoom further into the
#parse tree. This code gets the first <b> tag beneath the <body> tag
print(page_soup.body.b)

#This gets the first header inside the body 
print(page_soup.body.header)
#print(page_soup.find_all("div"))

#I guess why this is working is because of the 'class_ =' partition 
print(page_soup.find("p", class_="price_color").text)
#Let's try for an example by myself, this will give me the html in raw
print(page_soup.find("p", class_="instock availability"))
#Now in pretty using the .text command
print(page_soup.find("p", class_="instock availability").text) #doesn'nt work

#Find all elements 
#print(page_soup.find_all("p", class_="price_color").text) #doesn't workd
print(page_soup.find_all("p", text="price_color")) #out: []







#print(page_soup.find(id="price_color"))


#Just testing – I can access every HTML element now 
#print(page_soup.h1)
#print(page_soup.p)

#Grabs each price based on the container it's lying in 
#1. go to price on Website, click "inspect"
#2. Look for the div-class that's one above the tag 
#3. Copy the name of the div tag class
#containers= page_soup.findAll("li",{'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

#How many elements did he find? or: How many product containers do we have?
#print(len(containers)) #out: 20

#Contains one Book-Info, because [0] is the first element of the 12 containers
#container = containers[0]
#print(container.article.div.p)

#https://www.youtube.com/watch?v=XQgXKtPSzUI

