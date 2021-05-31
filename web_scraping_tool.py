import requests as rq
from bs4 import BeautifulSoup as bs

github_user = input("Input Github User: ")
link = "https://github.com/"+github_user
request = rq.get(link)
soup = bs(request.content, 'html.parser')
profile_img = soup.find('img', {'alt' : 'Avatar'})['src']
print("This is link: ", profile_img)