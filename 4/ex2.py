import requests
import json
import requests
from typing import List , Tuple


with requests.Session() as session: #create a Session instance

    session.headers['Authorization'] = 'token feecf38355de126375fad51d1d891211f2be6ac6'  #initialize with authentication credentials(token)
    
    #data = {'name':'test', 'description':'some test repo'}  #data to post 
    response = session.get('https://api.github.com/orgs/cepdnaclk/members')  #make a post request using Session instance
    response = response.json()
    for member in response:  #for loop to iterate through details of each member
            
            data = {"page" : 1, "per_page" : 100}
            user = member['login']  #member name
            repos = session.get(member['repos_url'], params = data) #make a get request to url of the repository of each user
            repos = repos.json() #r
            print(repos)
            break
    #store and print response
   # formated_response = response.json()    

    
    #GET /orgs/:org/members
