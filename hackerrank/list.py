list = [1, 2, 3, 4, 5]
n = int(input("Enter the number of commands you want to give: "))
for i in range(0, n):
    command = input("What's your command for the list? ")
    if command  == "insert":
        integer = int(input("Enter the integer to insert: "))
        index = int(input("Enter the index for integer: "))
        list.insert(index, integer)

    elif command == "append":
        integer = int(input("Enter the integer to append: "))
        list.append(integer)

    elif command == "remove":
        integer = int(input("Enter the integer to remove: "))
        
        if integer in list:
            list.remove(integer)
        else:
            print("Integer not found in the list. ")


    elif command == "print":
        print(list)

    elif command == "pop":
        index = int(input("Enter the index to pop: "))
        if index < len(list):
            list.pop(index)
        else:
            print("Index out of range. ")
        

    elif command == "sort":
        list.sort()

    elif command == "reverse":
        list.reverse()

    else:
        print("Please enter a valid command. ")