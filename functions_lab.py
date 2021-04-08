#!/usr/bin/env python
                    ##~ CHEF CALCULATOR APP ~##

######### FOOD COST BY OUNCE TO MENU PRICE CONVERSION CALCULATOR ################
######## Industry food cost ideally between 28-35% of revenue | App based on 30%

############ BULK ITEM PRICE BY CASE CONVERTED TO FOOD COST PER OZ.

n = True
total = 0
while n:
    size = float(input("Enter bulk weight of item in pounds: "))
    price = float(input("Enter total bulk cost of item: "))

    def food_cost_per_ounce(*args):
        cost = lambda x, y: x / (y * 16)
        return cost(price, size)
    print(f'This item costs ${food_cost_per_ounce(size, price):.2f} per oz.\n')


    ######## MENU ITEM COST BASED ON PORTION SIZE PER INGREDIENT

    portion = float(input("Enter portion size in ounces: "))
    menu_price = food_cost_per_ounce() * portion
    print(f"This item will add ${menu_price:.2f} to food cost of dish\n")


    ####### SUGGESTED MENU SELLING PRICE OF ITEM BASED ON FOOD COST PERCENTAGE

    suggested_menu_price = menu_price / .30
    print(f"Individual item should be sold on menu as ${suggested_menu_price:.2f}\n")


    ####### ADD ITEM TO DISH | TOTAL FOOD COST TO MENU SELLING PRICE

    add_item_option = str(input("Would you like to add another item? y/n: "))
    if add_item_option == "y":
        total += menu_price
        print(f"Total food cost for this dish is currently at ${total:.2f}\n")
    else:
        total += menu_price
        print(f"total food cost for dish is ${total:.2f}\n")
        print(f"Completed dish should be priced on menu at ${(total / .30):.2f}\n")
        break








