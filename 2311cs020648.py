def calculate_grade():
    # Take input for marks in three subjects
    try:
        subject1 = float(input("Enter marks for Subject 1: "))
        subject2 = float(input("Enter marks for Subject 2: "))
        subject3 = float(input("Enter marks for Subject 3: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate the average
    average = (subject1 + subject2 + subject3) / 3

    # Determine the grade
    if average >= 90:
        grade