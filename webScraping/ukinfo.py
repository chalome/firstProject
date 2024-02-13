import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

#See html source
# print(page.content)
'''Even though we have all the HTML saved in our code, it still looks like a whole 
lot of mumbo jumbo. We have to figure out how to parse out the exact
elements that we want - and we can use Beautiful Soup to do just that!

We can use Beautiful Soup to help find the elements that can be identified
with the class or the ID that we want to find. Similar to any library.
'''
soup = BeautifulSoup(page.content, 'html.parser')
print('The title is ')
#Get HTML page title
print(soup.title)

#Get string of HTML title
print('The title string is ')
print(soup.title.string)
#Find all elements with <a> tag
print('all elements with <a> tag  are ')
print(soup.find_all('a'))
# Find element with id of “link1”
print('element with id of “link1”')
print(soup.find(id="link1"))
#Find all p elements with class “title”
print('all p elements with class “title”')
print(soup.find_all("p", class_="title"))
print('///////////////////////////////')
titles = soup.find_all("a", class_="gem-c-document-list__item-title")
