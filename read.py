#read

def file_reader():
    """
    This function reads data from text files

    Returns:
     data in form of list
    """
    try:
        inventory = open("inventory.txt", "r")

        # reading and storing information of each product(line) in a list
        products = inventory.readlines()
        inventory.close()
        return products
    except FileNotFoundError:
        print("FILE NOT FOUND!")
    except PermissionError:
        print("Error reading file")
