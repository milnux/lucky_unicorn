import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# testing loop to generate 20 tokens
for item in range(0, 100):
    chosen_num = random.randint(1, 100)

    # adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 >= chosen_num <= 40:
        chosen = "donkey"
        balance -= 1
    elif 41 >= chosen_num <= 70:
        chosen = "horse"
        balance -= 0.5
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

# output

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
    print()
    print()
    print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
    print("Final Balance: ${:.2f}".format())