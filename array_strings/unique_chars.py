def unique_chars(string):
    # Implement an algorithm to determine if a string has all unique characters
    # '' -> True
    # 'foo' -> False
    # 'bar' -> True    
    result = True
    
    if len(string) > 1:
        index = 0
        for i in string:
            index1 = 0
            for j in string:
                if index != index1:
                    if i == j:
                        result = False
                index1 += 1
            index += 1
    return result
import unittest

class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert(func('')) == True
        assert(func('foo')) == False
        assert(func('bar')) == True
        print('Success: test_unique_chars')

def main():
    test = TestUniqueChars()
    test.test_unique_chars(unique_chars)
    try:
        test.test_unique_chars(unique_chars_hash)
        test.test_unique_chars(unique_chars_inplace)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass

if __name__ == '__main__':
    main()