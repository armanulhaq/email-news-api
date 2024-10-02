import requests
from send_email import send_email

api_key = "00a7a6936d9542b5b0ad4927e6ca27ac"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=00a7a6936d9542b5b0ad4927e6ca27ac"

#Make request
request = requests.get(url)

#Get data in a dictionary
content = request.json()

#Access title and description of data
body = ""
for article in content['articles']:
    body = body + article['title'] + "\n" + article['description'] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
