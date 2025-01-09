from shopping_list_manager import *

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item(shopping_list)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item(shopping_list)
        elif choice == '3':
            # Display the shopping list
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()