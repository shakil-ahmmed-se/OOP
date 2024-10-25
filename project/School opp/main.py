from school import School,ClassRoom, Subject
from person import Student,Teacher

def main():
    school = School('Joregaccha High School','Sariakandi,Bogura')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    abul = Student('Abul Khan',eight)
    school.student_admission(abul)
    babul = Student('Babul Khan',eight)
    school.student_admission(babul)
    abir = Student('Abir Khan',eight)
    school.student_admission(abir)

    #subject 
    physics_teacher = Teacher('Shajahan Topon')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Haradan Nag')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher('Azmal Sir')
    biology = Subject('biology',biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()
    print(school)

if __name__ == '__main__':
    main()