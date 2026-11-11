#this program will capture up to 10 grades entered by the user

#this prompts the user for input
numberOfGrades = int(input("Enter the number of grades you want? "))

#this is my accumulator/counter for my while loop
counter = 0

while counter < numberOfGrades:
    grade = input("Enter your grade: ")
    print(grade)
    counter = counter + 1


