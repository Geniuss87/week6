# # polimorfizm
#
# from random import randint
#
#
# class Triangle:
#     def __init__(self, count):
#         self.names_values = {f"side_{i}": randint(1, 20) for i in range(count)}
#         self.square = 0
#
#     def get_attrs(self):
#         print(self.__dict__)
#
#     def distract_square(self):
#         square = 0.5 * self.names_values["side_0"] * self.names_values["side_1"]
#         self.square = square
#         print(self.square)
#
#     def get_list_atr(self):
#         tr_list = list(self.__dict__.items())
#         print(tr_list)
#
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.side_a = a
#         self.side_b = b
#         self.square = 0
#
#     def get_list_atr(self):
#         rec_list = list(self.__dict__.items())
#         print(rec_list)
#
#     def get_attrs(self):
#         print(self.__dict__)
#
#     def distract_square(self):
#         square = self.side_a * self.side_b
#         self.square = square
#         print(self.square)
#
#
# triangle1 = Triangle(2)
# triangle2 = Triangle(2)
# rectangle1 = Rectangle(12, 6)
# rectangle2 = Rectangle(7, 8)
#
# my_list = [triangle1, rectangle1, triangle2, rectangle2]
# for i in my_list:
#     i.distract_square()
#     i.get_attrs()
#     i.get_list_atr()

class Student:
    def __init__(self, course):
        self.full_name = "Nurlan Ashyrov"
        self.course = course
        self.subjects = {}
        self.total = 0

    def set_subjects(self, subjects: dict):
        self.subjects = subjects

    def get_total(self):
        self.total = sum(self.subjects.values()) / len(self.subjects.values())

    def save_total_file(self):
        with open(f"{self.full_name}.txt", "a") as f:
            f.write(f"{self.full_name} - {self.course} - {self.total}\n")
            for key, value in self.subjects.items():
                f.write(f"{key} - {value}\n")
        self.total = 0
        self.subjects = {}

    def set_course(self):
        self.course += 1

subjects = {
    "algebra": 55,
    "python": 56
}
subjects1 = {
    "math": 59,
    "c++": 58
}

student1 = Student(2)
student1.set_subjects(subjects)
student1.get_total()
student1.save_total_file()
student1.set_course()
student1.set_subjects(subjects1)
student1.get_total()
student1.save_total_file()
student1.set_course()