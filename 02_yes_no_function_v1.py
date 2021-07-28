

# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
        print("Program continues")

    elif show_instructions == "no" or show_instructions == "n":
            print("Display instructions")

    else:
        print("<error> Please answer yes / no")
# Main routine goes here...
show_instructions = yes_no("Have you ever played this game before")

print("You chose {}".format(show_instructions))
