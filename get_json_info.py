import json

def json_reader(filename, key):
    '''
    :param filename: name of json file and a key
    :return: a value for a searched key
    '''
    f = open(filename, encoding="utf8")
    data = json.loads(f.read())
    f.close()
    if isinstance(data, list):
        info = data[0]
        answer = info.pop(key)
        return answer
    if isinstance(data, dict) and key == 'users':
        return data.pop('users')
    if isinstance(data, dict):
        info = data.pop('users')
        print(type(info))
        print(len(info))
        for i in info:
            answer = i.pop(key)
            print(answer)

if __name__ == '__main__':
    print("Now we gonna know everything about you! BUGAGA!")
    filename = input("enter name of json file: ")
    while True:
        key = input("enter a key u search for(or type exit to out): ")
        if key == "exit":
            break
        print(json_reader(filename, key))