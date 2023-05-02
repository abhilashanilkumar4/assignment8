def sort_dict_order(str_list):
    
    return sorted(str_list, key=lambda s: [ord(c) for c in s])


str_list = ['apple', 'banana', 'orange', 'cat', 'dog', 'zebra']
print(sort_dict_order(str_list))
