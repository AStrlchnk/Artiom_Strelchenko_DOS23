str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common_symbols = set(str1) & set(str2)

print("Common symbols:", sorted(common_symbols))