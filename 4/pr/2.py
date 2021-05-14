import requests
from typing import List , Tuple


from typing import List, Tuple

def github_superstars(orgnanization: str) -> List[Tuple]:

    #Sirasa superstar for Computer engineers. :
    with requests.Session() as session:
         git = requests.get("https://api.github.com/orgs/cepdnaclk/members")
         print(git.text)


github_superstars("svj")
