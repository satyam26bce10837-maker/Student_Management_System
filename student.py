from storage import load_data, save_data 


# Add a new student to the system
def add_student():
    students = load_data("data/students.json")

    # Get student details from user 
    name = input("Enter student name: ")
    if not name.strip():
        print("Name cannot be empty.")
        return
    try:
        age = int(input("Enter student age: "))
        if age < 0:
            print("Age must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return
    course = input("Enter student course: ")
    if not course.strip():
        print("Please enter a valid course.")
        return
    college = input("Enter student college: ")
    if not college.strip():
        print("Please enter a valid college.")
        return

    student = {
        "name": name,
        "age": age,
        "course": course,
        "college": college
    }

    students.append(student)
    save_data("data/students.json", students)
    print("Student added successfully!")

# Display the list of students in the system
def view_students():
    students = load_data("data/students.json")
    if not students:
        print("No students found.")
        return

    print("\n====== Student List ======")
    for student in students:
        print("Name: ", student['name'])
        print("Age: ", student['age'])
        print("Course: ", student['course'])
        print("College: ", student['college'])
        print("---------------------------")

# Update the details of an existing student in the system
def update_student():
    students = load_data("data/students.json")
    name = input("Enter the name of the student to update: ")

    for student in students:
        if student['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep current value):")
            new_name = input("Enter new name: ") or student['name']
            new_age = int(input("Enter new age: ")) or student['age']
            new_course = input("Enter new course: ") or student['course']
            new_college = input("Enter new college: ") or student['college']

            student.update({
                "name": new_name,
                "age": int(new_age),
                "course": new_course,
                "college": new_college
            })

            save_data("data/students.json", students)
            print("Student updated successfully!")
            return

    print("Student not found.")

# Delete a student from the system
def delete_student():
    students = load_data("data/students.json")
    name = input("Enter the name of the student to delete: ")

    for student in students:
        if student['name'].lower() == name.lower():
            students.remove(student)
            save_data("data/students.json", students)
            print("Student deleted successfully!")
            return

    print("Student not found.")    