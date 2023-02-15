"""
Before you run this project, remember to install pyshorteners
pip install pyshorteners

If this project doesn't run on your setup, make sure to check your python version.
This requires Python 3.10 or greater to run.
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

