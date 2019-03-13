This is a webscraper to fetch and watch flight ticket prices move during a period of time 

needed:
a get Data Function
a put Data in CSV Function
a Variable: Timeout for waiting between the fetches 
Some kind of output/Log what the programm is doing right now and when it'll fetch Data again.

Then I can just do the whole program like this:
getData() "Price right now is..." "Already passed to {Dateiname}.csv
Next fetch in XY Minutes @13:23"...

I should also consider using a VPN or a Proxy that is rotating IP adresses
Bet there's a plugin for that...

Before starting to scrape I should get a clue on how to read a robots.txt which
can be found for almost any site via https://anysite.com/robots.txt to see 
whether they have a problem with your bot or not. 

Following taken from https://bit.ly/2F5j9fN without any liability assumed. 

1. Full access
User-agent: *
Disallow:
-> All pages are crawlable 

2. Block all access 
User-agent: *
Disallow: /
-> no part of the site should be visited by using an automated crawler 
and violating this could mean legal trouble.

3. Partial Access
User-agent: *
Disallow: /folder/
User-agent: *
Disallow: /file.html
-> crawling only particular sections or files allowed

4. Visit time 
Visit-time: 0400-0845
-> hours when crawling is allowed. In this example, the site can be crawled 
between 04:00 and 08:45 UTC. Sites do this to avoid load from 
bots during their peak hours.

5. Crawl rate limiting 
Crawl-delay: 11
-> can be crawled with a delay of 11 seconds.

6. Request Rate 
Request-rate: 1/10
-> site allows crawlers to request one page every 10 seconds.

 
GETTING A PROXY
After some research and evaluation of whether using scrapy or whatever, I
found a really nice tutorial getting proxies from free-proxy-list.net and rotating it
https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/

So this tutorial also tought me something about scapring which'll be useful later on
because we want to automate proxy change and don't enter every proxy by hand 
as they change quite often on https://free-proxy-list.net/. I guess. 
-> This worked fine for getting one single IP Address

As I was facing some serious trouble when trying to convert this single proxy
in a fitting format for the requests.get(proxies=proxies) method, I'll try
something different first on
https://codelike.pro/create-a-crawler-with-rotating-ip-proxy-in-python/



More tutorials
More general
https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
https://www.pythonforbeginners.com/beautifulsoup/scraping-websites-with-beautifulsoup

Good tutorial
https://www.youtube.com/watch?v=XQgXKtPSzUI

Perfect example to copy
-> Use their website and solve the problem by myself and then see how they did

https://realpython.com/python-web-scraping-practical-introduction/


As I still can't figure out some wokring free-hands file for me I decided to 
practice some more. Or: Follow another fucking tutorial until I make it. 
The Tutorial is quite good tho. Object oriented and taken from here: 
https://medium.com/the-andela-way/learn-how-to-scrape-the-web-2a7cc488e017

A German one: 
https://www.btelligent.com/blog/howto-einfaches-web-scraping-mit-python/

The latest one using a Fake-Twitter-Site and also parsing it to csv
https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184
 




