import requests  

response = requests.get('https://api.github.com')   #making a get request to url

print(response.headers.json)
#print X-Ratelimit headers
for header in response.headers:
    if(header[0:11] == "X-Ratelimit"):
        print(header + " " + response.headers[header])
    


