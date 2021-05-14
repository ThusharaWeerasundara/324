#E/16/388
#CO 324 lab3

from urllib import request  

response = request.urlopen("http://eng.pdn.ac.lk")  #make a request and get response


body = response.read()  #store request body

response.close() #close used resources

#ex1 question a
response_code = response.getcode()  #storing response code and display
print("response code (question a): {} \n".format(response_code))






























