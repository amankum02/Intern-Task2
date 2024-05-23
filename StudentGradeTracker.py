class Student:
    def __init__(self, stdname):
        self.stdname = stdname
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = [grade]
        else:
            self.grades[subject].append(grade)

    def calculate_average_grade(self):
        total = 0
        count = 0
        for subject, grades in self.grades.items():
            total += sum(grades)
            count += len(grades)
        if count == 0:
            return 0
        else:
            return total / count

    def display_grades(self):
        print(f"Grades for {self.stdname}:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")
        average_grade = self.calculate_average_grade()
        print(f"Average grade: {average_grade:.2f}")


def main():
    students = []
    while True:
        print("\n1. Add student")
        print("2. Add grade for a student")
        print("3. Display grades for a student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stdname = input("Enter student name: ")
            student = Student(stdname)
            students.append(student)
            print(f"Student {stdname} added successfully.")
        elif choice == "2":
            if not students:
                print("No students added yet. Please add a student first.")
                continue
            student_name = input("Enter student name: ")
            found = False
            for student in students:
                if student.stdname == student_name:
                    found = True
                    subject = input("Enter subject: ")
                    grade = float(input("Enter grade: "))
                    student.add_grade(subject, grade)
                    print("Grade added successfully.")
                    break
            if not found:
                print("Student not found.")
        elif choice == "3":
            if not students:
                print("No students added yet. Please add a student first.")
                continue
            student_name = input("Enter student name: ")
            found = False
            for student in students:
                if student.stdname == student_name:
                    found = True
                    student.display_grades()
                    break
            if not found:
                print("Student not found.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()