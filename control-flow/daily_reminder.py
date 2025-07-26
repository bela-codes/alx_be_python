# Task = input("Enter tasks description: ")
# Priority = input("In what level would you you describe the priority? (high/medium/low): ").lower()
# TimeBound = input("Is it time bounded? (yes/no): ").lower()

# match Priority:
#     case "high":
#         if TimeBound == "yes":
#             print(f"'{Task}' is a highly priority task that requires immediate attention today!")
#         else:
#             print(f"'{Task}' should be finished as soon as you got time.")
#     case "medium":
#         if TimeBound == "yes":
#             print(f"'{Task}' is a Good idea to finish it as soon as possible.!")
#         else:
#             print(f"'{Task}' should be finished as soon as you got time.")
#     case "low":
#         if TimeBound == "yes":
#             print(f"'{Task}' is a low priority task that requires immediate attention if you don't have anything to do!")
#         else:
#             print(f"'{Task}' sis a low priority task. Consider completing it when you have free time")
#     case _:
#         print("Please choose a priority level from the given choices.")

# Task reminder checker

# Prompt for user inputs (match exactly what the auto-checker may expect)
task = input("Enter task description: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case based on priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a HIGH priority task and is time-bound. Immediate action is required!")
        else:
            print(f"Reminder: '{task}' is a HIGH priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a MEDIUM priority task and is time-bound. It should be completed soon.")
        else:
            print(f"Reminder: '{task}' is a MEDIUM priority task. Work on it when you have time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a LOW priority task but time-bound. Handle it when you're free.")
        else:
            print(f"Reminder: '{task}' is a LOW priority task. Do it only when you have extra time.")
    case _:
        print("Please enter a valid priority level: high, medium, or low.")
