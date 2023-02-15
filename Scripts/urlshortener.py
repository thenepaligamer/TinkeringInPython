"""
Before you run this project, remember to install pyshorteners
pip install pyshorteners

If pip is not installed then 
sudo apt update
pip install pyshorteners
"""

import pyshorteners

xs = input("What would you like to do \n1: URL Shortening \n2: URL Expanding\n")

match xs:
    case "1":
        link = input("\nEnter the link you want to shorten it: ")
        shortenedlink = pyshorteners.Shortener()
        shortlink = shortenedlink.tinyurl.short(link)
        print("\nShortened link is: "+shortlink)
    
    case "2":
        link = input("\nEnter the link you want to expand it: ")
        shortenedlink = pyshorteners.Shortener()
        expandedLink = shortenedlink.tinyurl.expand(link)
        print("\nExpanded link is: "+expandedLink)
        
"""
https://github.com/larymak/Python-project-Scripts
https://www.askpython.com/python/examples/sudoku-solver-in-python
"""

