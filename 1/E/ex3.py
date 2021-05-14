#ex3

def load_users_to_dict(filename):

    users = dict()  #users dictionary to store entries

    with open(filename) as f: #open file

        for line in f:  #iterate through lines

            id, login = line.split()  #split by space

            users[id] = login  #store login name according to id

    return users  #return results


