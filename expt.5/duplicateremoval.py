def remove_duplicates(d):
    new_dict = {}
    
    for key, value in d.items():
        if value not in new_dict.values():
            new_dict[key] = value
            
    return new_dict


d = eval(input("Enter a dictionary: "))

result = remove_duplicates(d)

print("Dictionary after removing duplicate values:", result)
