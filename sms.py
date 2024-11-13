# Base class for Staff
class Staff:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_staff_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"


# Teacher class, inherits from Staff
class Teacher(Staff):
    def __init__(self, name, salary):
        super().__init__(name, "Teacher", salary)

    def upload_scores(self, student, subject, score):
        student.add_score(subject, score)
        print(f"{self.name} uploaded score for {student.name} in {subject}: {score}")


# Administrator class, inherits from Staff
class Administrator(Staff):
    def __init__(self, name, salary):
        super().__init__(name, "Administrator", salary)
        self.fees_collected = 0

    def collect_fee(self, student_name, amount):
        print(f"Collected fee of ${amount} from {student_name}")
        return f"Receipt for {student_name}: ${amount} received. Thank you."


# Student class
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = {}

    def add_score(self, subject, score):
        self.scores[subject] = score

    def display_info(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def get_scores(self):
        return self.scores


# Parent class, allows viewing of child’s scores
class Parent:
    def __init__(self, child):
        self.child = child

    def view_child_scores(self):
        return f"{self.child.name}'s Scores: {self.child.get_scores()}"


# School Management System, main class to manage all entities
class SchoolManagementSystem:
    def __init__(self):
        self.staff_list = []
        self.student_list = []

    def add_staff(self, staff_member):
        self.staff_list.append(staff_member)
        print(f"Added staff member: {staff_member.display_staff_info()}")

    def add_student(self, student):
        self.student_list.append(student)
        print(f"Added student: {student.display_info()}")

    def find_student_by_id(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                return student
        return None


# Dashboard for Teacher
class TeacherDashboard:
    def __init__(self, teacher, system):
        self.teacher = teacher
        self.system = system

    def view_students(self):
        for student in self.system.student_list:
            print(student.display_info())

    def upload_student_score(self, student_id, subject, score):
        student = self.system.find_student_by_id(student_id)
        if student:
            self.teacher.upload_scores(student, subject, score)
        else:
            print("Student not found")


# Dashboard for Administrator
class AdminDashboard:
    def __init__(self, admin, system):
        self.admin = admin
        self.system = system

    def collect_student_fee(self, student_name, amount):
        receipt = self.admin.collect_fee(student_name, amount)
        print(receipt)

    def view_all_fees(self):
        print(f"Total fees collected: ${self.admin.fees_collected}")


# Dashboard for Management (overview of staff and students)
class ManagementDashboard:
    def __init__(self, system):
        self.system = system

    def view_all_staff(self):
        print("All Staff Members:")
        for staff in self.system.staff_list:
            print(staff.display_staff_info())

    def view_all_students(self):
        print("All Students:")
        for student in self.system.student_list:
            print(student.display_info())


# Main program
if __name__ == "__main__":
    # Initialize school management system
    system = SchoolManagementSystem()
    
    # Add staff members
    teacher = Teacher("Alice Johnson", 50000)
    admin = Administrator("Robert Smith", 70000)
    system.add_staff(teacher)
    system.add_staff(admin)

    # Add students
    student1 = Student("S001", "John Doe", 15, "Grade 10")
    student2 = Student("S002", "Jane Doe", 14, "Grade 9")
    system.add_student(student1)
    system.add_student(student2)

    # Teacher Dashboard
    teacher_dashboard = TeacherDashboard(teacher, system)
    teacher_dashboard.view_students()
    teacher_dashboard.upload_student_score("S001", "Math", 88)
    teacher_dashboard.upload_student_score("S002", "Science", 92)

    # Parent views student scores
    parent1 = Parent(student1)
    print(parent1.view_child_scores())

    # Admin Dashboard
    admin_dashboard = AdminDashboard(admin, system)
    admin_dashboard.collect_student_fee("John Doe", 500)
    admin_dashboard.collect_student_fee("Jane Doe", 300)

    # Management Dashboard
    management_dashboard = ManagementDashboard(system)
    management_dashboard.view_all_staff()
    management_dashboard.view_all_students()
