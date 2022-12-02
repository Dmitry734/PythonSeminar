def reader(filename):
    with open(filename, 'r+', encoding='utf-8') as myfile:
        return myfile.read()


'''
def reader(d):
    file = open('data', 'r')
    s = file.read()
    st = s.split('\n')
    list = []
    for i in st:
        list.append(i.split())
    print(d)
'''
