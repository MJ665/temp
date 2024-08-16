class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def display_menu(self):
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        new_student = Student(student_id, name, grade)
        self.students.append(new_student)
        print(f"Student '{name}' has been added.")

    def view_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("Student List:")
            for student in self.students:
                print(student)

    def update_student(self):
        if not self.students:
            print("No students in the system.")
        else:
            self.view_students()
            student_id = input("Enter the ID of the student to update: ")
            for student in self.students:
                if student.student_id == student_id:
                    student.name = input("Enter the new name: ")
                    student.grade = input("Enter the new grade: ")
                    print(f"Student ID '{student_id}' has been updated.")
                    return
            print("Student ID not found.")

    def delete_student(self):
        if not self.students:
            print("No students in the system.")
        else:
            self.view_students()
            student_id = input("Enter the ID of the student to delete: ")
            for student in self.students:
                if student.student_id == student_id:
                    self.students.remove(student)
                    print(f"Student ID '{student_id}' has been deleted.")
                    return
            print("Student ID not found.")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_student()
                elif choice == 2:
                    self.view_students()
                elif choice == 3:
                    self.update_student()
                elif choice == 4:
                    self.delete_student()
                elif choice == 5:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()
