import json

def locations_getter(filename):
    '''
    :param filename: the json file
    :return: list [[name, location],...]
    '''
    f = open(filename, encoding="utf8")
    data = json.loads(f.read())
    f.close()
    info = []
    users = data.pop('users')
    for i in users:
        ud = i
        name = ud.pop('name')
        location = ud.pop('location')
        if location != '':
            info.append([name, location])
        if __name__ == "__main__":
            print("""
            UserName: {0} 
            Location: {1}""".format(name,location))
    return info

if __name__ == "__main__":
    filename = input("enter name of json file: ")
    locations_getter(filename)