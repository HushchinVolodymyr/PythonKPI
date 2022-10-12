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
