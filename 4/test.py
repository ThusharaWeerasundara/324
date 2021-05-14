

import requests
from typing import List , Tuple


from typing import List, Tuple

def github_superstars(orgnanization: str) -> List[Tuple]:

    i = 1
    #Sirasa superstar for Computer engineers. :
    with requests.Session() as session:
         response = session.get("https://api.github.com/orgs/cepdnaclk/members")
         response = response.json()
         for member in response:
             
             print(member['login'])
             response2 = session.get(member['repos_url'])
             response2 = response2.json()
             print(member['repos_url'])
             print()
             
             
         


github_superstars("svj")
