task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f'Reminder: {task} is a {priority} priority task that requires immediate attention today!')
        elif time_bound == "no":
            print(f'Note: {task} is a {priority} priority task but it does not immediate attention today!')

    case "medium":
        if time_bound == "yes":
            print(f'Reminder: {task} is a {priority} priority task that requires immediate attention today!')
        elif time_bound == "no":
            print(f'Note: {task} is a {priority} priority task but it does not immediate attention today!')
    case "low":
        if time_bound == "yes":
            print(f'Reminder: {task} is a {priority} priority task that requires immediate attention today!')
        elif time_bound == "no":
            print(f'Note: {task} is a {priority} priority task but it does not immediate attention today!')

