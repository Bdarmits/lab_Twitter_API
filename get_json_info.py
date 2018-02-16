import json

def json_reader(filename, key):
    '''
    :param filename: name of json file and a key
    :return: a value for a searched key
    '''
    f = open(filename, encoding="utf8")
    data = json.loads(f.read())
    f.close()
    if type(data) == 'list':
        info = data[0]
    if type(data) == 'dict':
        info = data.pop('users')

if __name__ == '__main__':
    print("Now we gonna know everything about you! BUGAGA!")
    filename = input("enter name of json file: ")
    key = input("enter a key u search for: ")
    json_reader(filename, key)