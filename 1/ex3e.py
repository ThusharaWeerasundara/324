#ex3e

def load_users_to_dict(filename):

    users = dict()  #users dictionary to store entries

    with open(filename) as f: #open file

        for line in f:  #iterate through lines

            id, login = line.split()  #split by space

            users[id] = login  #store login name according to id

    return users  #return results


users = load_users_to_dict('userdata.txt')    #method call

for id in users:      #using loop to go through id in results
    print("id: {}, user's login: {}".format(id, users[id]))   #display logins
