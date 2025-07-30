from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date

current_time = display_current_datetime()
print(f"Current date and time: {current_time}")


days = int(input("Enter the number of days to add: "))

def calculate_future_date(days):
    future_date = datetime.now() + datetime.timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date


future_date = calculate_future_date(days)
print(f"Future date: {future_date}")