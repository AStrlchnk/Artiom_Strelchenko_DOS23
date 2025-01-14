list1 = input("Enter the elements of the first list separated by a space: ").split()
list2 = input("Enter the elements of the second list separated by a space: ").split()

common_elements = set(list1) & set(list2)

print("Common elements:", list(common_elements))