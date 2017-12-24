## Author: Christopher Hampton
import os

Pre_Query = input("What do you want to search on Youtube?: ")
Query = Pre_Query.replace(' ', '+')
URL = 'start http://www.youtube.com/results?search_query=' + Query
os.system(URL)
