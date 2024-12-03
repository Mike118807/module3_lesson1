# Restaurant Menu Update You are given an initial structure of a restaurant
#  menu stored in a nested dictionary. Your task is to update this menu based 
# on given instructions, using Initial menu.


# Initial menu

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
    }

# Add a new category titled "Beverages" with at least two items.
restaurant_menu["Beverages"] = {"Coffee": 2.99, "Tea": 1.99}

# Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters".
del restaurant_menu["Starters"]["Bruschetta"]

# Print new menu.
print(restaurant_menu)

# Finished code will:
#  - Add a new category called "Beverages" with at least two items. 
#  - Update the price of "Steak" to 17.99.
#  - Remove "Bruschetta" from "Starters".