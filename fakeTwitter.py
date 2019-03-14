from bs4 import BeautifulSoup
import requests

url = 'https://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')

#Just to check whether everything worked finde
#print(content)

#get text from the <p> tags which are from class content 
tweet = content.find('p', {"class":"content"})#.text or, same: 
#print(tweet.text)
#Works fine for one item, if I wanna do find_all it breaks
#AttributeError: ResultSet object has no attribute 'text'. You're 
#probably treating a list of items like a single item. Did you call 
#find_all() when you meant to call find()?
#-> Find_all method returns a generated list (loosely using the term list
#here) of items that beautifulsoup has found matching my criteria 
#after parsing the source webpages html recursiveley or non-recursevely
#depending on how you search
#The resulting set of objects has no attribute text, since it isn't an
#element but rather a collection of them! However, the single item inside 
#the resulting set (should any be found) do. 

print(type(content)) #<class 'bs4.BeautifulSoup'>
#-> means all the elements that match the class 
print(tweet.text)


#I tried: 
#for p in content.find_all('p', {'class':'content'}):
    #print(tweet.text)
#Which just prints the same tweet all over again 
    
    
#what you can do is iterate over the single elements via:
for tweet in content.find_all('p',{'class':'content'}):
    print(tweet.text)
#For everything you find in the content (HTML)which is a div and is 
#from class content (which is a bit misleading here, but meant are the 
#div tags which are from class content on the website,
# print that out after transforming it to text 

#So why is it 'for tweet in ..' ???
#Just a quick refresher on for LOOPS
#1. Loops where I know how often to repeat:
for x in range(10):
     print(x)
#out: 0 1 2 3 4 5 6 7 8 9 

#2. Loops where I dont know how often to iterate
collection=['hey', 5, 'd', 'fuck', 'I', 'need', 'training']
for x in collection:
    print (x)

#No need to distinguish:
#"Do this until this ending condition happens"

#What my mistake was (I guess):
#you have to call functions like this:
# for IT in WHENTOSTOP:
   #print IT    #or do whatever with IT
#-> important is that the thing after the 'for' is being repeated
#-> down in the 'iteration'-field of the for loop

#I dont fucking know why this shit doesn't worl 
#for x in content.find_all('div', {'class':'content'}):
#    print(p.text())



