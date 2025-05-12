# Student Management System
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists!")
        else:
            self.students[student_id] = Student(student_id, name, age, grade)
            print(f"Student {name} added successfully!")

    def remove_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Student {removed_student.name} removed successfully!")
        else:
            print("Student ID not found!")

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print(f"Student {student_id} updated successfully!")
        else:
            print("Student ID not found!")

    def display_student(self, student_id):
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print("Student ID not found!")

    def display_all_students(self):
        if self.students:
            for student in self.students.values():
                print(student)
        else:
            print("No students to display!")


# Main Program
if __name__ == "__main__":
    system = StudentManagementSystem()

    while True:
        print("\n1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Display Student")
        print("5. Display All Students")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            system.add_student(student_id, name, age, grade)
        elif choice == "2":
            student_id = input("Enter Student ID to remove: ")
            system.remove_student(student_id)
        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new Name (or leave blank): ")
            age = input("Enter new Age (or leave blank): ")
            grade = input("Enter new Grade (or leave blank): ")
            system.update_student(student_id, name=name or None, age=age or None, grade=grade or None)
        elif choice == "4":
            student_id = input("Enter Student ID to display: ")
            system.display_student(student_id)
        elif choice == "5":
            system.display_all_students()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")
