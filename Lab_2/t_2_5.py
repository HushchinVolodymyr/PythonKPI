class Student:
    def __init__(self, name, surname, inp, marks):
        self.name = name
        self.surname = surname
        self.inp = inp
        self.marks = marks

    def aver_mark(self):
        amount_marks = 0
        count_marks = 0

        for el in self.marks:
            amount_marks += 1
            count_marks += el
        
        return count_marks / amount_marks

class Group:
    def __init__(self, students):
        self.students = students
        self.__max_students__ = 20
        self.__students__ = 0
        
    def add_students(self, __students__):
        if __students__ >= self.max_students:
            print("Not enough place in group!")
        elif students in __students__:
            print("This student already in group")
        else:
            self.__students__.append(students)

    def top_5_students(self):
        top = []
        top_mark = 0
        
        for el_1 in range(0, 5):
            top_mark = 0
            stud = self.students[0]

            for el_2 in range(0, len(self.students)):
                if self.students[el_2].aver_mark() > top_mark:
                    top_mark = self.students[el_2].aver_mark()

                    if self.students[el_2] not in top:
                        stud = self.students[el_2]

            top.append(stud)

        return top

first_student = Student("name_1", "surname_1", "inp", [2, 4, 6, 3, 6, 4])
second_student = Student("name_2", "surname_2", "inp", [2, 4, 5, 3, 2, 4]) 
third_student = Student("name_3", "surname_3", "inp", [4, 4, 6, 7, 2, 4]) 
fourth_student = Student("name_4", "surname_4", "inp", [2, 4, 6, 3, 2, 4]) 
fivth_student = Student("name_5", "surname_5", "inp", [2, 4, 6, 3, 9, 2]) 
sixth_student = Student("name_6", "surname_6", "inp", [2, 4, 5, 3, 2, 4]) 
seventh_student = Student("name_7", "surname_7", "inp", [2, 9, 4, 3, 2, 4]) 
eighth_student = Student("name_8", "surname_8", "inp", [3, 4, 6, 3, 2, 1]) 
ninth_student = Student("name_9", "surname_9", "inp", [2, 4, 6, 9, 2, 4]) 
tenth_student = Student("name_10", "surname_10", "inp", [1, 4, 6, 3, 2, 5])

all_students = [first_student, second_student, third_student, fourth_student, fivth_student,
sixth_student, seventh_student, eighth_student, ninth_student, tenth_student]

group = Group(all_students)

top_student = group.top_5_students()

for el in top_student:
    print(el.name)
