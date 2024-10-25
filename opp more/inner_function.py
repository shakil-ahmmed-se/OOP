def doube_decker():
    print('Starting the double decker')
    def inner_fun():
        print('inner function')
        return 3000
    return inner_fun    
    
# print(doube_decker())
# print(doube_decker()())

def do_something(work):
    print('start working')
    work()
    print('ending work')

# do_something(2)
# do_something('ami busy')

def coding():
    print('coding in python')

# do_something(coding)

def sleeping():
    print('sleeping and dreaming in python')
    
do_something(sleeping)