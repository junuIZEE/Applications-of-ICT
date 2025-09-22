# This program takes in a user's marks and gives appropriate grade.

MARKS = int(input("Enter your marks: "))
GRADE = ""

MIN_MARKS = 0
MAX_MARKS = 100

# Compares the marks to a standard
if MARKS <= MAX_MARKS and MARKS >= MIN_MARKS:
    if MARKS >= 90 and MARKS <= MAX_MARKS:
        GRADE = "A"
    elif MARKS >= 75:
        GRADE = "B"
    elif MARKS >= 60:
        GRADE = "C"
    elif MARKS >= 50:
        GRADE = "D"
    else:
        GRADE = "F"
else:
    print("Marks fall outside a possible range.")

# Outputs the result based on marks
print(GRADE)
