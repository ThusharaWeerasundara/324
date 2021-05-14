
import requests
from typing import List , Tuple

def github_superstars(orgnanization: str) -> List[Tuple]:

    results = []    #list to store results
        
    with requests.Session() as session: #make an instance of Session
        session.headers['Authorization'] = 'token feecf38355de126375fad51d1d891211f2be6ac6'  #initialize with authentication credentials(token)

        response = session.get('https://api.github.com/orgs/' + orgnanization + '/members') #make get request to get members of the organization
        response = response.json() #response in json format
         
        for member in response:  #for loop to iterate through details of each member
            
            data = {"page" : 1, "per_page" : 100}
            #user = member['login']  #member name
            repos = session.get(member['repos_url'], params = data) #make a get request to url of the repository of each user
            repos = repos.json() #response in json format

            repository = repos[0]['url']    #set 1st url as max star url
            maximum = 0 #consider initial max stars for each user as 0

            for repo in repos: #go through all repositories for each user
                
                if maximum < repo['stargazers_count']:  #check for repository with max no of stars
                    maximum = repo['stargazers_count']  #set new max value
                    repository = repo['url']           #set repository url with max stars

            results.append((repository, maximum))   #append the list with required information for each user

    results.sort(key = lambda arr: arr[1], reverse = True)  #sort the list according to no of max stars

    return results #return list
                 
             
#print(github_superstars("cepdnaclk"))

