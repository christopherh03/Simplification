## Author: Christopher Hampton
import os

Pre_Query = input("What do you want to search on Youtube?: ")
Query = Pre_Query.replace(' ', '+')
URL = 'start https://www.google.com/search?q=' + Query
os.system(URL)
