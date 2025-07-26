Task = input("Enter tasks description: ")
Priority = input("In what level would you you describe the priority? (high/medium/low): ").lower()
TimeBound = input("Is it time bounded? (yes/no): ").lower()

match Priority:
    case "high":
        if TimeBound == "yes":
            print(f"'{Task}' is a highly priority task that requires immediate attention today!")
        else:
            print(f"'{Task}' should be finished as soon as you got time.")
    case "medium":
        if TimeBound == "yes":
            print(f"'{Task}' is a Good idea to finish it as soon as possible.!")
        else:
            print(f"'{Task}' should be finished as soon as you got time.")
    case "low":
        if TimeBound == "yes":
            print(f"'{Task}' is a low priority task that requires immediate attention if you don't have anything to do!")
        else:
            print(f"'{Task}' sis a low priority task. Consider completing it when you have free time")
    case _:
        print("Please choose a priority level from the given choices.")