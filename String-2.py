# String-2 chance

# Medium python string problems -- 1 loop.. Use + to combine strings, len(str) is the number of chars in a String, str[i:j] extracts the substring starting at index i and running up to but not including index j.


def double_char(str):
    new_str = ''
    for i in range(len(str)):
        new_str += str[i] * 2
    return new_str


# String-2 > count_hi

# Return the number of times that the string "hi" appears anywhere in the given string.

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
    # return str.count('hi')
    count = 0
    for i in range(len(str)):
        if str[i: i+2] == 'hi':
            count += 1
    return count


# String-2 > cat_dog

# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    cd = 0
    for i in range(len(str)):
        if str[i: i+3] == 'cat':
            cd += 1
        if str[i: i+3] == 'dog':
            cd -= 1
    return cd == 0


# String-2 > count_code

# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i: i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count


# String-2 > end_other

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)


# String-2 > xyz_there

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
  # return 'xyz' in str and not '.xyz' in str
    for i in range(len(str) - 1):
        if str[i: i+3] == 'xyz' and str[i-1] != '.':
            return True
    return False
