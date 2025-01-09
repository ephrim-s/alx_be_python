
shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' added successfully.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed successfully.")
    else:
        print(f"'{item}' is not available in your shoping list")

def view_list(shopping_list):
    if shopping_list:
        print("Your shoping list: ")
        for item in shopping_list:
            print(f"* {item}")
    else:
        print("Your shoping list is empty")
