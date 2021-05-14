def load_users_to_dict(filename):

    users = dict()

    with open(filename) as f:

        for line in f:

            id, login = line.split()

            users[id] = login

    return users

users = load_users_to_dict("userdata.txt")

for id in users:
    print('id: {}  login: {}' .format(id,users[id]))
