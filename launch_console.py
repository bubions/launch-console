user_name = input("What's your name?: ")
print(f"Welcome to the Launch Console, {user_name}!")

isRunning = True
while isRunning:

    print("1. About me")
    print("2. My goals")
    print("3. Cat")
    print("4. Exit")

    user_choice = input("Pick an option 1-4: ")

    if user_choice == "1": # ABOUT ME
        pass
    elif user_choice == "2": # MY GOALS
        pass
    elif user_choice == "3": # CAT
        pass
    elif user_choice == "4": # EXIT
        print("Goodbye!")
        isRunning = False
    else:
        print("Not a valid option.")