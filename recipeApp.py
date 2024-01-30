import requests
from bs4 import BeautifulSoup

class Recipe:
    def __init__(self,Ingredients,directions,Nutrition_info):
        self.Ingredients = Ingredients
        self.directions = directions
        self.Nutrition_info = Nutrition_info

url = 'https://www.allrecipes.com/recipe'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

recipe_list = []
urls = []
filter_out =  ["auth","pinterest","twitter","flipboard","news","magazines","youtube","tiktok","instagram","facebook","tips","article","gallery","author","about-us","meredith"]


for link in soup.find_all('a'):
    if any (x in str(link) for x in filter_out) :
        continue
    print(link.get('href'))
    urls.append(link)

for link in urls:
    response2 = requests.get(link)
    soup2 = BeautifulSoup(response.content,"html.parser")
    anchor_tag = soup2.find('h',text ='Directions')

print(len(urls))
