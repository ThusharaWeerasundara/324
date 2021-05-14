#ex2 question l

from urllib import request, parse

with request.urlopen("https://duckduckgo.com/?q="+parse.quote("තුෂාර+වීරසුන්දර")) as query: #query to search for my name. name is parsed
    
    headers = query.headers.items()         #store headers in a list
    body = query.read().decode("utf-8")     #store body after decoding

    print("\n ex2 l \n")
    print(headers)
    print("\n")
    print(body)    
