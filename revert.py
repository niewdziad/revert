string_ = "Revert me please:)"

def method_1(string_):
    return string_[::-1]
    
def method_2(string_):
    return ''.join(reversed(string_))
    
def method_3(string_):
    inverted = ''
    for char in string_:
        inverted = char + inverted
    return inverted
    
print("1 -->", method_1(string_))
print("2 -->", method_2(string_))
print("3 -->", method_3(string_))