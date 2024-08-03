import quiz
import auth

print("******************************************************** WELCOME TO PYTHON QUEST! 🐍*******************************************************")
print("Welcome to Python Quest! 🐍 Test your Python skills with quizzes of varying difficulty levels—Easy, Medium, or Hard. Sign up or log in to track your progress, answer multiple-choice questions, and earn titles based on your score. Review your results, improve your knowledge, and enjoy the journey of mastering Python. Start your Python Quest today and level up your coding expertise!")

while True:
    start = int(input("1. LOGIN\n" + "2. SIGNUP\n" + "3. Choose one: "))

    if start == 1:
        auth.login()
        

    elif start == 2:
        auth.signup()        

    else:
        print("Invalid attempt! ")
