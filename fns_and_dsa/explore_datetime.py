#Working with datetime
from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in the format YYYY-MM-DD HH:MM:SS."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """Calculates and displays the future date after adding a specified number of days."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"The date after {days_to_add} days will be: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

# Main program execution
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
