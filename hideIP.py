import requests
from lxml.html import fromstring

def get_proxy():
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
	proxy=set()
	
	for i in parser.xpath('//tbody/tr'):
		if i.xpath('.//td[7][contains(text(),"yes")]'):
			#Grabbing the IP and corresponding port
			proxy_content= ":".join([i.xpath('.//td[1]/text()')[0],i.xpath('.//td[2]/text()')[0]])
			proxy.add(proxy_content)
			return proxy

#For testing purposes
#proxies = get_proxy()
#print(proxy)
