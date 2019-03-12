import requests
from lxml.html import fromstring

def get_proxies():
	#saving the url in a local variable 
	url='https://free-proxy-list.net/'
	#loading the website. Now we have an object 'response' and can extract infos from it
	response = requests.get(url)
	#decoding the content from the website
	parser= fromstring(response.text)
	#we could check the encoding (propably UTF-8)
	#response = resonspe.encoding()
	
	#Instantiating 'proxies' variable as datatype set
	#a set is an unordered collection of unique and unchangeable Elements
	proxies=set()
	
	for i in parser.xpath('//tbody/tr'):
		if i.xpath('.//td[7][contains(text(),"yes")]'):
			#Grabbing the IP and corresponding port
			proxy= ":".join([i.xpath('.//td[1]/text()')[0],i.xpath('.//td[2]/text()')[0]])
			proxies.add(proxy)
			return proxies

#For testing purposes
#proxies = get_proxies()
#print(proxies)
