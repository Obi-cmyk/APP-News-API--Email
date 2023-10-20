import requests


api_key = "BIM-BIM"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-09-20&" \
       "sortBy=publishedAt&apiKey="\
       "eb7a5794dd8a4b378a1b782372d5222c")

request = requests.get(url)
content = request.json()
for article in content['articles']:
    length = len(content['articles'])
    print(article['title'])
    print(article['description'])
