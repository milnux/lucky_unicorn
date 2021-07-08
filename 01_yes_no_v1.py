# ask the user if they have played before
show_instructions = input("Have you ever played this game before").lower()
# if they say yes, output 'program continues'
if show_instructions == "yes":
    print("Program continues")

# if they say no, output 'display instructions'

elif show_instructions == "no":
    print("display instructions")
# if thy type something other than yes or no 'print error'
else:
    print("<error> PLease type yes or no")
