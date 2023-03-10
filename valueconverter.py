def conv():

    def temp_conv():
        print("Which conversion would you like to choose? \n"
              "1. Celsius to Farenheit\n"
              "2. Farenheit to Celsius\n")
        choice = int(input("Now enter your choice: "))

        if choice == 1:
            temp = float(input("Enter the temperature in Celsius"))
            print(
                f"{temp} degree Celsius is equal to {(temp*9/5)+32} degree Farenheit. ")
        elif choice == 2:
            temp = float(input("Enter the temperature in Farenheit"))
            print(
                f"{temp} degree Farenheit is equal to {(temp-32)*5/9} degree Celsius. ")
        else:
            print("Invalid Input...")

    def leng_conv():

        print("Which conversion would you like to choose? \n"
              "1. Centimeter to Foot \n"
              "2. Foot to Centimeter \n"
              "3. Centimeter to Inches \n"
              "4. Inches to Centimeter \n")
        choice = int(input("Now enter your choice: "))

        if choice == 1:
            val = float(input("Enter the length in cm "))
            foot = val/30.48
            print(f"{val} cm is equal to {foot} foots/foot.")

        elif choice == 2:
            foot = float(input("Enter the length in foot "))
            cm = foot*30.48
            print(f"{foot} foot/s is equal to {cm} cm.")
        elif choice == 3:
            val = float(input("Enter the length in cm "))
            inches = val/2.54
            print(f"{val} cm is equal to {inches} inches/inch.")
        elif choice == 4:
            inches = float(input("Enter the length in inches "))
            cm = inches*2.54
            print(f"{inches} inch/s is equal to {cm} cm.")
        else:
            print("Invalid Input...")

    def weight_conv():
        print("Which conversion would you like to choose? \n"
              "1. Kilograms to Pounds \n"
              "2. Pounds to Kilograms\n")
        choice = int(input("Now enter your choice: "))

        if choice == 1:
            kg = float(input("Enter the weight in kgs: "))
            print(f"{kg} kg is equal to {kg*2.205} lbs.")
        elif choice == 2:
            lb = float(input("Enter the weight in lbs: "))
            print(f"{lb} lbs is equal to {lb/2.205} kg.")
        else:
            print("Invalid Input...")

    print("Welcome i can convert the following. \n"
          "1. Convert Temperature \n"
          "2. Convert Length \n"
          "3. Convert Weight \n")
    choice = int(input("Now state what would you like to do today? "))

    if choice == 1:
        temp_conv()
    elif choice == 2:
        leng_conv()
    elif choice == 3:
        weight_conv()
    else:
        print("Wrong input!")

conv()

while True:
    choice = input("Would you like to restart again y/n ?")
    if choice == "y":
        conv()
    elif choice == "n":
        print("Okay, have a nice day.")
        quit()
    else:
        print("Invalid arguement")

