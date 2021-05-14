#ex3f

def load_users_to_dict(filename):

    users = dict()  #users dictionary to store entries

    with open(filename) as f: #open file

        for line in f:  #iterate through lines

            id, login = line.split()  #split by space

            users[login] = id  #store id according to login

    return users  #return results


users = load_users_to_dict('userdata.txt')    #method call

for login in users:      #using loop to go through id in results
    print("login: {}, user's id: {}".format(login, users[login]))   #display logins
