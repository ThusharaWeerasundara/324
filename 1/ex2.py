#ex1

def load_users_to_lists(filename):

    ids, logins = list(), list()    #2 lists to store ids and login names

    with open(filename) as f:       #open file

        for line in f:              #iterate through lines

            id, login = line.split() #split strings by space
            ids.append(id)           #append 2 lists
            logins.append(login)
            # add details to the two lists using list.append()

    return ids, logins


ids, logins = load_users_to_lists("userdata.txt")   #calling the method

combined = zip(ids, logins) #combine arguments

print(combined)   #printing combined          

print(tuple(combined))  #printing combined as a tuple to see stored values
