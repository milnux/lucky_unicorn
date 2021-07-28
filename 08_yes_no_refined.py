# looping code
show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if they have played before
    show_instructions = input("Have you ever played this game before").strip().lower()

    # if they say yes, output 'program continues
    # if they say no, output 'display instructions'
    # if user puts unexpected code, display error message

    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    elif show_instructions == "no" or show_instructions == "n":
            print("Display instructions")

    else:
        print("<error> Please answer yes / no")
