import requests

response = requests.get('https://api.github.com/users/ThusharaWeerasundara')  #Geting my Github profile information from the endpoint 

print(response.text)    #convert response into a string and print
