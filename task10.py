# import json
# from bs4 import BeautifulSoup
# with open("task5.json","r+")as f:
#     data = json.load(f)
# def analyse_language_and_directors(data):
#     dic={}
#     for i in data:
#         for j in i["director"]:
#             dic[j]={}
#     for director in dic:
#         for dic_movie in data:
#             if director in dic_movie["director"]:
#                 if "language" in dic_movie:
#                     lan=dic_movie["language"]
#                     language_Count=0
#                     dic[director][lan]=language_Count
#                     for each_dict in data:
#                         if "language" in each_dict:
#                             lan2=each_dict["language"]
                            
#                                 dic[director][lan]+=1
#                                 language_Count=+1

#     with open("task10.json","w+") as file:
#         json.dump(dic,file,indent = 4)
# analyse_language_and_directors(data)

import json
with open("task5.json","r+")as file:
    movies_details=json.load(file)
def analyse_language_and_directors():
    dic={}
    list=[]
    for i in movies_details:
        for j in i["director"]:
            if j not in list:
                list.append(j)
    for i in list:
        dic1={}
        for j in movies_details:
            if i in j["director"]:
                if "Language" in j:
                    language=j["Language"]
                    # print(language)
                    for k in language:
                        
                        if k in  dic1:
                            dic1[k]+=1
                        if k not in dic1:
                            dic1[k]=1
                dic[i]=dic1
    with open("task10.json","w+") as file:
        json.dump(dic,file,indent=4)

analyse_language_and_directors()
