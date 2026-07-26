'''Hello Github! I started learning about programming from 0, just 4 days ago. This is my first project.
   It has still long way to go but i didnt learn them yet, i dont wanted to copy-paste ai writed codes, instead
   understand the logic behind, so...this is almost all i know for now'''
# for calculator we need to set first three parameters
# two for numbers and one for operator
# then we should set elif for each type of operator
# but i learned the match - case system, its better for use in calculator

first_number = float(input("Enter a number "))
operator = (input("")).strip()
second_number = float(input("Enter a number "))

match operator:
    case "+":
        print(f"{first_number + second_number:,.3f}")

    case "-":
        print(f"{first_number - second_number:,.3f}")

    case "x" | "*":
        print(f"{first_number * second_number:,.3f}")

    case "/":
        if second_number == 0:
            print("Error! Can't divide with 0")
        else:
            print(f"{first_number / second_number:,.3f}")
       
    case "//":
        if second_number == 0:
            print("Error! Can't divide with 0")
        else:
            print(f"{first_number // second_number:,.3f}")
        

    case "**":
        print(f"{first_number ** second_number:,.3f}")

# i also added error if user type number or word instead operator
# But somehow if user try to divide with 0 program will shut down so we dont want it
# i added if and else inside case divide for divide zero protection
# i also added :.3f to round the long float numbers and , between each 3 number to mark
# this way it would easier to read
