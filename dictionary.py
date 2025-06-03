my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get keys
keys = my_dict.keys()
print("Keys:", list(keys))

# Get values
values = my_dict.values()
print("Values:", list(values))

# Get key-value pairs
items = my_dict.items()
print("Items:", list(items))

# Iterate through key-value pairs
print("Key-Value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

popped_value=my_dict.pop('a')
print("popped value:",popped_value)
print("dictionary after pop(a):",my_dict)
