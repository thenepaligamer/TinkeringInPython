"""
We are using themoviedb for retrieving movie data
"""

import requests
from pprint import pprint

API_KEY = '348ba04d676ea0f56b13e794edbf05a0'

query_params = {
    "limit": 10
}

ask = input("What would you like to do \n1: See trending movies \n2: See upcoming movies \n3: Search movie \n4: Current popular movies on TheMovieDatabase \n")

match ask:
    case "1":
        time_period = input("\nEnter trending list time period: ")
        TrendingURL = 'https://api.themoviedb.org/3/trending/movie/'+time_period+'?api_key='+ API_KEY
        request_data = requests.get(TrendingURL, params= query_params).json()
        pprint(request_data)

    case "2":
        UpcomingURL = 'https://api.themoviedb.org/3/movie/upcoming/?api_key='+ API_KEY
        request_data = requests.get(UpcomingURL, params= query_params).json()
        pprint(request_data)
        
    case "3":
        search = input("\nEnter the movie you want to search: ")
        MovieSearchURL = 'https://api.themoviedb.org/3/search/movie?api_key='+API_KEY+'&language=en-US&query='+search+'&page=1&include_adult=false'
        request_data = requests.get(MovieSearchURL, params=query_params).json()
        pprint(request_data)
        
    case "4":
        PopularURL = 'https://api.themoviedb.org/3/movie/popular/?api_key='+ API_KEY
        request_data = requests.get(PopularURL, params= query_params).json()
        pprint(request_data)