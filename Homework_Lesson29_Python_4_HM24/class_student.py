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