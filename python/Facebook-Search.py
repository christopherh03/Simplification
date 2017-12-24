## Author: Christopher Hampton
import os

Pre_Query = input("What do you want to search on Youtube?: ")
Query = Pre_Query.replace(' ', '+')
URL = 'start https://www.facebook.com/search/top/?q=' + Query
os.system(URL)
