from bs4 import BeautifulSoup
import requests
import time
#Getting the functions from the other python script (hideIP.py)
import hideIP


#15 Minutes * 60 seconds = 900
timeuntilfetch=900
#Convert the time until fetch into a set time
#Get the Time right now and add timeuntilfetch-time to it
#nextfetchtime=

#proxies= {"http": "http://"proxies, "https": "http://"proxies}
#Alternativeley just delete / comment out this line and try with 
#the format provided via my hideIP function (rewuests.get(proxies=proxies)
#or format the output of hideIP in a line above 

#Former this was a function but as I need proxies as global variable 
#I just put it in the main programm
#Calling the function get_proxies() I wrote in the other file to get a proxy



def getData(proxy):
   
    #Getting the Website in HTML
    website= requests.get("https://www.skyscanner.de/transport/fluge/cgn/spu/190713/190721/?adults=2&children=0&adultsv2=2&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=true&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results", proxies=proxies)
    #Open the Website's html and read it 
    raw_html=open('website').read()
    #html=BeautifulSoup(raw_html, 'html_parser')
    
    #Testing
    print(html)
    
        
def userAgent():
    #Addition: User agent spoofing
    #Everytime you visit a website, it gets your browser information via user agent
    #It would look suspicious if we send 200 requests/second with the same user
    #agent so we generate one by ourselves
    from user_agent import generate_user_agent
    #generate user agent
    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    ##headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'}
    page_response = requests.get(page_link, timeout=5, headers=headers)


def passData():
    #Open the csv file in "write"-mode
    abc=test
    #Don't forget to close the file


#def convertProxieFormat(proxy):
    #As rewuests.get needs proxy in a string format we have to do this typecasting
    #converting proxy from 'set'-Datastructure to string
    #proxy=str(proxy)
    #Stripping of the brackets
    #proxy=proxy.strip('{')
    #proxy=proxy.strip('}')
    #print(proxy)
    #proxies= {
    #"http": "http://"+proxy,
    #"https": "https://"+proxy,}
    #print(proxies)
    

    

def main():
	#The real programm
    print("Processing...")
    proxy= hideIP.get_proxy()
    print("Your IP adress is ", proxy)
    convertProxieFormat(proxy)
    #getData(proxy)
    #getData()
#	userAgent()
#	passData()
#	timeout(timeuntilfetch)
#   print(f"Next fetch will be in {timeuntilfetch/60} minutes at {nextfetchtime}")

if __name__ == '__main__':
  main()
            
     
