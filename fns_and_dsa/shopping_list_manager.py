def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            break
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            break
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
        elif choice == '3':
            # Display the shopping list
            break
            print("Shopping List:")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()