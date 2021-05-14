import requests

with requests.Session() as session: #create a Session instance 

    session.headers['Authorization'] = 'token feecf38355de126375fad51d1d891211f2be6ac6'  #initialize with authentication credentials(token)
    
    response = session.get('https://api.github.com/user')   #make a get request using the Session instance

    #storing and printing response
    formated_response = response.json()     
    print(formated_response)
    
