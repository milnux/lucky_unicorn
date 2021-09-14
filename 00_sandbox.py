greeting = "Welcome to the Lucky Unicorn Game"
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "*" * len(greeting)

print()
print(top_bottom)
print(greeting)
print(top_bottom)
print()

greeting_2 = "Congratulations you got a Unicorn"
sides = "!" * 3

greeting_2 = "{} {} {}".format(sides, greeting_2, sides)

top_bottom_2 = "!" * len(greeting_2)

print()
print(top_bottom_2)
print(greeting_2)
print(top_bottom_2)
print()
