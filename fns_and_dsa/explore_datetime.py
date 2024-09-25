from datetime import datetime, timedelta


def display_current_datetime():
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    "%Y-%m-%d %H:%M:%S"
    print("Current date and time: ", str(current_date).split(".")[0])
    #Part 2: Calculate a Future Date
    number_of_days =  int(input("Enter the number of days to add to the current date: "))

    def calculate_future_date():
        future_date =  current_date + timedelta(days=number_of_days)

        print("Future date: ", future_date.strftime("%Y-%m-%d"))
    calculate_future_date()

display_current_datetime()