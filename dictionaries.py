my_dic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020, # Overwrite the previous value with 2020
    "color": ["red", "blue", "green"] 
}

print(my_dic);

items = my_dic.items()
print("Items: ",items);

values = my_dic.values();
print("values: ", values);

keys = my_dic.keys();
print("keys: ", keys);

# access items
access = my_dic["model"];
print("Access Items: ",access);

# change items
my_dic.update({"model":"Ferary"});
print(my_dic);

# remove item
my_dic.pop("color");
print(my_dic);

# copy the existing dictonory
my_dic2 = my_dic.copy();
print("my_dic2",my_dic2);

if "model" in my_dic:
    print("Yes this model is available in the dictonary");