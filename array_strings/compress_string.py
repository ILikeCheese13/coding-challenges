def compress_string(string):
    # Compress a string such that 'AAABCCDDDD' becomes 'A3B1C2D4'. Only compress the string if it saves space.
    # None -> None
    # '' -> ''
    # 'AABBCC' -> 'AABBCC'
    # 'AAABCCDDDD' -> 'A3B1C2D4'
    if string == None or len(string) == 0:
        return string
    prev_char = string[0]
    char_count = 0
    out_str = ""
    for char in string:
        if prev_char != char:
            out_str = out_str + prev_char + str(char_count)
            prev_char = char
            char_count = 1
        else: 
            char_count += 1
    out_str = out_str + prev_char + str(char_count)
    
    if len(out_str) < len(string):
        return out_str
    else:
        return string
    