import string
def from_camel_case(name):
    
    for c in  [i for i in name if i in string.ascii_uppercase]:
        name = name.replace(c,'_'+c.lower())
    if name.startswith('_'):
        name=name[1:]
    return name.lower()
if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("MyFunctionName"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert from_camel_case("MyFunctionName") == "my_function_name"
    # assert from_camel_case("IPhone") == "i_phone"
    # assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    # assert from_camel_case("Name") == "name"
    # print("Coding complete? Click 'Check' to earn cool rewards!")