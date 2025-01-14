1. Создайте класс "Круг", который имеет атрибуты радиус и цвет, и
методы вычисления площади и длины окружности. Создайте несколько
объектов этого класса и вызовите его методы для каждого объекта.

        import math

        class Circle:
            def __init__(self, radius, color):
                self.radius = radius
                self.color = color

            def area(self):
                return math.pi * self.radius ** 2

            def circumference(self):
                return 2 * math.pi * self.radius

            def __str__(self):
                return f"Circle(radius={self.radius}, color='{self.color}')"

        circle1 = Circle(2, "red")
        circle2 = Circle(4, "blue")
        circle3 = Circle(8, "green")

        circles = [circle1, circle2, circle3]
    
        for circle in circles:
        print(circle)
        print(f"Area: {circle.area():.2f}")
        print(f"Circumference: {circle.circumference():.2f}\n")
    f перед строкой в print указывает, что строка является форматированной (f-string), и в ней можно использовать выражения в {}.

    :.2f означает, что количество знаков после запятой равно двум (f-float).

    Результат:

        Circle(radius=2, color='red')
        Area: 12.57
        Circumference: 12.57

        Circle(radius=4, color='blue')
        Area: 50.27
        Circumference: 25.13

        Circle(radius=8, color='green')
        Area: 201.06
        Circumference: 50.27

2. Создайте класс "Банковский счет", который имеет атрибуты номер
счета, имя владельца, баланс и методы пополнения и снятия денег со
счета. Создайте несколько объектов этого класса и вызовите его методы
для каждого объекта.

        class BankAccount:
            def __init__(self, account_number, owner_name, balance=0):
                self.account_number = account_number
                self.owner_name = owner_name
                self.balance = balance

            def deposit(self, amount):
                if amount > 0:
                    self.balance += amount
                    print(f"The account {self.account_number} has been funded with {amount}. New balance: {self.balance}")
                else:
                    print("The amount for replenishment must be positive.")

            def withdraw(self, amount):
                if amount > 0:
                    if amount <= self.balance:
                        self.balance -= amount
                        print(f"Account {amount} withdrawal {self.account_number}. Balance: {self.balance}")
                    else:
                        print("Insufficient funds in the account.")
                else:
                    print("The amount for replenishment must be positive.")

            def __str__(self):
                return f"Account {self.account_number}, Owner: {self.owner_name}, Balance: {self.balance}"

        account1 = BankAccount("123456", "Ivan Semin", 1000)
        account2 = BankAccount("654321", "Natalia Lukina", 500)
        account3 = BankAccount("789123", "Alexander Ivanov")

        print(account1)
        account1.deposit(500)
        account1.withdraw(300)

        print()

        print(account2)
        account2.deposit(200)
        account2.withdraw(800)

        print()

        print(account3)
        account3.deposit(1000)
        account3.withdraw(1500)

    Результат выполнения:

        Account 123456, Owner: Ivan Semin, Balance: 1000
        The account 123456 has been funded with 500. New balance: 1500
        Account 300 withdrawal 123456. Balance: 1200

        Account 654321, Owner: Natalia Lukina, Balance: 500
        The account 654321 has been funded with 200. New balance: 700
        Insufficient funds in the account.

        Account 789123, Owner: Alexander Ivanov, Balance: 0
        The account 789123 has been funded with 1000. New balance: 1000
        Insufficient funds in the account.

3. Создайте класс "Студент", который имеет атрибуты имя, возраст и
средний балл. Создайте методы для вычисления среднего балла и
определения статуса студента (отличник, хорошист, троечник).Создайте
несколько объектов этого класса и вызовите его методы для каждого
объекта.

        class Student:
            def __init__(self, name, age, grades):
                self.name = name
                self.age = age
                self.grades = grades

            def calculate_average(self):
                if self.grades:
                    return sum(self.grades) / len(self.grades)
                else:
                    return 0

            def determine_status(self):
                average = self.calculate_average()
                if average >= 9:
                    return "Отличник"
                elif average >= 6:
                    return "Хорошист"
                else:
                    return "Двоечник"

            def __str__(self):
                return f"Студент {self.name}, Возраст: {self.age}, Средний балл: {self.calculate_average():.2f}, Статус: {self.determine_status()}"

        student1 = Student("Никита Сергеев", 20, [8, 9, 9, 10])
        student2 = Student("Мария Турчина", 19, [3, 2, 4, 3])
        student3 = Student("Сергей Петров", 21, [4, 9, 7, 7])

        print(student1)
        print()
        print(student2)
        print()
        print(student3)

    Результат выполнения:

        Студент Никита Сергеев, Возраст: 20, Средний балл: 9.00, Статус: Отличник

        Студент Мария Турчина, Возраст: 19, Средний балл: 3.00, Статус: Двоечник

        Студент Сергей Петров, Возраст: 21, Средний балл: 6.75, Статус: Хорошист