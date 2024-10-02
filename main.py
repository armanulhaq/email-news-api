import requests

api_key = "00a7a6936d9542b5b0ad4927e6ca27ac"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=00a7a6936d9542b5b0ad4927e6ca27ac"

#Make request
request = requests.get(url)

#Get data in a dictionary
content = request.json()

#Print title and description of data
for article in content['articles']:
    print(article['title'])
    print(article['description'])
