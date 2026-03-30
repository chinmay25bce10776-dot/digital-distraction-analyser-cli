def get_valid_input(message):
    attempts = 0
    while True:
        if attempts >= 3:
            print("\nToo many invalid attempts. Exiting program.")
            exit()

        value = input(message)

        if value.isdigit():
            return int(value)
        else:
            print("Invalid input, please enter numbers only.")
            attempts += 1


# Main Program
name = input("Enter your name: ")

while True:
    print("\nHii,", name)
    print("Let's analyze your daily digital usage\n")

    # Taking inputs one by one
    yt = get_valid_input("Enter YouTube hours per day: ")
    insta = get_valid_input("Enter Instagram/Social Media hours per day: ")
    game = get_valid_input("Enter Gaming hours per day: ")
    sleep = get_valid_input("Enter Sleep hours: ")

    distraction = yt + insta + game

    print("\n--- Analysis Report ---")
    print("Total Digital Distraction:", distraction, "hours")

    if distraction >= 8:
        print("Productivity Level: Low")
        print("Suggestion: Reduce screen time and focus more on important tasks")
    elif distraction >= 4:
        print("Productivity Level: Medium")
        print("Suggestion: Try to balance screen time and productive work")
    else:
        print("Productivity Level: High")
        print("Suggestion: Keep maintaining your good habits")

    # Feedback section
    while True:
        feedback = input("\nWas this analysis helpful? (yes/no): ").lower()

        if feedback == "yes":
            print("I'm glad you liked it!")
            break
        elif feedback == "no":
            print("Thanks for your feedback, we will improve!")
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

    # Loop for reuse
    while True:
        again = input("\nDo you want to analyze again? (yes/no): ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("\nThank you for using the system!")
            exit()
        else:
            print("Invalid input, please enter 'yes' or 'no'.")


