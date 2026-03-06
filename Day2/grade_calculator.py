# Beginner-friendly script to calculate student average and pass/fail status

while True:
    # Prompt the user for student's name (not used in calculation, but for personalization)
    student_name = input("Enter the student's name (or type 'Exit' to quit): ")
    if student_name.strip().lower() == 'exit':
        break

    # Prompt for three subject marks with validation
    while True:
        try:
            mark1 = float(input("Enter mark for subject 1 (0-100): "))
            if mark1 < 0 or mark1 > 100:
                print("Error: Marks must be between 0 and 100. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
    
    while True:
        try:
            mark2 = float(input("Enter mark for subject 2 (0-100): "))
            if mark2 < 0 or mark2 > 100:
                print("Error: Marks must be between 0 and 100. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
    
    while True:
        try:
            mark3 = float(input("Enter mark for subject 3 (0-100): "))
            if mark3 < 0 or mark3 > 100:
                print("Error: Marks must be between 0 and 100. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    # Calculate the average mark
    average = (mark1 + mark2 + mark3) / 3

    # Determine grade based on average
    if average >= 75:
        grade = "A"
    elif average >= 60:  # 60-74
        grade = "B"
    elif average >= 40:  # 40-59
        grade = "C"
    else:
        grade = "Fail"

    # Print a clean formatted summary
    print("------------------------------")
    print(f"Name   : {student_name}")
    print(f"Average: {average:.2f}")
    print(f"Grade  : {grade}")
    print("------------------------------")
    print()  # blank line before next iteration


