def permutations(str1, str2):
    # Determine if a string is a permutation of another string
    # One or more empty strings -> False
    # 'Nib', 'bin' -> False
    # 'act', 'cat' -> True
    # 'a ct', 'ca t' -> True    
    return set(str1) == set(str2)