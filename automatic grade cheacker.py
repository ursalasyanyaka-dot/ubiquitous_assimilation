# automatic grade cheacker

Student_name = input("Enter student name: ")

Course_name = input("Enter your course: ")
# i used try and exception handling for error management.
try:
    Score = int(input("Enter your score: "))

    if Score in range(81,100): #used range to specify the limit of the points and then an elif for conditions
        print("Congratulations")
        print("Grade: A")
    elif Score in range(71,81):
        print("Congratulations")
        print("Grade: B")
    elif Score in range(61,71):
        print("Congratulations")
        print("Grade: C")
    elif Score in range(51,61):
        print("Congratulations")
        print("Grade: D")
    elif Score in range(0,51):
        print("Grade:")
    else:
        print("WHAT INPUT IS THIS?!")
except ValueError:
    print("INVALID INPUT")
