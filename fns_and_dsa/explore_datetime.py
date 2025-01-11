from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        # Prompt the user to enter a number of days
        days = int(input("Enter the number of days to add to the current date: "))
        # Get the current date
        current_date = datetime.now()
        # Calculate the future date
        # future_date = current_date + timedelta(days=days)
        future_date = current_date + timedelta(days=days)
        # Print the future date
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()
    print()  # For better readability
    # Part 2: Calculate a future date
    calculate_future_date()
