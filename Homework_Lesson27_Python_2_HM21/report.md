1. Написать скрипт, который принимает на вход строку и выводит на
экран количество букв в верхнем регистре, количество букв в нижнем
регистре, количество цифр и количество символов пунктуации.

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
2. Написать скрипт, который принимает на вход два списка и выводит на
экран элементы, которые присутствуют в обоих списках.

        list1 = input("Enter the elements of the first list separated by a space: ").split()

        list2 = input("Enter the elements of the second list separated by a space: ").split()

        common_elements = set(list1) & set(list2)

        print("Common elements:", list(common_elements))
3. Написать скрипт, который принимает на вход массив чисел и сортирует
его в порядке убывания.

        numbers = list(map(int, input("Enter numbers with a space: ").split()))

        numbers.sort(reverse=True)

        print("Sorted list:", numbers)
4. Написать скрипт, который принимает на вход две строки и выводит на
экран все символы, которые встречаются в обеих строках.

        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")

        common_symbols = set(str1) & set(str2)

        print("Common symbols:", sorted(common_symbols))
5. Написать скрипт, который принимает на вход список чисел и находит
медиану этого списка.

        numbers = list(map(int, input("Enter numbers with a space: ").split()))

        numbers.sort()

        n = len(numbers)
        if n % 2 == 1:
            median = numbers[n // 2]
        else:
            median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

        print("Median:", median)
6. Написать скрипт, который принимает на вход строку и заменяет в ней
все гласные буквы на символ "-".

        input_string = input("Enter string: ")

        output_string = ""

        for char in input_string:
            if char in "aeiouAEIOU": 
                output_string += "-" 
            else:
                output_string += char

        print(output_string)