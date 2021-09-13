import random
# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("<error> Please answer yes / no")


def instructions():
    print(" ******** How To Play ********")
    print()
    print(" ***************************** \n     the rules of the game \n             go here \n *****************************")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low/ too high, give an error message
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine goes here...

played_before = yes_no("Have you ever played this game before")

if played_before == "no":
    instructions()
print()
print("Program continues")
print()
# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))
print()
balance =  how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5
    # user gets a unicorn(+$4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # If the random # is between 6 and 36
    # user gets a donkey (-$1 from balance)
    elif 6 >= chosen_num <= 40:
        chosen = "donkey"
        balance -= 1

    # The token is either a horse or zebra...
    # in both cases, -$0.50 from the balance
    else:
        # if the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
        # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:

        play_again = input("Press Enter to play again, or press 'xxx' to quit")

print()
print("Final Balance", balance)
