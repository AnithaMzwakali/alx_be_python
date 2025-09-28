# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    """Calculate a future date by adding a user-specified number of days."""
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()

