#operations
import write as fw

# store the read data in a dictionary with auto incremented id as key and the list of details of products as values
def details_gen(data_file):
    """
    This function stores the read data in a dictionary.

    Args:
    data_file:Dictionary containing product inventory where:
            - Key (int): Product ID (auto-incremented)
            - Value (list): Product details in format [name, brand, stock, price, country]

    Returns:
    A dictionary with keys as IDs from 1-number of items and list of details of product as values.
    """
    # declaring an empty set/dictionary to hold product details
    try:
        product_list = {}
        # integer
        product_id = 0
        if data_file is None:
            raise ValueError()
        for product in data_file:
            # unique id for each product
            product_id += 1
            product_list[product_id] = product.replace("\n", "").split(",")
        return product_list
    except ValueError:
        print("Invalid data provided")



def display_info(product_info, mode):
    """
    Displays product information in a formatted table.

    Args:
    productInfo (dict): A dictionary where keys are product IDs and values are lists
    in the format [name, brand, stock, price, country].
    mode (str): A mode to differentiate between buying nd selling.
    """
    # to draw the ______  lines 
    print("_"*135)
    # names for each column
    print("|    ID\t| NAME\t\t\t| BRAND\t\t\t| STOCK\t\t\t| PRICE\t\t| COUNTRY\t|")
    # to draw the ¯¯¯¯¯¯¯¯  lines 
    print("\u00AF"*192)
    # loop to display the products in a table format
    try:
        if product_info is None:
            raise ValueError()
        for prod_id, product in product_info.items():
            print("|    "+str(prod_id), end="\t| ")
            # these conditions are set so that tab spaces are given according to their length for proper formatting

            # for name column
            if len(product[0]) <= 8:
                print(product[0], end="        \t\t| ")
            elif len(product[0]) >= 18:
                print(product[0], end="\t| ")
            else:
                print(product[0], end="\t\t| ")

            # for brand column
            if len(product[1]) <= 8:
                print(product[1], end="        \t\t|")
            else:
                print(product[1], end="\t\t|")

            # for stocks column
            print(product[2], end="\t\t\t|")

            # for price column
            if mode.lower() == "sell":
                print(str(int(product[3])*2), end="\t\t|")
            else:
                print(product[3], end="\t\t|")

            # for country column
            if len(product[4]) < 8:
                print(product[4], end="\t\t|")
            else:
                print(product[4], end="\t|")
            # new line after each list is finished
            print()

        # to draw the ¯¯¯¯¯¯¯¯  lines at last
        print("\u00AF"*192)
    except ValueError:
        print("INVALID DATA")


def sell_item(data_dict):
    """
    Handles the product selling process including inventory updates and invoice generation.

    This function allows the admin to sell products by:
    1. Displaying available products
    2. Accepting product selection and quantity input
    3. Updating inventory levels
    4. Generating purchase invoices

    Args:
        data_dict (dict): Dictionary containing product inventory where:
            - Key (int): Product ID (auto-incremented)
            - Value (list): Product details in format [name, brand, stock, price, country]

    Raises:
        ValueError: If input data is invalid or data_dict is None

    Side Effects:
        - Modifies inventory.txt with updated stock levels
        - Creates new invoice file for each purchase transaction
    """
    print("\t\t\t\t\t\t\t AVAILABLE PRODUCTS")
    # list to store different items/ works as a cart
    user_items = []
    available_products = data_dict
    display_info(available_products, "sell")
    try:
        if available_products is None:
            raise ValueError()
        while True:
            item_details = []
            while True:
                try:
                    product_id = int(input("Enter ID of the product: "))
                    if product_id <= 0 or product_id > len(available_products):
                        print("Please enter valid id!")
                        continue
                    else:
                        product_brand = available_products[product_id][1]
                        product_name = available_products[product_id][0]
                        available_quantity = int(available_products[product_id][2])
                        price_per_item = int(available_products[product_id][3]) * 3
                        if available_quantity == 0:
                            print("The product is out of stock!")
                            continue
                        print("Selected item: ", product_name,"  ||  Stock available: ", available_quantity, "  ||  Price per unit: ", price_per_item)
                        break
                except ValueError:
                    print("Please enter a valid number!")
            while True:
                try:
                    requested_quantity = int(input("Enter number of quantity: "))
                    free_items = requested_quantity // 3
                    actual_quantity = requested_quantity + free_items
                    if actual_quantity > available_quantity:
                        print("The requested quantity is greater than available stock")
                        continue
                    elif requested_quantity <= 0:
                        print("Please enter a value greater than 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Please enter valid quantity!")
            print("The total quantity of", product_name, ":", str(actual_quantity), "Free items:", str(free_items))
            total_price = requested_quantity * price_per_item
            print("The total price is: ", total_price)
            item_details.append(product_name)
            item_details.append(product_brand)
            item_details.append(str(actual_quantity))
            item_details.append(str(price_per_item))
            item_details.append(str(total_price))

            user_items.append(item_details)
            updated_stock = available_quantity - actual_quantity
            available_products[product_id][2] = str(updated_stock)
            fw.file_writer_products(available_products)
            confirmation = input("Add another item?(Type Y or N): ").lower()
            if confirmation == "n":
                break
            else:
                continue
        input("Press enter to generate invoice.")
        fw.file_writer_invoice(user_items, "sell")
    except ValueError:
        print("INVALID DATA")


def buy_item(data_dict):
    """Handles the product restocking process including inventory updates and invoice generation.

    This function allows the admin to restock products by:
    1. Displaying available products
    2. Accepting product selection and quantity input
    3. Updating inventory levels
    4. Generating purchase invoices

    Args:
        data_dict (dict): Dictionary containing product inventory where:
            - Key (int): Product ID (auto-incremented)
            - Value (list): Product details in format [name, brand, stock, price, country]

    Raises:
        ValueError: If input data is invalid or data_dict is None

    Side Effects:
        - Modifies inventory.txt with updated stock levels
        - Creates new invoice file for each purchase transaction
        """
    print("\t\t\t\t\t\t\t AVAILABLE PRODUCTS")
    # list to store different items/ works as a cart
    bought_items = []
    # accessing the products
    available_products = data_dict
    display_info(available_products, "buy")
    try:
        if available_products is None:
            raise ValueError()
        while True:
            # list to store details of bought items : [name, brand, quantity, unit price, total price]
            item_details = []

            while True:
                try:
                    product_id = int(input("Enter ID of the product to restock: "))
                    if product_id <= 0 or product_id > len(available_products):
                        print("Please enter valid id!")
                        continue
                    else:
                        product_brand = available_products[product_id][1]
                        product_name = available_products[product_id][0]
                        available_quantity = int(available_products[product_id][2])
                        price_per_item = int(available_products[product_id][3])
                        print("Selected item:", product_name, "||In Stock:", available_quantity, "||Price per unit:", price_per_item)
                        break
                except ValueError:
                    print("Please enter a valid number!")

            while True:
                try:
                    requested_quantity = int(input("Enter number of quantity: "))
                    if requested_quantity <= 0:
                        print("Please enter a value greater than 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Please enter valid quantity!")

            print("The total quantity of", product_name, ":", str(requested_quantity))
            total_price = requested_quantity * price_per_item
            print("The total price is: ", total_price)
            print("Successfully restocked: ", product_name, "Restocked quantity: ", str(requested_quantity))

            item_details.append(product_name)
            item_details.append(product_brand)
            item_details.append(str(requested_quantity))
            item_details.append(str(price_per_item))
            item_details.append(str(total_price))
            bought_items.append(item_details)
            updated_stock = available_quantity + requested_quantity
            available_products[product_id][2] = str(updated_stock)
            fw.file_writer_products(available_products)
            confirmation = input("Add another item?(Type Y or N): ").lower()
            if confirmation == "n":
                break
            else:
                continue
        input("Press ENTER to generate invoice")
        fw.file_writer_invoice(bought_items, "buy")
    except ValueError:
        print("INVALID DATA")


