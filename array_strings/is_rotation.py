def is_substring(s1, s2):
    return s1 in s2

def is_rotation(s1, s2):
    # Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring
    # Call is_substring only once
    # Any strings that differ in size -> False
    # None, 'foo' -> False (any None results in False)
    # ' ', 'foo' -> False
    # ' ', ' ' -> True
    # foobarbaz', 'barbazfoo' -> True    
    if s1 == None or s2 == None:
        return False
    if len(s1) != len(s2):
        return False
    s3 = s1 + s2
    return is_substring(s2, s3)