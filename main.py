import requests
from send_email import send_email

api_key = "00a7a6936d9542b5b0ad4927e6ca27ac"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=00a7a6936d9542b5b0ad4927e6ca27ac&language=en"

#Make request
response = requests.get(url)

#Get data in a dictionary
content = response.json()

#Access title and description of data
body = ""
for article in content['articles'][:10]:
    body = "Subject: Today's Headlines: \n" + body + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
