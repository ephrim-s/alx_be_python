from datetime import datetime, timedelta

def display_current_datetime():
    
    current_date = datetime.now()
    
    print("Current Date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:        
        days = int(input("Enter the number of days to add to the current date: "))
        
        current_date = datetime.now()
        
        future_date = current_date + timedelta(days=days)
        
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    
    display_current_datetime()
    print()     
    calculate_future_date()
