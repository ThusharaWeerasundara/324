#E/16/388
#CO 324 lab3


from urllib import request #for http requests
import json  #use json format
from typing import List  #work with lists



#ex3 a
def ddg_query(url: str, nr_results: int) -> List[str]:

    search_entry = url.strip().split(" ") #seperate input words by spaces
    req_type = "+".join(search_entry) #connect input words by '+' for the query
    
    response = request.urlopen(f"https://www.duckduckgo.com/?q={req_type}&format=json&pretty=1") #make a request
    body = json.loads(response.read().decode("utf-8"))  #store response in json format

    print(body)
    results = []    #to store reults
    related_topics = [] 

    if nr_results > 0:   #if valid int for nr_result is given extract urls in 2 loops

        for item in body['Results']: 
            results.append(item['FirstURL'])
            
        for item in body['RelatedTopics']:
            related_topics.append(item['FirstURL'])        
         
        total = results + related_topics #get total results
            
        if(nr_results > len(total)):    #if nr_results is larger than total result size return whole results
            return total

        response.close() #close used resources                 

        return (total[ :nr_results])    #else return requested url list

    return [] #for invalid nr_results return empty list
   
print("ex3 a \n ")
print(ddg_query("university of peradeniya", 1))  #calling ddg_query

