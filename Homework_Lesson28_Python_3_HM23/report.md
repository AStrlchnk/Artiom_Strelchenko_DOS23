1. Напишите функцию multiply_numbers(), которая принимает два
аргумента и возвращает их произведение. Затем вызовите эту функцию
и выведите результат на экран.

        def multiply(x, y):
            return x * y

        result = multiply(5, 7)

        print(result)
2. Создайте файл test.txt и запишите в него строку "Это тестовый файл для
домашнего задания по программированию". Затем откройте этот файл в
режиме чтения, прочитайте его содержимое и выведите на экран.

        with open("test.txt", "w", encoding="utf-8") as file:
        file.write("Это тестовый файл для домашнего задания по программированию")

        with open("test.txt", "r", encoding="utf-8") as file:
        content = file.read()

        print("Содержимое файла:", content)
3. Создайте пустую директорию mydir в текущей рабочей директории.
Затем перейдите в эту директорию и создайте в ней три пустых файла:
file1.txt, file2.txt и file3.txt. Наконец, выведите список файлов в
директории на экран.

        import os

        os.makedirs("mydir")

        os.chdir("mydir")

        for filename in ["file1.txt", "file2.txt", "file3.txt"]:
            with open(filename, "w") as file:
                pass 

        print("List of files in the directory 'mydir':", os.listdir("."))