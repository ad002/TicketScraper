Basic Idea

- take existing HTML data 
- use webscraper to extract the wanted data 
- convert data into a useful format 
- analyse data 

01 HTML STRUCTURE 

<body>
<h1>This is a header tag </h1>
     <div> [OPENING TAG]
	<p>Divs contain other elements like paragraph</p>
	<ul> [PARENT ELEMENT]
	   <li>and unordered lists</li> [CHILD ELEMENT]
	   <li>also unordered list</li>
	</ul>
	<table>
	    <th>tables header</th>
            <tr>
		<td>this is a table</td>
	    </tr>
	</table>
      </div> [CLOSING TAG]
</body>

- all elements are contained within the opening and closing 'body' tags
- every element has it's own opening and closing tag
- elements that are nested or intended in an HTML structure indicate that the element is a
  child element of it's container, or in other words: of it's parent element
- if we start scraping, we can not only identify elements that we want to scrape based on 
  their tag name, but also whether the element is a child of another element 

-> we can see that there is a <ul> element, indicating an unordered list 
-> each list element <li> is a child of the parent <ul> tag 
-> if we wanted to scrape the entire list, we want to tell Python to grab all of the child
   elements of the <ul> tag. 



02 HTML STRUCTURE – ELEMENTS

						Element type &
 Class attribute    				closing indicator 				
       |					    |
<h1 class="myClass" id="id_1">This is a header tag</h1>
 |		     |			|
Element		   ID attribute      Element content
Type & 
opening
indicator


- if we told Python we want the <h1> element, that would be fine, unless there are several 
  other <h1> elements on the page 
- if we want the first or the last <h1> tag, we might need to be specific in telling Python 
  to do so. 
- most elements give us "class" and "id" attributes

-> if we wanted to select only this specific <h1> element, we might be able to do so by  
   telling Python "give me the <h1> element, that has the class "myClass"
-> "ID" selectors are even more specific
-> so sometimes, when the "class" selectors return more elements than wanted, select with 
   the ID attribute


03 REQUESTS

Requests with Python and BeautifulSoup will basically have three parts:
1. URL: 'www.twitter.com'
2. RESPONSE: get(URL)
3. CONTENT: BeautifulSoup(response.content, 'html.parser')

THE URL
simply a string that contains the address of the HTML pages we intend to scrape

THE RESPONSE
- the response is the result of the GET request 
- we actually use the URL variable in the GET request here
- if we look what the resonse is, it's actually an HTTP status code
- if the request was successful, we'll get a status code like 200 
- if the request wasn't successful, there might be a problem with the request or
  the server doesn't respond to the request we made. 
- this will result in a status code like 404 for example
- if we don't get what we want, we can look up the status code to troubleshoot what 
  the error might be 
- useful resource: restapitutorial.com
- we maybe could ask if response == 200: go on, if not: print error code

THE CONTENT 
- the content is the content of the respond. If we print the entire response content, 
  we'll get all the content on the entire page of the URL we've requested.
- this would happen if we say 
  $ print (content) 








