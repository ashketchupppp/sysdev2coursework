def main():
    help_message = """The following is a list of valid inputs:
    Help - display this message
    Quit - exit the program
    Restart - restarts the program from the beginning"""

    welcome_message = "Welcome to the Stabbings search tool"

    end_program = False

    print("\n" + welcome_message)


    while not end_program:
        user_input = input(" > ")
        user_input = user_input.lower()
        print()
        if user_input == "help":
            print(help_message) 
        elif user_input == "restart":
            main()
        elif user_input == "quit":
            end_program = True
        else:
            print("That is not a valid command. Type 'help' for a list of command.")

if __name__ == '__main__':
    main()

