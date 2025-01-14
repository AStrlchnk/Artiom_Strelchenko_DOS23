input_string = input("Enter string: ")

output_string = ""

for char in input_string:
    if char in "aeiouAEIOU": 
        output_string += "-" 
    else:
        output_string += char

print(output_string)