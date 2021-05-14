from urllib import request #for http requests
import json  #use json format
from typing import List  #work with lists


with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1") as query:   #after appending &format=json&pretty=1

    headers = query.headers.items()     #store headers in a list

    body = query.read().decode("utf-8")     #store body

    
    print("\n")
    print(body)
