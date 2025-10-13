# Person class
class Person:
    def __init__(self, name: str):
        self.name = name

    def display_details(self):
        return f"Name: {self.name}"


# Student class
class Student(Person):
    def __init__(self, name: str, roll_no: str, branch: str, email: str, course: str):
        super().__init__(name)
        self.roll_no = roll_no
        self.branch = branch
        self.email = email
        self.course = course

    def display_details(self):
        return (f"{super().display_details()}, Roll No: {self.roll_no}, "
                f"Branch: {self.branch}, Email: {self.email}, Course: {self.course}")


# Employee class
class Employee(Person):
    def __init__(self, name: str, emp_id: str, branch: str, subject: str, salary: float, email: str, course: str):
        super().__init__(name)
        self.emp_id = emp_id
        self.branch = branch
        self.subject = subject
        self.salary = salary
        self.email = email
        self.course = course

    def display_details(self):
        return (f"{super().display_details()}, Emp ID: {self.emp_id}, Branch: {self.branch}, "
                f"Subject: {self.subject}, Salary: {self.salary}, Email: {self.email}, Course: {self.course}")


# University class
class University:
    def __init__(self, university_name: str, courses: list[str]):
        self.uni_name = university_name
        self.courses = courses
        self.students_table = dict()  # key = (roll_no, course), value = Student object
        self.emp_table = dict()       # key = emp_id, value = Employee object

    # Add student → allow duplicate roll_no only if course is different
    def addStudent(self, std_obj: Student):
        key = (std_obj.roll_no, std_obj.course)
        if key in self.students_table:
            return f"⚠️ Student ID {std_obj.roll_no} already exists in course {std_obj.course}"
        self.students_table[key] = std_obj
        return f"✅ Student {std_obj.name} added successfully."

    # Add employee → emp_id must be unique
    def addEmployee(self, emp_obj: Employee):
        if emp_obj.emp_id in self.emp_table:
            return f"⚠️ Employee ID {emp_obj.emp_id} already exists!"
        self.emp_table[emp_obj.emp_id] = emp_obj
        return f"✅ Employee {emp_obj.name} added successfully."

    # Add new course
    def addCourse(self, new_course: str):
        if new_course not in self.courses:
            self.courses.append(new_course)
            return f"✅ Course {new_course} added."
        return f"⚠️ Course {new_course} already exists."

    # Show students (filter by course or show summary)
    def totalStudents(self, search_course: str = None):
        if search_course:
            filtered = [s for (roll, course), s in self.students_table.items()
                        if course.lower() == search_course.lower()]
            print(f"\n📘 Students in {search_course} ({len(filtered)})")
            for s in filtered:
                print(s.display_details())
        else:
            print("\n📘 Student counts by Course:")
            counts = {}
            for (roll, course), s in self.students_table.items():
                counts[course] = counts.get(course, 0) + 1
            for course, count in counts.items():
                print(f"{course}: {count} students")

    # Show employees (filter by dept, subject, or course)
    def totalEmployees(self, dept_filter=None, subject_filter=None, course_filter=None):
        employees = list(self.emp_table.values())

        if dept_filter:
            filtered = [e for e in employees if e.branch.lower() == dept_filter.lower()]
            print(f"\n👨‍🏫 Employees in Dept {dept_filter} ({len(filtered)})")

        elif subject_filter:
            filtered = [e for e in employees if e.subject.lower() == subject_filter.lower()]
            print(f"\n👨‍🏫 Employees teaching {subject_filter} ({len(filtered)})")

        elif course_filter:
            filtered = [e for e in employees if e.course.lower() == course_filter.lower()]
            print(f"\n👨‍🏫 Employees under {course_filter} ({len(filtered)})")

        else:
            print("\n👨‍🏫 Employee counts by Department:")
            counts = {}
            for e in employees:
                counts[e.branch] = counts.get(e.branch, 0) + 1
            for dept, count in counts.items():
                print(f"{dept}: {count} employees")
            filtered = employees

        for e in filtered:
            print(e.display_details())


# Main function with menu
if __name__ == "__main__":
    uni = University("Codegnan", ['PFS', 'JFS', 'DA', 'DS'])

    while True:
        print("\n===== University Menu =====")
        print("1. Add Student")
        print("2. Add Employee")
        print("3. Add Course")
        print("4. Show Students")
        print("5. Show Employees")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            rollno = input("Enter roll number: ")
            branch = input("Enter branch: ")
            email = input("Enter email: ")
            course = input("Enter course: ")
            s = Student(name, rollno, branch, email, course)
            print(uni.addStudent(s))

        elif choice == "2":
            name = input("Enter employee name: ")
            empid = input("Enter employee ID: ")
            branch = input("Enter branch: ")
            subject = input("Enter subject: ")
            salary = float(input("Enter salary: "))
            email = input("Enter email: ")
            course = input("Enter course: ")
            e = Employee(name, empid, branch, subject, salary, email, course)
            print(uni.addEmployee(e))

        elif choice == "3":
            new_course = input("Enter new course to add: ")
            print(uni.addCourse(new_course))

        elif choice == "4":
            course_filter = input("Enter course name (or press Enter for summary): ").strip()
            uni.totalStudents(course_filter if course_filter else None)

        elif choice == "5":
            dept_filter = input("Enter department filter (press Enter to skip): ").strip()
            subject_filter = ""
            course_filter = ""
            if not dept_filter:
                subject_filter = input("Enter subject filter (press Enter to skip): ").strip()
            if not dept_filter and not subject_filter:
                course_filter = input("Enter course filter (press Enter to skip): ").strip()

            uni.totalEmployees(
                dept_filter if dept_filter else None,
                subject_filter if subject_filter else None,
                course_filter if course_filter else None
            )

        elif choice == "6":
            print("Exiting... ✅")
            break
        else:
            print("⚠️ Invalid choice! Try again.")
