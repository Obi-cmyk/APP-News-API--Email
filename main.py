import requests
from send_email import send_email


api_key = "eb7a5794dd8a4b378a1b782372d5222c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-24&" \
    "sortBy=publishedAt&apiKey=" \
    "eb7a5794dd8a4b378a1b782372d5222c"
# make a request
request = requests.get(url)

# Get a dict. with data
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = ("Subject: Today's news" + "\n" + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2 * "\n")

body = body.encode("UTF-8")
send_email(message=body)
