import quiz
username1 = "momina"
username2 = "mahnoor"
password1 = "najeeb"
password2 = "iqbal"

def signup():
    new_username = input("Enter username: ")
    new_password = input("Enter password: ")
    print("Your account has been created! ")
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
    
        if username == new_username and password == new_password:
            print("Let's get started: ")
            quiz.get_started()
           
        else:
            print("Incorrect username or password! ")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == username1 and password == password1:
        print("Welcome back!")
        print("Let's get started!")
        quiz.get_started()
    elif username == username2 and password == password2:
        print("Welcome back!")
        print("Let's get started!")
        quiz.get_started()
    else:    
        print("Incorrect username or password! ")
        print("Create account: ")
        signup()
