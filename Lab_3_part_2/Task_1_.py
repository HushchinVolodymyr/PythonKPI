
class ITeacher():
    def __str__(self):
        return "Teacher: " + str(self.teacher_name)

class Teacher(ITeacher):
    def __init__(self, teacher_name = " "):
        self.teacher_name = teacher_name

    def set_name(self, name):
        self.teacher_name = name

class ICourse():
    def __str__(self) -> str:
        return "Name of course: " + str(self.course)

class ILocalCourse(ICourse):
    def __init__(self, course_name, topics, teacher):
        self.course_name = course_name
        self.topics = topics
        self.teacher = teacher

class IOffsiteCourse(ILocalCourse):
    def __init__(self, course_name, topics, teacher):
        super().__init__(course_name, topics, teacher)

class ICourseFactory():
    def __str__(self):
        return "Tecaher: " + str(self.teacher) + "\nCourse name" + str(self.course_name)
        
class CourseFactory(ICourseFactory):
    def create_teacher(self, teacher_name):
        if isinstance(teacher_name, str):
           return Teacher(teacher_name)
        else:
            raise Exception("Name of teacher must be string!") 

    def create_course(self, course_name, topics, teacher, course):
        if not isinstance(course_name, str):
            raise Exception("Name of course must be string!")
        if not isinstance(teacher, ITeacher):
            raise Exception("Tecaher must be ITeacher!")
        if course == "Local":
            return ILocalCourse(course_name, teacher, topics)
        elif course == "Offfsite":
            return IOffsiteCourse(course_name, teacher, topics)
        else:
            raise Exception("Unkonwm course type!")

