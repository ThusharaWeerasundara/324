import ex2a #import ex2a for use the method github_superstars
import requests

repos_with_most_stars = ex2a.github_superstars("cepdnaclk")  #get repos with post stars
print(repos_with_most_stars)    #print answers

print()
print(repos_with_most_stars[0][0] + ' is the winner.') #winner
print()

#make a put request with authorization headers to subscribe to winner
response = requests.put(repos_with_most_stars[0][0] + '/subscription', headers = {'Authorization' : 'token feecf38355de126375fad51d1d891211f2be6ac6', 'Accept': 'application/vnd.github.v3+json'})
print(response.json())  #print response
