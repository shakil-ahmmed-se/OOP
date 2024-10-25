class Students:
    def __init__(self,name,current_class,id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student {self.name}, class {self.current_class} , id {self.id}'

class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name = name
        self.subject =subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher : {self.name} Subjcet: {self.subject}'


class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self,name,subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
    
    def enroll(self,name, fee):
        if fee < 6500:
            return 'Not Enough Money'
        else:
            id = len(self.students) + 1
            student = Students(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id {id} extra money {fee -6500}'
        
    def __repr__(self) -> str:
        print(f'Welcom  to ',self.name )
        print('-------- Our Teachers ---------')
        for teacher in self.teachers:
            print(teacher)
        
        print('--------- Our Students --------')
        for student in self.students:
            print(student)
        return 'All done for Now'
# alia = Students('Alia ',7,20)
# print(alia)
# ranbir = Teacher('Ranbir','Algo',101)
# print(ranbir)

phithron = School('Phithron')
phithron.enroll('Alia',5200)
phithron.enroll('Ali', 7000)
phithron.enroll('Bhai Jan', 90000)

phithron.add_teacher('Tom Crusise','Python')
phithron.add_teacher('John Dev','Algo')
phithron.add_teacher('Stev ','DS')
phithron.add_teacher('Rahat  ','C Program')

print(phithron)