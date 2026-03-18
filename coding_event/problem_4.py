mystring = ["aaHIHI32", "89172389712398712"]

def validator(str):
    if len(str) != 8:
        return "Invalid"
    if str[:2].isalpha() and str[2:-2].isupper() and str[-2:].isnumeric():
        return "Valid"
    return "Invalid"

for str in mystring:
    print(validator(str))

