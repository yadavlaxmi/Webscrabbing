  
# import requests
from bs4 import BeautifulSoup
import json
from task1 import scrape_top_list
from task4 import movies_detailes
movie=scrape_top_list()
# ten_movies=movie[1:]
def get_movie_detailes():
    details=[]
    for i in movie:
        t=i["Url"]
        # print(t,"kkkkkkkkkkkkkkkk")
        a=movies_detailes(t)
        # print(a,"jjjjjjjj")
        details.append(a)
        print(details)
    with open("task5.json","w+") as file:
        json.dump(details,file,indent=4)           
get_movie_detailes()

