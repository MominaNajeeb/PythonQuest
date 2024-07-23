while True:
    n = int(input("Enter any number of your choice: "))
    modulus = n % 2

    if modulus != 0:
            print("Wierd")
    else:
         if n >= 2 and n <= 5:
            print("Not Wierd")

         elif n >= 6 and n <= 20:
            print("Wierd")

         elif n > 20:
            print("Not Wierd")

    