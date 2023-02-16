"""
We are using newscatcher api for getting news
"""

import requests

API_KEY = '4dxW8CeAvZjmx17UL1pi6RLamw6BV058P2BVD4zD-ZE'

url = 'https://api.newscatcherapi.com/v2/search'

topic_name = input("Enter the topic you want to search: ")
topic_lang = input("Enter the language of news: ")

headers = {
    "x-api-key" : API_KEY
}

querystring = {"q": topic_name, "lang": topic_lang, "sort_by":"relevancy", "page":"1"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)