import csv


def split_and_print(text):
        strings = text.split(",")
        for string in strings:
            substrings = string.split("||")
            for substring in substrings:
                print(substring)


def easy_level():
    score = 0
    count_easy= 0
    with open("quiz_data.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for row in reader:
            if count_easy<10:
                split_and_print(row[0])
                question = input("Your answer: ")
                if question == row[1]:
                    print("Your answer is correct! ✅\n", "You earned 2 points! 🎉")
                    score += 2
                    print("Your current score:", score)
                
                else:
                    print("Oops, that's not right! ❌")
                    print("Your current score:", score)

                count_easy += 1    

            else:
                break    

    print("You earned:", str(score), "points")
    if score >= 18 and score <=20:
        print("You are a Superstar of Python!")

    elif score >= 14 and score <=17:
        print("You are a Star Performer!")

    elif score >=10 and score <=13:
        print("You are a Solid Achiever!")
        
    elif score >= 6 and score <=9:
        print("You are a Rising Star of Python!")  

    else:
        score >= 18 and score <=20
        print("You are a Learning Explorer of Python")
    print("Wanna play again? ")


def medium_level():
    score = 0
    count_medium = 0
    with open("quiz_data.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            if count_medium>10 and count_medium<21:
                split_and_print(row[0])
                question = input("Your answer: ")
                if question == row[1]:
                    print("Your answer is correct! ✅\n", "You earned 2 points! 🎉")
                    score += 2
                    print("Your current score:", score)
                
                else:
                    print("Oops, that's not right! ❌")
                    print("Your current score:", score)

                count_medium += 1    

            else:
                count_medium += 1 

    print("You earned:", str(score), "points")
    if score >= 18 and score <=20:
        print("You are a Superstar of Python!")

    elif score >= 14 and score <=17:
        print("You are a Star Performer!")

    elif score >=10 and score <=13:
        print("You are a Solid Achiever!")
        
    elif score >= 6 and score <=9:
        print("You are a Rising Star of Python!")  

    else:
        score >= 18 and score <=20
        print("You are a Learning Explorer of Python")
    print("Wanna play again? ")
    


def hard_level(): 
    score = 0
    count_hard = 0 
    with open("quiz_data.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)      
        for row in reader:
            if count_hard>20 and count_hard<31:
                split_and_print(row[0])
                question = input("Your answer: ")
                if question == row[1]:
                    print("Your answer is correct! ✅\n", "You earned 2 points! 🎉")
                    score += 2
                    print("Your current score:", score)
                
                else:
                    print("Oops, that's not right! ❌")
                    print("Your current score:", score)

                count_hard += 1    

            else:
                count_hard += 1    

    print("You earned:", str(score), "points")
    if score >= 18 and score <=20:
        print("You are a Superstar of Python! 🌟")

    elif score >= 14 and score <=17:
        print("You are a Star Performer! 🌟")

    elif score >=10 and score <=13:
        print("You are a Solid Achiever! ⭐")
        
    elif score >= 6 and score <=9:
        print("You are a Rising Star of Python! ⭐")  

    else:
        score >= 18 and score <=20
        print("You are a Learning Explorer of Python! ⭐")
    print("Wanna play again? ")



def get_started():
    
    difficulty = int(input("Select difficulty level:\n" + "1.Easy\n" + "2.Medium\n" + "3.Hard\n"))
    
    if difficulty == 1:
        easy_level()

    elif difficulty == 2:
        medium_level()

    elif difficulty == 3:
        hard_level()        

    else:
        print("Please enter a valid difficulty level! ")   




 

