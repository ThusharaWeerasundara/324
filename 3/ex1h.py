#E/16/388
#CO 324 lab3

from urllib import request  

response = request.urlopen(" https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")  #make a request and get response


body = response.read().decode("utf-8")   #store request body after decoding

response.close() #close used resources

#ex1 question f
print("After decoding (question g)\n")
print(body) 




















