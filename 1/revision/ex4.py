def load_users_to_dict(filename):

    users = dict()

    with open(filename) as f:

        for line in f:
            line = line.strip()
            id, login = line.split(',')

            users[id] = login

    return users

users = load_users_to_dict("userdata_for_part_g.txt")

for id in users:
    print('id: {}  login: {}' .format(id,users[id]))
