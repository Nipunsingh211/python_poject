students=[]
while True:
    print("------Student Management System-------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        roll = input("Enter student roll number: ")
        mobile_no = input("Enter student Mobile number: ")
        student = {
            "name": name,
            "roll": roll,
            "mobile": mobile_no
        }
        students.append(student)
        print("Student added.")

    elif choice == '2':
        if not students:
            print("No students found.")
        else:
            for s in students:
                print(f"Name: {s['name']}, Roll: {s['roll']}, Mobile: {s['mobile']}")

    elif choice == '3':
        key = input("Enter roll number to search: ")
        found = [s for s in students if s['roll'] == key]
        if found:
            for s in found:
                print(f"Found - Name: {s['name']}, Roll: {s['roll']}, Mobile: {s['mobile']}")
        else:
            print("Student not found.")

    elif choice == '4':
        key = input("Enter roll number to delete: ")
        before = len(students)
        students = [s for s in students if s['roll'] != key]
        if len(students) < before:
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == '5':
        key = input("Enter roll number to update: ")
        for s in students:
            if s['roll'] == key:
                s['name'] = input(f"Enter new name (current: {s['name']}): ") or s['name']
                s['mobile'] = input(f"Enter new mobile (current: {s['mobile']}): ") or s['mobile']
                print("Student updated.")
                break
        else:
            print("Student not found.")

    elif choice == '6':
        print("Thanks!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        
    
   



