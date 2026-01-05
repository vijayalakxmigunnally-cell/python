# College Enrollment Program (Beginner Level)

students = []

while True:
    print("\n1. Enroll Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        course = input("Enter course name: ")
        students.append([name, course])
        print("Student enrolled successfully")

    elif choice == "2":
        print("\nEnrolled Students:")
        for s in students:
            print("Name:", s[0], "| Course:", s[1])

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice. Try again.")
