#E/16/388
#CO 324 lab3

from urllib import request  

response = request.urlopen("http://eng.pdn.ac.lk")  #make a request and get response


body = response.read()  #store request body

response.close() #close used resources

#ex1 question d
print("Type of body (question d): {} \n".format(type(body)))    #get body type




















