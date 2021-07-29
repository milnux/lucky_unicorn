# Functions go here...


# Main routine goes here...

error = "Please enter an whole number between 1 and 10"

valid = False
while not valid:
    # ask the question
    response = int(input("How much would you like to play with"))

    # if the amount is too low/ too high, give an error message
    if 0 < response <= 10:
        print("You have asked to play with ${}".format(response))

    else:
        print(error)
