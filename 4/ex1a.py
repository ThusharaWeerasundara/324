import requests  

response = requests.get('https://api.github.com')   #making a get request to url
print(response.text)  #convert response into a string and print


