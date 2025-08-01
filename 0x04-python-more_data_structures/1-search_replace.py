def search_replace(my_list, search, replace):
    # Create a new list with elements replaced as needed
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
