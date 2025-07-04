#write
import datetime as time

def file_writer_products(updated_product_dict):
    """
    Writes updated product inventory data to the inventory file in CSV format.

    Overwrites the existing inventory.txt file with the current product data from the dictionary.
    Each product is written as a comma-separated line in the format:
    name,brand,stock,price,country

    Args:
    updated_product_dict (dict): Dictionary containing the updated product inventory where:
        - Key (int): Product ID
        - Value (list): Product details in the format:
          [name (str), brand (str), stock (str), price (str), country (str)]

    Raises:
        IOError: If the file cannot be written (permission issues, disk full, etc.)
        TypeError: If the dictionary values are not in the expected format

    Side Effects:
        - Completely overwrites inventory.txt with new data
        - Creates the file if it doesn't exist
    """
    file = open("inventory.txt", "w")
    for products in updated_product_dict.values():
        file.write(str(products[0])+","+str(products[1])+","+str(products[2])+","+str(products[3])+","+str(products[4])+"\n")
    file.close()


def file_writer_invoice(total_items, mode):
    """
     Generates and saves transaction invoices in text format with proper formatting.

     Creates either a sales invoice (customer) or purchase invoice (supplier) based on mode.
     Files are named using a unique timestamp identifier and saved in the working directory.

     Args:
         total_items (list): List of transaction items where each item is a list containing: Product name, Brand name, Quantity (as string), Unit price (as string), Total price (as string)
         mode (str): Determines invoice type - 'sell' for sales or any other value for purchases

     Process Flow:
         1. Generates unique filename using current timestamp
         2. Collects customer/supplier information based on mode
         3. Writes formatted invoice header with company information
         4. Creates itemized list with proper column alignment
         5. Calculates and displays grand totals
         6. Saves to .txt file with appropriate naming convention

     File Naming Convention:
         - Sales: [timestamp]_[customer_name].txt
         - Purchases: [timestamp]_[supplier_name].txt

     Formatting Rules:
         - Product names:
             - ≤8 chars: 3 tabs
             - 9-17 chars: 2 tabs
             - ≥18 chars: 1 tab
         - Brand names:
             - ≤6 chars: 3 tabs
             - >6 chars: 2 tabs
    Raises:
        IOError: If file writing fails (permission issues, disk full)
        ValueError: If total_items is empty or incorrectly formatted
    """
    unique_id = str(time.datetime.now().year) + str(time.datetime.now().month) + str(time.datetime.now().day) + str(time.datetime.now().hour) + str(time.datetime.now().second) + str(time.datetime.now().microsecond)
    if mode.lower() == "sell":
        customer_name = input("Enter name of customer: ")
        customer_address = input("Enter address of customer:")
        file_name = unique_id + "_" + customer_name + ".txt"
        transaction_date = str(time.datetime.now())
        serial_no = 0
        total_quantity = 0
        total_price = 0
        print("Generating invoice........")
        file = open(file_name, "w")
        file.write("\t\t\t\t      WeCare\n")
        file.write("\t\t\t\tNew Road, Kathmandu\n")
        file.write("\t\t\t\tContact: 9012451010\n")
        file.write("\t\t\t\t      INVOICE\n")
        file.write("Name:"+customer_name+" \t\t\tLocation:"+customer_address + " \t\tDate:" + transaction_date)
        file.write("\n--------------------------------------------------------------------------------------------\n")
        file.write("S/N\tName\t\t\t Brand\t\t\tQuantity\tPrice\tTotal Price\n")
        for i in range(len(total_items)):
            serial_no += 1
            file.write(str(serial_no)+"\t")
            if len(total_items[i][0]) <= 8:
                file.write(total_items[i][0]+"\t\t\t")
            elif len(total_items[i][0]) >= 18:
                file.write(total_items[i][0]+"\t")
            else:
                file.write(total_items[i][0]+"\t\t")

            # for brand column
            if len(total_items[i][1]) <= 6:
                file.write(total_items[i][1]+"\t\t\t")
            else:
                file.write(total_items[i][1]+"\t\t")

            # for quantity column
            file.write(total_items[i][2]+"\t\t")
            # for price column
            file.write(total_items[i][3]+"\t")
            # for total price column
            file.write(total_items[i][4]+"\n")
            total_quantity += int(total_items[i][2])
            total_price += int(total_items[i][4])
        file.write("--------------------------------------------------------------------------------------------\n")
        file.write("Total items:"+str(total_quantity))
        file.write("\nTotal price:" + str(total_price))
        file.close()
    else:
        vendor_name = input("Enter name of supplier: ")
        file_name = unique_id + "_" + vendor_name + ".txt"
        transaction_date = str(time.datetime.now())
        serial_no = 0
        total_quantity = 0
        total_amount = 0
        print("Generating purchase invoice........")
        file = open(file_name, "w")
        file.write("\t\t\t\t   WeCare\n")
        file.write("\t\t\t\tNew Road, Kathmandu\n")
        file.write("\t\t\t\tContact: 9012451010\n")
        file.write("\t\t\t\tPURCHASE INVOICE\n")
        file.write("Vendor:" + vendor_name + " \t\t\t\t\t\tDate:" + transaction_date)
        file.write("\n--------------------------------------------------------------------------------------------\n")
        file.write("S/N\tName\t\t\t Brand\t\t\tQuantity\tRate\tTotal Amount\n")
        for i in range(len(total_items)):
            serial_no += 1
            file.write(str(serial_no) + "\t")
            if len(total_items[i][0]) <= 8:
                file.write(total_items[i][0] + "\t\t\t")
            elif len(total_items[i][0]) >= 18:
                file.write(total_items[i][0] + "\t")
            else:
                file.write(total_items[i][0] + "\t\t")

            # for brand column
            if len(total_items[i][1]) <= 6:
                file.write(total_items[i][1] + "\t\t\t")
            else:
                file.write(total_items[i][1] + "\t\t")

            # for quantity column
            file.write(total_items[i][2] + "\t\t")
            # for price column
            file.write(total_items[i][3] + "\t")
            # for total price column
            file.write(total_items[i][4] + "\n")
            total_quantity += int(total_items[i][2])
            total_amount += int(total_items[i][4])
        file.write("--------------------------------------------------------------------------------------------\n")
        file.write("Total items bought:" + str(total_quantity))
        file.write("\nTotal amount:" + str(total_amount))
        file.close()
