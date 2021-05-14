import requests
import json

with requests.Session() as session: #create a Session instance

    session.headers['Authorization'] = 'token feecf38355de126375fad51d1d891211f2be6ac6'  #initialize with authentication credentials(token)
    
    data = {'name':'revise', 'description':'some test repo'}  #data to post 
    response = session.post('https://api.github.com/user/repos', data = json.dumps(data))  #make a post request using Session instance

    #store and print response
    formated_response = response.json()    
    print(formated_response)
    
