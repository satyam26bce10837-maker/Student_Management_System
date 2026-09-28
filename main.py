from student import add_student, view_students, update_student, delete_student
from subjects import add_subject, view_subjects, update_subject, calculate_result, delete_subject
from attendance import add_attendance, view_attendance, calculate_attendance
from reports import student_report

# Display the main menu
while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Subject")
    print("6. View Subjects")
    print("7. Update Subject")
    print("8. Calculate Result")
    print("9. Delete Subject")
    print("10. Add Attendance")
    print("11. View Attendance")    
    print("12. Calculate Attendance")
    print("13. Generate Student Report")
    print("14. Exit")

    # Perform the operation based on the user's choice
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        add_subject()
    elif choice == "6":
        view_subjects()
    elif choice == "7":
        update_subject()
    elif choice == "8":
        calculate_result()
    elif choice == "9":
        delete_subject()
    elif choice == "10":
        add_attendance()
    elif choice == "11":
        view_attendance()
    elif choice == "12":
        calculate_attendance()  
    elif choice == "13":
        student_report()
    elif choice == "14":
        print("Thank you for using the system.")
        break
    else:
        print("Invalid choice! Please try again.")
