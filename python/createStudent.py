students = {}

def create_student():
    print("\n--- Create New Student Profile ---")

    student_id = input("Student ID: ").strip()

    # Check if ID already exists
    if student_id in students:
        print("Student ID already exists!\n")
        return

    full_name = input("Full Name: ").strip()
    major = input("Major: ").strip()

    # Save student
    students[student_id] = {
        "name": full_name,
        "major": major
    }

    print(f"\n[✓] Profile created successfully!")
    print(f"ID: {student_id} | Name: {full_name} | Major: {major}\n")


def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No student records found.\n")
        return

    for sid, info in students.items():
        print(f"{sid} - {info['name']} ({info['major']})")

    print()


def main():
    while True:
        print("===== MENU =====")
        print("1. Create Student Profile")
        print("2. View Students")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option\n")


if __name__ == "__main__":
    main()