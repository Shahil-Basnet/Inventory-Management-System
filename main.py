import operations as op
import read as r


def main_program():
    """
    Run and call all required functions

    Raises:
        ValueError: If string is given as input instead of integer
        FileNotFoundError: If the file does not exist when reading.
    """
    print("Welcome to WeCare system ADMIN.")
    while True:
        print("\nWhat would you like to do?\n")
        print("[1] Sell product\n[2] Restock product\n[3] Exit system.")
        admin_choice = input("Enter your choice:")
        print()
        try:
            if admin_choice == "1":
                op.sell_item(op.details_gen(r.file_reader()))
                continue
            elif admin_choice == "2":
                op.buy_item(op.details_gen(r.file_reader()))
                continue
            elif admin_choice == "3":
                print("Have a nice day ADMIN!")
                break
            else:
                print("Invalid choice. Please choose again!")
        except FileNotFoundError:
            print("File not found!")


main_program()
