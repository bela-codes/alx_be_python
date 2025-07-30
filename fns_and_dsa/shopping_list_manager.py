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

def main():
    while True:
        print("\nShopping List Manager:")
        print("1. add an item")
        print('2. remove an item')
        print("3. view the list")
        print("4. exit")

        user_option = input("Enter your choice (1, 2, 3, 4): ")

        if user_option == "1":
            item_name = input("Enter the name of the item: ").lower()
            add_item(item_name)
        elif user_option == "2":
            item_name = input("Enter the name of the item: ").lower()
            if item_name in shopping_list:
                remove_item(item_name)
            else:
                print(f"the item- {item_name} is not found.")
        elif user_option == "3":
            view_list()
        elif user_option == "4":
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
