# Base class Person (common attributes for Student and Employee)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, rollno, branch, email, course):
        super().__init__(name, age)  # Initialize Person attributes
        self.rollno = rollno
        self.branch = branch
        self.email = email
        self.course = course  # Course student enrolled in

    def display_info(self):
        # Override to add student-specific details
        return (f"{super().display_info()}, Roll No: {self.rollno}, "
                f"Branch: {self.branch}, Course: {self.course}, Email: {self.email}")


# Employee (Faculty/Staff) class inherits from Person
class Employee(Person):
    def __init__(self, name, age, empid, subject, dept, salary, email, course):
        super().__init__(name, age)  # Initialize Person attributes
        self.empid = empid
        self.subject = subject
        self.dept = dept
        self.salary = salary
        self.email = email
        self.course = course  # Course employee belongs to

    def display_info(self):
        # Override to add employee-specific details
        return (f"{super().display_info()}, Emp ID: {self.empid}, "
                f"Subject: {self.subject}, Dept: {self.dept}, "
                f"Course: {self.course}, Salary: {self.salary}, Email: {self.email}")


# University class to manage students and employees
class University:
    def __init__(self, university_name, courses):
        self.university_name = university_name
        self.courses = courses  # List of offered courses
        self.students = {}      # Dictionary with key (rollno, course)
        self.employees = {}     # Dictionary with empid (globally unique)

    def add_student(self, student):
        key = (student.rollno, student.course)
        if key in self.students:   # Duplicate ID check within same course
            print(f"❌ Student ID {student.rollno} already exists in course {student.course}!")
        else:
            self.students[key] = student
            print("✅ Student added successfully!")

    def add_employee(self, employee):
        if employee.empid in self.employees:  # Employee IDs must be unique globally
            print(f"❌ Employee ID {employee.empid} already exists!")
        else:
            self.employees[employee.empid] = employee
            print("✅ Employee added successfully!")

    def display_info(self):
        return f"University Name: {self.university_name}, Courses: {', '.join(self.courses)}"

    def list_students(self):
        if not self.students:
            print("No students enrolled yet.")
            return
        
        dept_filter = input("Enter branch to filter students (leave blank for all): ").strip()
        print("\n--- Students ---")
        found = False
        for student in self.students.values():
            if dept_filter == "" or student.branch.lower() == dept_filter.lower():
                print(student.display_info())
                found = True
        if not found:
            print("❌ No students found for this branch.")

    def list_employees(self):
        if not self.employees:
            print("No employees registered yet.")
            return
        
        dept_filter = input("Enter department to filter employees (leave blank for all): ").strip()
        print("\n--- Employees ---")
        found = False
        for employee in self.employees.values():
            if dept_filter == "" or employee.dept.lower() == dept_filter.lower():
                print(employee.display_info())
                found = True
        if not found:
            print("❌ No employees found for this department.")

    def course_report(self, course_name):
        """Show all students and employees in a given course, plus student count."""
        print(f"\n📘 Report for Course: {course_name}")
        student_count = 0

        # List students in course
        print("\n--- Students ---")
        for student in self.students.values():
            if student.course.lower() == course_name.lower():
                print(student.display_info())
                student_count += 1

        if student_count == 0:
            print("❌ No students in this course.")
        else:
            print(f"✅ Total Students in {course_name}: {student_count}")

        # List employees in course
        print("\n--- Employees ---")
        found_emp = False
        for employee in self.employees.values():
            if employee.course.lower() == course_name.lower():
                print(employee.display_info())
                found_emp = True

        if not found_emp:
            print("❌ No employees in this course.")


# Main function with user input (menu-driven system)
def main():
    # Step 1: Create a university
    uni_name = input("Enter University Name: ")
    courses = input("Enter courses offered (comma separated): ").split(",")
    uni = University(uni_name, [course.strip() for course in courses])
    print("\n✅ University created successfully!")

    while True:
        print("\n====== University Management Menu ======")
        print("1. Add Student")
        print("2. Add Employee")
        print("3. List Students")
        print("4. List Employees")
        print("5. Show University Info")
        print("6. Course Report")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            # Add student
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            rollno = input("Enter Roll No: ")
            branch = input("Enter Branch: ")
            email = input("Enter Email: ")
            course = input("Enter Course: ")
            student = Student(name, age, rollno, branch, email, course)
            uni.add_student(student)

        elif choice == "2":
            # Add employee
            name = input("Enter Employee Name: ")
            age = int(input("Enter Age: "))
            empid = input("Enter Employee ID: ")
            subject = input("Enter Subject: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            email = input("Enter Email: ")
            course = input("Enter Course: ")
            employee = Employee(name, age, empid, subject, dept, salary, email, course)
            uni.add_employee(employee)

        elif choice == "3":
            uni.list_students()

        elif choice == "4":
            uni.list_employees()

        elif choice == "5":
            print(uni.display_info())

        elif choice == "6":
            course_name = input("Enter course name for report: ")
            uni.course_report(course_name)

        elif choice == "7":
            print("🚪 Exiting University Management System. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
