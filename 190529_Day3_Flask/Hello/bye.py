def hello(func):
    print('hihi')
    func() #bye실행한것과 같음
    print('hihi')

@hello
def bye():
    print('bye bye')


bye()