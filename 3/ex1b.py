#E/16/388
#CO 324 lab3

from urllib import request  

response = request.urlopen("http://eng.pdn.ac.lk")  #make a request and get response


body = response.read()  #store request body

response.close() #close used resources

#ex1 question b
details = response.headers.items()  #storing header details in a list and display the list
print("Details (question b): {} \n".format(details))

print("Server and OS: {} \n".format(response.headers['Server'])) #use Server key to get required details from dictionary








