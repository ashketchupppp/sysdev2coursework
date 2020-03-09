help_message = """The following is a list of valid inputs:

Help - display this message
Quit - exit the program
Restart - it does something?"""

welcome_message = "Welcome to the Stabbings search tool"

end_program = False

print("\n" + welcome_message)
print(help_message)

while not end_program:
    user_input = input(" > ")
    user_input = user_input.lower()
    print()
    if user_input == "Help":
        print(help_message) 
    elif user_input == "Restart":
        print("not sure what this is meant to do yet")
    elif user_input == "Quit":
        end_program = True
    else:
        print("That is not a valid command. Type 'help' for a list of command.")
