# Anam Majikijela - Class 2
# importing everything from the player age module
from player_age import *
# Importing the random built-in module, to get the randint module that will choose random integer
from random import randint
# importing the doctest from the custom doctest module
from doctest import *


# create function to write to file
def write_to_file(name, age_years, correct_num, my_numbers, lotto_numbers):
    # write these to a file
    with open("lotto_results.txt", "a+") as file:
        file.write("Player name: " + str(name) + "\n")
        file.write("Player age: " + str(age_years) + "\n")
        # check if user falls under the categories
        if correct_num > 1:
            cat = correct_num
        else:
            cat = None
        file.write("Category: " + str(cat) + "\n")
        file.write("Your numbers: " + str(my_numbers) + "\n")
        file.write("Winning numbers: " + str(lotto_numbers) + "\n")
        if correct_num > 1:
            # get the correct prize accordingly
            prize = check_prize(correct_num)
            file.write("You won R" + str(prize) + " congratulation!")
        else:
            file.write("Unfortunately you didn't win any prize, better luck next time")
        # this is just a blank line to keep the results separate
        file.write("\n\n")

    # prizes to be won
    prizes = {
        6: "10 000 000.00",
        5: "8 584.00",
        4: "2 384.00",
        3: "100.50",
        2: "20.00"
    }
    # if the player gets 0 or 1 correct
    if correct_num < 2:
        return 'Nothing'  # the player receives nothing
    else:
        # else the player gets a prize depending on how many numbers he/she got correct
        return prizes.get(correct_num)


# this if statements prevents the game from starting in case there are errors
if start_game == True:
    # variable to store the randint
    new_num = 0
    # list for the lotto numbers
    lotto_numbers = []
    # list for the player's numbers
    my_numbers = []
    correct_num = 0
    # The while loop will create six lotto numbers
    while len(lotto_numbers) < 6:
        # lotto numbers will be from 1 - 49 or any number in between
        new_num = randint(1, 49)
        # prevents the computer from using the same number twice
        if new_num not in lotto_numbers:
            # appends new number to the list
            lotto_numbers.append(new_num)

    # sort the numbers to ascending order
    lotto_numbers.sort()

    # The while loop will loop the player's numbers
    while len(my_numbers) < 6:
        # this will check the input for any errors
        try:
            # will allow the player to input his/her six numbers
            new_num = int(input("Please enter number between 1 - 49: "))
        except Exception as e:
            # if there are errors, the program won't stop it will continue
            print("An error occurred:", e)
        else:
            # this part will execute only when there are no errors
            # prevents the player from using the same number twice
            if new_num not in my_numbers:
                # checks if the number is less than 1 or more than 49
                if 1 <= new_num <= 49:
                    # if its more than 1 then it will be appended but if its less than 49 it will be appended also
                    my_numbers.append(new_num)
                    # if the player's number matches the lotto number
                    if new_num in lotto_numbers:
                        # then the correct number increases by 1
                        correct_num += 1
                else:
                    # will be printed if the number is less than 1 or is above 49
                    print("The number is out of range")
            else:
                # if you repeat a number, this will be printed
                print("You have already guessed this number")

    # sort the player's numbers to ascending order
    my_numbers.sort()

    # call the function that will write to file
    write_to_file(name, age_years, correct_num, my_numbers, lotto_numbers)

    # the results has been printed to file and on screen
    print("Player name: " + str(name) + "\n")
    print("Player age: " + str(age_years) + "\n")
    # check if user falls under the categories
    if correct_num > 1:
        cat = correct_num
    else:
        cat = None
    print("Category: " + str(cat) + "\n")
    print("Your numbers: " + str(my_numbers) + "\n")
    print("Winning numbers: " + str(lotto_numbers) + "\n")
    if correct_num > 1:
        # get the correct prize accordingly
        prize = check_prize(correct_num)
        print("You won R" + str(prize) + " congratulation!")
    else:
        # printed when the player has lost or only got 1 correct answer!
        print("Unfortunately you didn't win any prize, better luck next time")
        # Automatically prints results to the lotto_results.txt
    print("Your results has been printed to file")
else:
    # prints when there's an error
    print("The game did't start")
