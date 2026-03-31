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
       print("Suggestions:")
       print("• Limit social media usage to 1-2 hours per day")
       print("• Set a daily study/work schedule")
       print("• Keep your phone away while studying")
       print("• Try work for 25-minutes then 5-minutes break (Pomodoro technique)")
    elif distraction >= 4:
        print("Productivity Level: Medium")
        print("Suggestions:")
        print("• Reduce unnecessary screen time gradually")
        print("• Plan your day with clear goals")
        print("• Take short breaks instead of long scrolling sessions")
        print("• Focus on completing important tasks first")
    else:
       print("Productivity Level: High")
       print("Suggestions:")
       print("• Maintain your current routine")
       print("• Keep tracking your screen time regularly")
       print("• Try learning new skills in free time")
       print("• Stay consistent and avoid distractions")

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



