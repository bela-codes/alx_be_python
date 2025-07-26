description = input("Enter tasks description: ")
priority = input("In what level would you you describe the priority? (high/medium/low): ").lower()
time_bound = input("Is it time bounded? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{description}' is a highly priority task that requires immediate attention today!")
        else:
            print(f"'{description}' should be finished as soon as you got time.")
    case "medium":
        if time_bound == "yes":
            print(f"'{description}' is a Good idea to finish it as soon as possible.!")
        else:
            print(f"'{description}' should be finished as soon as you got time.")
    case "low":
        if time_bound == "yes":
            print(f"'{description}' is a low priority task that requires immediate attention if you don't have anything to do!")
        else:
            print(f"'{description}' sis a low priority task. Consider completing it when you have free time")
    case _:
        print("Please choose a priority level from the given choices.")