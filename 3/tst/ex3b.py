#E/16/388
#CO 324 lab3


from urllib import request #for http requests
import json  #use json format
from typing import List  #work with lists

#ex3 b
def spider_metadata(urls: List[str]) -> List[List]:

    http_headers = [] #store results

    for URL in urls:   #use a loop to retrieve headers from urls and append to a list
        response = request.urlopen(URL)
        http_headers.append(response.headers.items())

    response.close() #close used resources

    return http_headers  #return the list


header_list = ["http://eng.pdn.ac.lk","https://www.youtube.com/"] 
print("ex3 b \n ")
print(spider_metadata(header_list))
