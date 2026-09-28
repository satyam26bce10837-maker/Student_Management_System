from storage import load_data, save_data

# Add a new attendance record to the system
def add_attendance():
    attendance = load_data("data/attendance.json")

    subject_name = input("Enter subject name: ")
    if not subject_name.strip():
        print("Subject name cannot be empty.")
        return
    try:
        total = int(input("Enter the total classes: "))
        attended = int(input("Enter the classes attended: "))

        if total <= 0 or attended < 0:
            print("Total and attended classes must be positive numbers.")
            return
        if attended > total:
            print("Attended classes cannot be greater than total classes.")
            return
    except ValueError:
        print("Please enter valid numbers for total and attended classes.")
        return

    record = {
        "subject": subject_name,
        "total_classes": total,
        "attended_classes": attended
    }
    attendance.append(record)
    save_data("data/attendance.json", attendance)

    print("Attendance record added successfully!")

# Display the list of attendance records in the system
def view_attendance():
    attendance = load_data("data/attendance.json")
    if not attendance:
        print("No attendance records found.")
        return

    print("\n====== Attendance Records ======")
    for record in attendance:
        print("Subject: ", record['subject'])
        print("Total Classes: ", record['total_classes'])
        print("Attended Classes: ", record['attended_classes'])
        print("---------------------------")

# Calculate the attendance percentage for each subject
def calculate_attendance():
    attendance = load_data("data/attendance.json")
    if not attendance:
        print("No attendance records found.")
        return

    print("\n====== Attendance Percentage ======")
    for record in attendance:
        percentage = (record['attended_classes'] / record['total_classes']) * 100
        print("Subject: ", record['subject'])
        print("Attendance: ", percentage, "%")
        if percentage < 75:
            print("Warning: Attendance is below 75%!")
        else:
            print("Attendance is satisfactory.")        
        print("---------------------------")

