
#ex2 question j
from urllib import request, parse

with request.urlopen("https://duckduckgo.com/?q=Rocco's+basilisk&format=json&pretty=1") as query:   #search for the phrase “Rocco's basilisk”
    
    headers = query.headers.items()     #store headers in a list
    body = query.read().decode("utf-8") #store body after decoding

    print("\n ex2 j \n")
    print(headers)
    print("\n")
    print(body)
