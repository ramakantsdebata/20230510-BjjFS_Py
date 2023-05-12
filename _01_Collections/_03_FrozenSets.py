# FROZENSET
# Printing Dictionary keys as a FrozenSet

Item = {"Name": "Cheese spread", "Company": "Amul", "Class": "Dairy", 
        "MFD": "01/23", "Shelf Life": "6 months"}
 
# making keys of dictionary as frozenset
key = frozenset(Item)
 
# printing dict keys as frozenset
print('The frozen set is:', key)


# Using a fozenset as a key in a dictionary
dairyItems = frozenset({"Cheese Spread", "Butter", "Mayonese"})
print(type(dairyItems))

warehouseSection = {"Furniture": "Rear North", 
                    "Kitchenware": "1st floor", dairyItems: "Deep Fridge"}
print(warehouseSection["Furniture"])
print(warehouseSection[dairyItems])
