import string

input_string = input("Enter the sttring: ")

upper_case_count = 0
lower_case_count = 0
digit_count = 0
punctuation_count = 0

for char in input_string:
    if char.isupper(): 
        upper_case_count += 1
    elif char.islower(): 
        lower_case_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char in string.punctuation:
        punctuation_count += 1

print("Number of letters in upper case:", upper_case_count)
print("Number of letters in lower case:", lower_case_count)
print("Number of digits:", digit_count)
print("Number of punctuation characters:", punctuation_count)
