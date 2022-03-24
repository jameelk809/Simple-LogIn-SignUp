import hashlib
import json

jsonFile = "record_dict.json"


def add_user(user, password):
    entry = {"name": user, "password": password}
    with open(jsonFile, "r") as file:
        data = json.load(file)
    data.append(entry)
    with open(jsonFile, "w") as file:
        json.dump(data, file, indent=4)


def print_user():
    with open(jsonFile) as file:
        data = json.load(file)
        for i in data:
            print(i['name'], i['password'])


def Signup():
    print("\nWelcome")
    username_list = []
    with open(jsonFile) as file:
        data = json.load(file)
        for i in data:
            username_list.append(i['name'])
    username = create_hash(input("Enter preffered username: "))
    if username in username_list:
        print('Username already exists, try another!')
        return
    passwrd = input("Enter password: ")
    retype = input("Retype password: ")
    if passwrd == retype:
        password = create_hash(passwrd)
        add_user(username, password)
        print('User created')
    else:
        print("Password didn't matched")


def Login():
    print('\nWelcome back!')
    username = create_hash(input("Username: "))
    password = create_hash(input("Password: "))
    with open(jsonFile) as file:
        data = json.load(file)
        for i in data:
            if i['name'] == username and i['password'] == password:
                print("Login Successful")


def Admin():
    pass


def create_hash(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()


def goodbye():
    print('\nGoodbye!!')
    exit(0)


def main():
    print("\nChoose:")
    print("1.   SignUp")
    print("2.   LogIn")
    print("3.   For Admin")
    print("4.   Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        Signup()
    elif choice == 2:
        Login()
    elif choice == 3:
        Admin()
    elif choice == 4:
        goodbye()
    else:
        print("Wrong Choice")


while True:
    main()

