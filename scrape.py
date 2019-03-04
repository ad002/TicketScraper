from b4s import BeautifulSoup
import requests
import time

#15 Minutes * 60 seconds
timeuntilfetch=900
#Convert the time until fetch into a set time
#Get the Time right now and add timeuntilfetch-time to it
#nextfetchtime=

def getData():
    page_link = 'https://www.skyscanner.de/transport/fluge/colo/spu/190713/190721/?adults=2&children=0&adultsv2=2&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results'
    #Fetch the content from URL
    page_response = requests.get(page_link, timeout = 10)
    #Parse html
    page_content=BeautifulSoup(page_response.content, "html.parser")

    #extract all html elements where price is stored
    prices= page_content.find_all(class_='CTASection__price-2bc7h price')
    if prices is None:
        print("Can't get any price")
    print(f"The price is {prices} right now")

print(prices)

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

    #Don't forget to close the file

def changeIP():
    #find a way to get rid of my actual IP and rotate to another


#The real programm
userAgent()
getData()
changeIP()
passData()
timeout(timeuntilfetch)
print(f"Next fetch will be in {timeuntilfetch/60} minutes at {nextfetchtime}")
