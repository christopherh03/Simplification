import os
# Christopher Hampton
site_query = input("Enter a website name to search on: ")
search_query = input("Enter a search query: ")
url = " start http://" + site_query + ".com/search?q=" + search_query
os.system(url)
