shopping_list = []
def add_item(item):
    shopping_list.append(item)
    print(f"Added {item} to the shoppinglist.")

def remove_item(item):
    shopping_list.remove(item)
    print(f"Removed {item} from the shopping list.")

def view_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is empty.")

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

def main():
    while True:
        display_menu()

        user_option = int(input("Enter your choice (1, 2, 3, 4): "))

        if user_option == 1:
            item_name = input("Enter the name of the item: ").lower()
            add_item(item_name)
        elif user_option == 2:
            item_name = input("Enter the name of the item: ").lower()
            if item_name in shopping_list:
                remove_item(item_name)
            else:
                print(f"the item- {item_name} is not found.")
        elif user_option == 3:
            view_list()
        elif user_option == 4:
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
