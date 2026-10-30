print("Welcome to My Calculator!")
try:
   firs = input("Enter a   first number: ")
   first = float(firs)
   oprators = input("Enter (+,-,*,/,%)")
   secon = input("Enter a second number: ")
   second = float(secon)
except ValueError:
    print("Enter a number.")
    exit()

while True:
    
    if oprators == '+':
         number = first + second
         print(first, "+", second, "=", number)
    elif oprators == "-":
         number = first - second
         print(first, "-", second, "=", number)
    elif oprators == "*":
        number = first * second
        print(first, "*", second, "=", number)
    elif oprators == "%":
         if second == 0:
            print("zero is not allowed.")
         else:
           number = first % second
           print(first, "%", second, "=", number)
    elif oprators == "/":
        if second == 0:
            print("Number cannot divide by zero")
        else:
            number = first / second
            print(first, "/", second, "=", number)
    else:
        print("Invalid operation.")
    while True:
     ask = input("DO you want to perform another calculation? (y/n)")
     if ask == "y" or ask == "Y":
         try :
          firs = input("Enter a first number ")
          first = float(firs)
          oprators = input("Enter (+,-,*,/,%)")
          secon = input("Enter a second number ")
          second = float(secon)

         except ValueError:
          print("Enter a number.")
          exit()
         break
     elif ask == 'n'or ask == "N":
        print("Thank you for using my calculator!")
        exit()
     else:
        print("Please enter only y or no")