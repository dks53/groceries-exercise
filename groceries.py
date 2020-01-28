# groceries.py

#from pprint import pprint
import operator

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
#pprint(products)

# TODO: write some Python code here to produce the desired output

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """

print("------------------------")
print(f"THERE ARE {len(products)} PRODUCTS:")

### Can also use a basic comma-separated format:
#print("THERE ARE ", len(products), " PRODUCTS:")

### Can also use concatanation, but, concatonation won't work here because we're trying to conc. a string and integer
#print("THERE ARE " + len(products) + " PRODUCTS:") 
### so, to make that work, you can:
#print("THERE ARE " + str(len(products)) + " PRODUCTS:") 

print("------------------------")

sorted_products = sorted(products, key = operator.itemgetter("name"))

for prod in sorted_products:
    print("+ ", prod["name"], "(", to_usd(prod["price"]), ")")

print("------------------------")
print("THERE ARE ", len("department"), " DEPARTMENTS:")
print("------------------------")

depts = []

for prod in sorted_products:
    if prod["department"] not in depts:
        depts.append(prod["department"])

sorted_departments = sorted(depts)

for d in sorted_departments:
    matching_dept = [prod for prod in products if prod["department"] == d]
    matching_dept_count =len(matching_dept)
    
    if (matching_dept_count > 1):
        print("+ ", d.title(), "(", matching_dept_count, "products)")
    else:
        print("+ ", d.title(), "(", matching_dept_count, "product)")

 

# -------------
# THERE ARE 20 PRODUCTS:
# -------------
# + All-Seasons Salt ($4.99)
# + Chocolate Fudge Layer Cake ($18.50)
# + Chocolate Sandwich Cookies ($3.50)
# + Cut Russet Potatoes Steam N' Mash ($4.25)
# + Dry Nose Oil ($21.99)
# + Fresh Scent Dishwasher Cleaner ($4.99)
# + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
# + Green Chile Anytime Sauce ($7.99)
# + Light Strawberry Blueberry Yogurt ($6.50)
# + Mint Chocolate Flavored Syrup ($4.50)
# + Overnight Diapers Size 6 ($25.50)
# + Peach Mango Juice ($1.99)
# + Pizza For One Suprema Frozen Pizza ($12.50)
# + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
# + Pure Coconut Water With Orange ($3.50)
# + Rendered Duck Fat ($9.99)
# + Robust Golden Unsweetened Oolong Tea ($2.49)
# + Saline Nasal Mist ($16.00)
# + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
# + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)
#--------------
#THERE ARE 10 DEPARTMENTS:
#--------------
# + Babies (1 product)
# + Beverages (5 products)
# + Dairy Eggs (1 product)
# + Dry Goods Pasta (1 product)
# + Frozen (4 products)
# + Household (1 product)
# + Meat Seafood (1 product)
# + Pantry (2 products)
# + Personal Care (2 products)
# + Snacks (2 products)