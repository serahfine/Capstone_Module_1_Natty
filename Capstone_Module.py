""" Welcome to the Fruit Market
List Menu:
1. Show Fruit List
2. Update Fruit List
3. Delete Fruit
4. Buy Fruit
5. Exit Program
Enter the desired number in the List Menu: """

import copy

menu_input = -1 # list menu is integer positive (and will be updated every user input), -1 is impossible; 
# show if the input is user input or default input 

# why shallow copy? --> prevent code side effects (mutate) on said dictionary 
# you dont want weird bugs when a global list suddenly gets updated
# fruit_dict_list is a global variable used in multiple functions -> 
# keep functions pure to prevent global list from being edited

# print(fruit_dict_list_copy)

def create_main_menu():
    global menu_input
    print("")
    print("Welcome to the Fruit Market!")
    print("")
    print("List Menu:")
    print("1. Create or Update Fruit List")
    print("2. Show Fruit List")
    print("3. Delete Fruit")
    print("4. Buy Fruit")
    print("5. Exit Program")
    menu_input = int(input("Enter the desired number in the List Menu: "))
    print("")
    if menu_input == 1:
        return create_menu_1()
    elif menu_input == 2:
        return create_menu_2()
    elif menu_input == 3:
        return create_menu_3()
    elif menu_input == 4:
        return create_menu_4()
    elif menu_input == 5:
        return create_menu_5()
    else:
        print("Your input is invalid! Please try again.\n")
        return create_main_menu()

def return_to_main_menu():
    back_to_main_menu = int(input("Enter 9 to return to the main menu: "))
    print("")
    if back_to_main_menu == 9:
        return create_main_menu()
    
counter= 1 
fruit_dict_list = []

def add_item(name, origin, stock, price): # add unique ID to every addition of dictionary
    global counter
    global fruit_dict_list
    fruit_dict_list.append({
        "Item ID": "{:03d}".format(counter),
        "Fruit": name,
        "Origin": origin,
        "Stock": stock,
        "Price": price
    })
    counter += 1
    return(fruit_dict_list)
add_item("Pomelo","Bali",10,10000)
add_item("Apple","Malang",15,7500)
add_item("Orange","Bogor",20,8000)
add_item("Pear","Tasikmalaya",20,8000)

fruit_dict_list_copy = copy.copy(fruit_dict_list)
    
def create_menu_1():
    print("You have accessed Menu 1")
    global fruit_dict_list
    global fruit_dict_list_copy
    print("Please select an option.")
    print("1. Add New Fruit")
    print("2. Add Stock to Existing Fruit")
    print("3. Edit Fruit List")
    print("4. Return to Main Menu")
    input_menu_1 = int(input("Please enter the number of the desired function: "))
    if input_menu_1 == 1:
        input_new_fruit_name = input("Please enter the fruit you want to add to the list: ")
        input_new_fruit_origin = input("Please enter the origin of the fruit: ")
        input_new_fruit_stock = int(input("Please enter the number of fruits in stock: "))
        input_new_fruit_price = int(input("Please enter the price of the fruit: "))
        add_item(input_new_fruit_name,input_new_fruit_origin,input_new_fruit_stock,input_new_fruit_price)
        fruit_dict_list_copy = fruit_dict_list
        print(fruit_dict_list)
        print(f"\nFruit:{input_new_fruit_name}    Origin:{input_new_fruit_origin}   Stock:{input_new_fruit_stock}   Price:Rp{input_new_fruit_price}" "\n")
        print("Your addition was successful!\n")
        return return_to_main_menu()
    elif input_menu_1 == 2:
        print(fruit_dict_list)
        input_fruit_add = input("Please enter the ID of the fruit you want to replenish stock: ")
        input_num_add = int(input("Please enter how much fruit you want to add: "))
        for j in range(len(fruit_dict_list)):
            fruit_dict_add = fruit_dict_list[j]
            fruit_add_name = fruit_dict_add["Fruit"]
            fruit_add_stock = fruit_dict_add["Stock"]
            fruit_add_id = fruit_dict_add["Item ID"] 
            if fruit_add_id == input_fruit_add:
                # fruit_add_id is the list index to edit
                fruit_dict_add["Stock"] = fruit_add_stock + input_num_add
                new_stock = fruit_dict_add["Stock"]
                fruit_dict_list_copy = fruit_dict_list
                print(fruit_dict_list) # return function stops the functions when you run thru what u needed in the list
                print(f"You have successfully replenished the stock of {fruit_add_name} with ID: {fruit_add_id} to {new_stock}!\n")
                return return_to_main_menu()
    elif input_menu_1 == 3:
        print("1. Edit Fruit Name")
        print("2. Edit Fruit Origin")
        print("3. Edit Fruit Price")
        input_edit_fx = int(input("Please enter the number of the function you want to access: "))
        edit_id = input("Which Item ID do you want to access? ")
        for k in range(len(fruit_dict_list)):
            fruit_edit_dict = fruit_dict_list[k]
            fruit_edit_name = fruit_edit_dict["Fruit"]
            fruit_edit_origin = fruit_edit_dict["Origin"]
            fruit_edit_price = fruit_edit_dict["Price"]
            fruit_edit_id = fruit_edit_dict["Item ID"]
            if fruit_edit_id == edit_id:
                    print(f"You have selected {fruit_edit_dict}")
                    if input_edit_fx == 1:
                        name_edit = input("What would you like to be the new name? ")
                        fruit_edit_dict["Fruit"] = name_edit
                        new_name = fruit_edit_dict["Fruit"]
                        fruit_dict_list_copy = fruit_dict_list
                        print(fruit_edit_dict)
                        print(f"You have successfully updated the name from {fruit_edit_name} to {new_name}!")
                        return return_to_main_menu()
                    elif input_edit_fx == 2:
                        origin_edit = input("What would you like to be the new origin? ")
                        fruit_edit_dict["Origin"] = origin_edit
                        new_origin = fruit_edit_dict["Origin"]
                        fruit_dict_list_copy = fruit_dict_list
                        print(fruit_edit_dict)
                        print(f"You have successfully updated the origin from {fruit_edit_origin} to {new_origin}!")
                        return return_to_main_menu()
                        # print(fruit_edit_dict["Origin"])
                    elif input_edit_fx == 3:
                        price_edit = int(input("What would you like to be the new price? "))
                        fruit_edit_dict["Price"] = price_edit
                        new_price = fruit_edit_dict["Price"]
                        fruit_dict_list_copy = fruit_dict_list
                        print(fruit_edit_dict)
                        print(f"You have successfully updated the origin from {fruit_edit_price} to {new_price}!")
                        return return_to_main_menu()
                    else:
                        print("Error! Please select the correct input!")
                        return return_to_main_menu()
    elif input_menu_1 == 4:
        return create_main_menu()
    else:
        print ("The Item ID was not found! Please try again.\n")
        return create_menu_1()
    return return_to_main_menu()

def create_menu_2():
    print("You have accessed Menu 2")
    for i in fruit_dict_list:
        fruit_id = str(i["Item ID"])
        fruit_name = str(i["Fruit"])
        fruit_origin = str(i["Origin"])
        fruit_stock = str(i["Stock"])
        fruit_price = str(i["Price"])
        print(f"Item ID:{fruit_id}     {fruit_name}    Origin:{fruit_origin}   Stock:{fruit_stock}   Price:Rp{fruit_price}" "\n")
        #insert return to main menu
    return return_to_main_menu()
    
def create_menu_3():
    print("You have accessed Menu 3")
    global fruit_dict_list
    global fruit_dict_list_copy
    input_delete = input("Enter the ID you want to delete: ")
    for dict in range(len(fruit_dict_list)):
        fruit_dict = fruit_dict_list[dict]
        fruit_dict_id = fruit_dict["Item ID"] # delete the item from its index
        if fruit_dict_id == input_delete:
            # index is the list index to delete
            del_conf = input(f"You are about to delete {fruit_dict} from the list. Are you sure? (Y/N) ")
            if del_conf == "Y":
                del fruit_dict_list_copy[dict]
                # stop the if when the condition is met in the for loop
                fruit_dict_list = fruit_dict_list_copy #re-update fruit_dict_list
                print(fruit_dict_list) # return function stops the functions when you run thru what u needed in the list
                print("You have successfully deleted the item from the list!\n")
                return return_to_main_menu()
            if del_conf == "N":
                print("You will be redirected back to Menu 3")
                return create_menu_3()
    print("Your input of {} was not found.\n".format(input_delete)) # if the ID is not found or error
    print(fruit_dict_list)
    return return_to_main_menu()
    
def create_menu_4():
    global fruit_dict_list
    global fruit_dict_list_copy
    print("You have accessed Menu 4")
    fruit_purchase = input("What fruit do you wish to purchase? ")
    num_purchase = int(input("Enter how many fruits you want to purchase: "))
    for i in fruit_dict_list:
        fruit_to_purchase = str(i["Fruit"])
        fruit_purchase_stock = int(i["Stock"])
        fruit_purchase_price = int(i["Price"])
        if fruit_purchase == fruit_to_purchase:
            if num_purchase > fruit_purchase_stock:
                print(f"There is not enough stock!\nThe amount of stock for {fruit_purchase} is {fruit_purchase_stock}.")
                q_replenish = input("Do you want to replenish stock? (Y/N) ")
                if q_replenish == "Y":
                    print("You will be redirected to Menu 1.")
                    print("Please add more stock to the fruit!")
                    return create_menu_1()
                else:
                    print("Error! There is not enough stock. You will be redirected to the main menu.")
                return create_main_menu()
            total_price = fruit_purchase_price * num_purchase
            stock_remaining = fruit_purchase_stock - num_purchase
            i["Stock"]=stock_remaining
            print(("The total price you need to pay is Rp.{}.").format(total_price))
            print((f"The stock of {fruit_purchase} left remaining is {stock_remaining}"))
            return return_to_main_menu()
    print("The fruit you are looking for was not found! Please check the list again!")         
    fruit_dict_list_copy = fruit_dict_list
    print(fruit_dict_list)
    return return_to_main_menu()

def create_menu_5():
    print("Thank you for visiting the Fruit Market!")
    print("You will be exiting the program shortly.")
    return()

create_main_menu()