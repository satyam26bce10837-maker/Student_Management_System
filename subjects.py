from storage import load_data, save_data

# Add a new subject to the system
def add_subject():
    subjects = load_data("data/subjects.json")

    subject_name = input("Enter subject name: ")

    try:
        marks = int(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return    

    subject = {
        "subject": subject_name,
        "marks": marks
    }

    subjects.append(subject)
    save_data("data/subjects.json", subjects)
    print("Subject added successfully!")

# Display the list of subjects in the system
def view_subjects():
    subjects = load_data("data/subjects.json")
    if not subjects:
        print("No subjects found.")
        return

    print("\n====== Subject List ======")
    for subject in subjects:
        print("Subject: ", subject['subject'])
        print("Marks: ", subject['marks'])
        print("---------------------------")   

# Update the details of an existing subject in the system
def update_subject():
    subjects = load_data("data/subjects.json")
    subject_name = input("Enter the name of the subject to update: ")

    for subject in subjects:
        if subject['subject'].lower() == subject_name.lower():
            try:
                new_marks = int(input("Enter new marks: ")) or subject['marks']

                if new_marks < 0 or new_marks > 100:
                    print("Marks should be between 0 and 100.")
                    return
            except ValueError:
                print("Please enter valid marks.")
                return    
            
            subject['marks'] = new_marks
            
            save_data("data/subjects.json", subjects)
            print("Subject updated successfully!")
            return

    print("Subject not found.")    

# Calculate percentage and grade
def calculate_result():
    subjects = load_data("data/subjects.json")
    if not subjects:
        print("No subjects found.")
        return

    total_marks = 0

    for subject in subjects:
        total_marks = total_marks + subject['marks']

    percentage = total_marks / len(subjects)


    print("\n====== Result ======")
    print("Total Marks: ", total_marks)
    print("Percentage: ", percentage)         

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

# Delete a subject from the system
def delete_subject():
    subjects = load_data("data/subjects.json")
    subject_name = input("Enter the name of the subject to delete: ")

    for subject in subjects:
        if subject['subject'].lower() == subject_name.lower():
            subjects.remove(subject)
            save_data("data/subjects.json", subjects)
            print("Subject deleted successfully!")
            return

    print("Subject not found.")