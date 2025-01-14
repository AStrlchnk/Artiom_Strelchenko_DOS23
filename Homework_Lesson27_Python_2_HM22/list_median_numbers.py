numbers = list(map(int, input("Enter numbers with a space as a delimeter: ").split()))


def find_median(numbers):
    
    if not numbers:
        raise ValueError("the list could not be empty")
    
    sorted_numbers=sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

print(find_median(numbers))
# print("Median:", median)