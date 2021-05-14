#ex3g
def load_users_to_dict(filename):

    users = dict()      #dictionary to store entries

    with open(filename) as f:   #open file

        for line in f:  #iterate through lines

            row = line.strip()  #remove whitesapace(new line character) from each row
            id, login = row.split(',')  #split by ,


            users[id] = login  #store login name by user id

    return users #return results

print(load_users_to_dict("userdata_for_part_g.txt")) #testing by printing
