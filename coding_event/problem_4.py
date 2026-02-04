mystring = "Hello my name is alex"
print(mystring)
if len(mystring) >8:
    print("bad barcode")

regex_str = r"[a-zA-Z]{2}"
num_regex_str = r'[0-9]{2}'
first = mystring[:2]
middle = mystring[2:-2]
end = mystring[-2:]

print(first, middle, end)