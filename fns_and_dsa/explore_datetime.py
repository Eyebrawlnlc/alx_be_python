from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date():
    """Calculates and prints a future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future_date)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
