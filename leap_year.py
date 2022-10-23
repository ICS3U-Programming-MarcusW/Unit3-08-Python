#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 19th, 2022
# This program asks the user to enter a year
# It then displays if the year they inputted is a leap year
# It also uses a try catch for any errors
import random


def main():
    # declare variable
    # get the users input (any year)
    user_year_input_string = input("Enter a year: ")
    # use a try catch to ensure user properly enters a year
    try:
        # convert the input form a string to an integer
        user_year_input_int = int(user_year_input_string)
        # if it is evenly divisible by 4
        if user_year_input_int % 4 == 0:
            # if it is evenly divisible by 100
            if user_year_input_int % 100 == 0:
                # if it is evenly divisible by 400
                if user_year_input_int % 400 == 0:
                    print("This is a leap year")
                else:
                    print("This is not a leap year")
            else:
                print("This is a leap year.")
        else:
            print("This is not a leap year.")
    # tell the user they incorrectly inputted a year
    except Exception:
        print("Please enter a valid year.")


if __name__ == "__main__":
    main()
