def list_of_chars(list_chars):
    # Implement a function to reverse a string (a list of characters), in-place.
    # None -> None
    # [''] -> ['']
    # ['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']    
    if list_chars == None or len(list_chars) == 1:
        return list_chars
    
    index = len(list_chars) - 1
    new_list = []
    while index >= 0:
        new_list.append(list_chars[index])
        index -= 1
        
    return new_list