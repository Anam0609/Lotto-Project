# Anam Majikijela - Class 2
# Importing the datetime built-in module, to get the present date
import datetime
# prints the greeting to the game
print("Welcome to the lottery game!")

try:
    # try to check for errors first
    start_game = False
    # prompts the player for his/her name
    name = input("Enter your name: ")
    # prompts for the player's year of birth
    year = int(input("Enter your year of birth: "))
    # prompts for the player's month of birth
    month = int(input("Enter your month of birth: "))
    # prompts for the player's day of birth
    day = int(input("Enter your day of birth: "))

    # collects everything the user has filled in
    DOB = datetime.datetime(year, month, day)
    # subtracts the date of birth from the current date
    age = datetime.datetime.now() - DOB
    # the answer from subtracting the date of birth in days
    convert_days = int(age.days)
    # converting the days to years using floor division
    age_years = convert_days // 365
except Exception as e:
    # if there are errors, print them out
    print("An error occurred:", e)
else:
    # this will only execute when there are no errors
    if age_years < 18:
        print("You are not in within he legal age of playing!")
    else:
        # setting the start_game variable as true will make the game play
        start_game = True
        # will greet the player with his/her name and age
        print("Hello, " + name + ". You are " + str(age_years) + ". Ready to try your luck?")
