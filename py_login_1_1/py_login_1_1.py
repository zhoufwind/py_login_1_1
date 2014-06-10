database = {}

def read():
    'Import file: \'test.txt\', createing user/password database.'
    f = open('test.txt', 'r')
    for line in f.readlines():
        str = line.split(',')
        name = str[0].lower()
        pwd = str[1].strip('\n')
        database[name] = pwd
    f.close()

def write(n):
    'If user enter incorrect password N times, adding user name into \'blockList.txt\'.'
    f = open('blockList.txt', 'a')
    f.writelines(n + '\n')
    f.close()

def lookup(n):
    'Check if user exist in the database, if exist, return user\'s password.'
    return database.get(n)

def checkBlock(name):
    f = open('blockList.txt','r')
    for line in f.readlines():
        if name == line.strip('\n'):    # blocklist contains user, block him immediately!
            return True
            break
        else:
            continue

def login(times):
    'Login function, first check if user exist in the database, then check if user in blocklist, then begin login process, block user if login failed 3 times'
    name = raw_input('Enter user name: ').lower()
    if lookup(name):    # Check if user exist in the database
        #print "Found the user!"
        if not checkBlock(name):    # Check if user have been blocked
            for i in range(times):      # Verify the user name and password
                pwd = raw_input('Enter Password: ')
                if pwd == database[name]:
                    login = True
                    break
                else:
                    login = False
                    print 'Password Incorrect!'
            if login:
                print 'Login Success!!\nWelcome!!'
            else:
                print 'Login Failed 3 times, block this account!!'
                write(name)     # Adding user into blockList
        else:
            print 'User have been blocked already!'
    else:
        print 'User isn\'t exist!!'

read()
login(3)