from storage import load_data 

# Generate a complete academic report for each student
def student_report():
    students = load_data("data/students.json")
    subjects = load_data("data/subjects.json")
    attendance = load_data("data/attendance.json")
    if not students:
        print("No students records found.")
        return

    print("\n====== Student Report ======")
    for student in students:
        print("\nStudent Information")
        print("Name: ", student['name'])
        print("Age: ", student['age'])
        print("Course: ", student['course'])
        print("College: ", student['college'])

        print("\nSubjects and Marks")
        if not subjects:
            print("No subjects records found.")
        else:
            for subject in subjects:
                print(subject['subject'], ":", subject['marks'])

        print("\nAcademic Result")
        if not subjects:
            print("Result cannot be calculated.")
        else:
            total_marks = 0
            for subject in subjects:
                total_marks = total_marks + subject['marks']
            percentage = (total_marks / (len(subjects)*100)) * 100        
            print("Total Marks: ", total_marks)
            print("Percentage: ", round(percentage, 2), "%")

            if percentage >= 90:
                print("Grade: A")
            elif percentage >= 80:  
                print("Grade: B")
            elif percentage >= 70:
                print("Grade: C")
            elif percentage >= 60:
                print("Grade: D")
            else:
                print("Grade: F")

        print("\nAttendance Records")
        if not attendance:
            print("No attendance records found.")
        else:
            for record in attendance:
                percentage = (record['attended_classes'] / record['total_classes']) * 100

                print(record["subject"], ":", round(percentage, 2), "%")

        print("\n-----------------------------------")
