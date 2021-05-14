

import requests
from typing import List , Tuple


from typing import List, Tuple

def github_superstars(orgnanization: str) -> List[Tuple]:

    stars = []
    
    
    with requests.Session() as session:
        session.headers['Authorization'] = 'token feecf38355de126375fad51d1d891211f2be6ac6'  #initialize with authentication credentials(token)

        response = session.get('https://api.github.com/orgs/' + orgnanization + '/members')
        response = response.json()
         
        for member in response:
            
            data = {"page" : 1, "per_page" : 100}
            user = member['login']
            repos = session.get(member['repos_url'], params = data)
            repos = repos.json()

            maximum = 0

            for repo in repos:
                
                if maximum < repo['stargazers_count']:
                    maximum = repo['stargazers_count']
                    repository = repo['name']

            stars.append((user, repository, maximum))

    stars.sort(key = lambda arr: arr[2], reverse = True)

    return stars
                 
             
             
         
#github_superstars("cepdnaclk")
print(github_superstars("cepdnaclk"))

