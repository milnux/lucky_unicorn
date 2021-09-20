import random


# Functions go here...


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("<error> Please answer yes / no")


def instructions():
    print()
    print(statement_generator("How To Play", "*"))
    print()
    print("Choose a starting amount (minimum $1, maximum $10)")
    print()
    print("Then press <enter> to play. You will either get a Horse, a Zebra, a Donkey or a Unicorn")
    print()
    print("It costs $1 per round. Depending on your prize you might win some of your money back.")
    print()
    print("Here's the payout amounts...")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1)")
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


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here...
statement_generator("Welcome to Lucky Unicorn", "~")
played_before = yes_no("Have you ever played this game before?")

if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))
balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    round_state = "Round #{}".format(rounds_played, "*")
    statement_generator(round_state, "*")

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5
    # user gets a unicorn (+$4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        prize_decoration = "!"
        balance += 4

    # If the random # is between 6 and 36
    # user gets a donkey (-$1 from balance)
    elif 6 >= chosen_num <= 36:
        chosen = "Donkey"
        prize_decoration = "D"
        balance -= 1

    # The token is either a horse or zebra...
    # in both cases, -$0.50 from the balance
    else:
        # if the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "Horse"
            prize_decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "Zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(outcome, prize_decoration)

    if play_again == "xxx":
        print("Sorry you have run out of money")
        print()
        print("Thanks for playing the Lucky Unicorn Game")

    elif balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")

    else:
        print()
        play_again = input("Press Enter to play again, or type 'xxx' to quit")

print()
print("Final Balance ${:.2f}".format(balance))
print()
print("Thanks for playing the Lucky Unicorn Game")
