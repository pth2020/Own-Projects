#Shopping cart program:
#Enables shoppers to shop online for food.
#In the shopping cart, shoppers can add items, remove items, view items,
#view total cost, change quantities of items and finally check out.

print("\n******************************************")
print("Welcome to Moonlight Food Supermarket")
print("******************************************\n")

#dictionary - food/drink list
#key(item name) - value(item price £)
shopping_items = {
    'Orange Juice':  1.75, 'Apple Juice' : 1.75, 'Water' : 0.55, 
    'Tomatoes' : 2.15, 'Lettuce' : 1.20, 'Cucumber' : 0.35, 
    'Potatoes' : 1.50, 'Onions' : 1.75, 'Courgettes' : 1.60,
    'Bread' : 1.15, 'Butter' : 2.20, 'Teabags' : 4.15,
    'Pasta' : 0.95, 'Tomato_tins' : 2.00, 'Cooking_Oil' : 5.50,
    'Milk' : 1.80, 'Nescafe' : 5.40, 'Sugar' : 2.15 
}
#empty shopping cart dictionary 
shopping_cart_dict = {}
option  = 1 #menu option

#to add an item to shopping cart
def add_item_to_cart():
    item = input("Enter item name to add: ")
    qty_entered = int(input("Enter quantity: "))
    if not qty_entered.is_integer or qty_entered < 1 : #To verify entered value is integer and not less than 1
        print("**************************************************")
        print("Invalid entry!")
        print("Item unavailable in shopping list or incorrect quantity entered.")
        print("**************************************************")
    elif shopping_cart_dict.__contains__(item): #to increase quantity of item if item is already in shopping cart
        qty_old = int(float(shopping_cart_dict.get(item))/(shopping_items.get(item))) #works out available quantity of item
        qty_new = qty_old + qty_entered
        edit_items_qty(qty_new,item) #updates quantity of item in shopping cart
    else:
        item_name = item.capitalize()
        #To write the price of an item to two decimal places
        shopping_cart_dict[item_name] = format_to_decimal_place(compute_items_total_cost(qty_entered ,float(shopping_items.get(item_name))))
        print(f"{item_name} added to cart")

def compute_items_total_cost(qty,shopping_item_price): #computes total price of an item = quantity * unit price
    return qty * shopping_item_price
    
def edit_items_qty(qty,item): #updates quantity of item in shopping cart
    shopping_cart_dict[item] = qty*float(shopping_items[item])

def remove_item_from_cart(): #To remove an item from shopping cart
    item = input("Enter item name to remove: ")
    item_name = item.capitalize()
    #checks if shopping cart is empty or item doesn't exist in shopping cart
    if shopping_cart_dict == {} or not shopping_cart_dict.__contains__(item_name):
        print("****************************************************")
        print("Shopping cart is empty or item not in shopping cart.")
        print("****************************************************")
    else:
        shopping_cart_dict.pop(item_name)
        print(f"{item_name} removed from cart")

def view_food_list():  #displays all items available to buy
    for x,y in shopping_items.items():
        print(x,": £",format_to_decimal_place(y))
    print("*********************************")

def view_shopping_cart_dict(): #displays items in the shopping cart
    if shopping_cart_dict == {}:
        print("Shopping cart is empty")
    else: 
        for x,y in shopping_cart_dict.items():
            y_formatted = format_to_decimal_place(y)
            #works out quantity of an item in the shopping cart by 
            #diving total cost in shopping cart to unit price in the shopping list
            print("Item: ", x,",",f"Qty: {int(float(y)/float(shopping_items[x]))}",",","Total cost: £",y_formatted)
    print("**************************************************")

def compute_total_cost(): #works out total cost of all items added to shopping cart
    total_cost = 0.0
    for cost in shopping_cart_dict.values():
        total_cost += float(cost)
    return format_to_decimal_place(total_cost) 

def format_to_decimal_place(value): #formats money to two decimal places
    return "{:.2f}".format(float(value))

    

while (option != 7):
    print("Choose an option to continue.(e.g. 1 for add)\n")
    print("1. Add an item to cart.")
    print("2. Remove an item from cart.")
    print("3. View shopping cart")
    print("4. View total cost.")
    print("5. Edit quantity of an item.")
    print("6. View food items available.")
    print("7. Check out.")

    option = int(input("\nEnter your option: "))
    print("\n")
    if option == 1: 
        add_item_to_cart()
        
    elif option == 2:
        remove_item_from_cart()

    elif option == 3:
        print("**************************************************")
        print("Shopping cart")
        print("**************************************************")
        view_shopping_cart_dict()

    elif option == 4:
        print("****************************************")
        print(f"Shopping cart total cost so far: £ {compute_total_cost()}")
        print("****************************************")

    elif option == 5:
        item_name = input("Enter name of item: ")
        qty_to_edit = int(input("Enter the new quantity: "))
        edit_items_qty(qty_to_edit,item_name)

    elif option == 6:
        print("*********************************")
        print("Shopping list")
        print("*********************************")
        view_food_list()

    else:
        print("**************************************************")
        print("Check out...")
        print("**************************************************")
        view_shopping_cart_dict()
        print(f"Total cost: £{compute_total_cost()}")
        print("**************************************************")
