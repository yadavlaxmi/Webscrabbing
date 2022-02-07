

import requests
import os
from task1 import scrape_top_list
data=scrape_top_list()
def get_scrape_movie_details():
    for i in data:
        path="/home/dell33/task8/task8"+i["Name"]+"text"
        if os.path.exists(path):
            pass
        else:
            create=open(path,"w+")
            url=requests.get(i["Url"])
            c=create.write(url.text)
get_scrape_movie_details() 