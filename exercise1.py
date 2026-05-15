def main():
    students = []
    
    # 1. Input the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students >= 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # 2. Input student information
    for i in range(num_students):
        print(f"\n--- Entering information for student {i+1} ---")
        student_id = input("Student ID: ")
        full_name = input("Full name: ")
        while True:
            try:
                python_score = float(input("Python score: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number for the score.")
        
        # 3. Store all students in a list of dictionaries
        student = {
            "Student ID": student_id,
            "Full name": full_name,
            "Python score": python_score
        }
        students.append(student)
        
    print("\n==================================")
    
    # 4. Display
    # All students
    print("\n--- All Students ---")
    if not students:
        print("No students recorded.")
        return
        
    for s in students:
        print(f"ID: {s['Student ID']}, Name: {s['Full name']}, Score: {s['Python score']}")
        
    # The student with the highest score
    highest_score_student = max(students, key=lambda x: x["Python score"])
    print("\n--- Student with the Highest Score ---")
    print(f"ID: {highest_score_student['Student ID']}, Name: {highest_score_student['Full name']}, Score: {highest_score_student['Python score']}")
    
    # The average score
    total_score = sum(s["Python score"] for s in students)
    average_score = total_score / len(students)
    print(f"\n--- Average Score ---")
    print(f"{average_score:.2f}")
    
    # Students who passed (score >= 5)
    print("\n--- Students who passed (score >= 5) ---")
    passed_students = [s for s in students if s["Python score"] >= 5]
    if passed_students:
        for s in passed_students:
             print(f"ID: {s['Student ID']}, Name: {s['Full name']}, Score: {s['Python score']}")
    else:
        print("No students passed.")

if __name__ == "__main__":
    main()
