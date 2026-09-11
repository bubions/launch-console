user_name = input("What's your name?: ")
print(f"Welcome to the Launch Console, {user_name}!")

isRunning = True
while isRunning:
    print("")

    print("1. About me")
    print("2. My goals")
    print("3. Cat")
    print("4. Exit")

    user_choice = input("Pick an option 1-4: ")

    if user_choice == "1": # ABOUT ME
        print("I'm Raiyan, a sophmore at Vista Ridge High School.")
    elif user_choice == "2": # MY GOALS
        print("My goal is to ship my first real project this term.")
    elif user_choice == "3": # CAT
        print("  /\\      /\\")
        print(" /  \\____/  \\")
        print("| ___   ___ |")
        print("|/ | \\ / | \\|")
        print("|\\___/ \\___/|")
        print("|           |")
        print("|___________|")
    elif user_choice == "4": # EXIT
        print("Goodbye!")
        isRunning = False
    else:
        print("Not a valid option.")