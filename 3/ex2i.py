#E/16/388
#CO 324 lab3

from urllib import request, parse

with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya") as query:

    headers = query.headers.items()

    body = query.read()
    print("ex2\n")
    print(headers)
    print("\n")
    print(body)


#ex2 question i
    
with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1") as query:   #after appending &format=json&pretty=1

    headers = query.headers.items()     #store headers in a list

    body = query.read()     #store body

    print("\n ex2 i \n")
    print(headers)
    print("\n")
    print(body)
