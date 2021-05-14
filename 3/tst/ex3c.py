#E/16/388
#CO 324 lab3


from urllib import request #for http requests
import json  #use json format
from typing import List  #work with lists



#ex3 c

def spider_metadata(urls: List[str]) -> List[List]:

    http_headers = []

    for URL in urls:   #use a loop to retrieve headers from urls and append to a list. use HEAD method to only get header data
        Request = request.Request(URL, method = 'HEAD')

        response = request.urlopen(Request) 
        http_headers.append(response.headers.items()) 

    response.close()    #close used resources

    return http_headers #return list

print("ex3 c \n ")
header_list = ["http://eng.pdn.ac.lk"]
print(spider_metadata(header_list))

