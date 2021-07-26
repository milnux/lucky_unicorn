# looping code
show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if they have played before
    show_instructions = input("Have you ever played this game before").strip().lower()

    # if they say yes, output 'program continues
    if show_instructions == "yes":
        print("program continues")

    elif show_instructions == "y":
        print("Program continues")

    # if they say no, output 'display instructions'
    elif show_instructions == "no":
        print("Display instructions")

    elif show_instructions == "n":
        print("display instrucions")

    # if user puts unexpected code, display error message
    else:
        print("Please answer yes / no")
