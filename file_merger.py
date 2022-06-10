import os
def console():
    print(os.getcwd())
    print("enter 'p' to get into previous directory:")
    print("enter 'cd 'to change directory")
    print("enter 'ls' to list all directories ")
    while True:
        op = input("enter here:")
        if op == 'p':
            os.chdir('..')
        elif op == 'ls':
            print(os.listdir())
        elif op == 'cd':
            while True:
                print(os.listdir())
                d = input("enter the dir name:")
                if d in os.listdir():
                    os.chdir(os.path.join(os.getcwd(),d))
                    break
                elif d == 0:
                    break
                else:
                    print('command not found')
        elif op == '0':
            exit()
        else:
            print('re-enter:')
        print(os.getcwd())

console()