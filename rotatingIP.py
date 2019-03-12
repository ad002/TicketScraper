from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random 

"""Retrieving a list of valid HTTPs proxies from sslproxies.org"""

#Simulating a real request
ua= UserAgent() #From where we generate a random user agent
proxies=[] #Will contain proxies [ip, port]


#Main function 
def main():
    #Our code here
    #Scraping  sslproxies.org with BeautifulSoup
    
    #Initializing a request
    proxies_req = Request('https://www.sslproxies.org/')
    #attaching a random user agent to the request 
    proxies_req.add_header('User-Agent',ua.random)
    #retrieve contents
    proxies_doc = urlopen(proxies_req).read().decode('utf8')
    
    
    #Now creating a new BeatifulSoup Instance, we scan all the rows contained 
    #in the main table by passing the soup the opened and decoded url
    soup=BeautifulSoup(proxies_doc,'html.parser')
    #Find elements
    proxies_table = soup.find(id='proxylisttable')
    
    #Save the proxies in the empty array created in line 10
    for row in proxies_table.tbody.find_all('tr'):
        #Saving a new dict with the keys IP and Port
        proxies.append({
        'ip': row.find_all('td')[0].string,
        'port': row.find_all('td')[1].string
        })
    
    #Getting random ints / dict-keys
    proxy_index = random_proxy()
    #Get the proxy at random 
    proxy = proxies[proxy_index]
    
       
    #for testing purpose, we'll make 100 requests to icanhazip.com which will 
    #return our currentIP (proxied, of course)
    for n in range(1,100):
        req = Request('http://icanhazip.com')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'],'http')
        
        #Every 10 requests, generate a new proxy
        if n%10 ==0:
            proxy_index = random_proxy()
            proxy=proxies[proxy_index]

    #Now with a catch/try we intercept broken proxies and delete them from 
    #our list and notice the user. Or, if the request has been succesfull, 
    #we print what IP icanhazip see.

    #make the call 
        try:
            my_ip =urlopen(req).read().decode('utf8')
            print('#' + str(n) + ':' +my_ip)
        except: #if error, delete this proxy and find another one 
            del proxies[proxy_index]
            print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted')
            #generate new proxy
            proxy_index = random_proxy()
            proxy=proxies[proxy_index]

#We need this for testing putposes, to get a random proxy out of our list
#Note that we return the key to the proxy and not the value of the proxy
#-> if a proxy fails, we want to remove it from the list so we won't catch it again
def random_proxy():
    return random.randint(0,len(proxies)-1)
 
    

#This command will be needed later on for the rewuests.get function
#req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

    
if __name__=='__main__':
    main()
