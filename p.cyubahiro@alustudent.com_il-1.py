# Define a class to represent an Assignment
class Assignment:
    def __init__(self, name, type, score, weight):
        # Initialize attributes for assignment name, type, score, and weight
        self.name = name
        self.type = type
        self.score = score
        self.weight = weight

    def weighted_score(self):
         # Calculate the weighted score as (score percentage * weight)
        return (self.score / 100)  * self.weight 
    
# Define a class to represent a Student
class Student:
    def __init__(self, name, surname, level):
        # Initialize attributes for student name, surname, level, and an empty list of assignments
        self.name = name
        self.surname = surname
        self.level = level
        self.assignments = []

    def add_assignment(self, assignment):
         # Add an assignment to the student's list of assignments
        self.assignments.append(assignment)

    def weighted_total(self):
        # Calculate the total weighted score for formative and summative assignments separately
        formative_group = sum(a.weighted_score() for a in self.assignments if a.type == "formative")
        summative_group = sum(a.weighted_score() for a in self.assignments if a.type == "summative")
        return formative_group, summative_group
    
    def total_sum(self):
       # Calculate the combined total of formative and summative weighted scores 
        formative_group, summative_group = self.weighted_total()
        return formative_group + summative_group
         
    def course_prog(self):
        # Check if the student has met the minimum requirements for passing the course
        # Formative >= 30%, Summative >= 20%
        formative_group, summative_group = self.weighted_total()
        return formative_group >= 30 and summative_group >= 20
    
    def resubm(self):
         # Identify assignments eligible for resubmission (score < 50 and formative type)
        return [a for a in self.assignments if a.score < 50  and a.type == "formative"]
    
    def transcript_gen(self, order="ascending"):
        # Generate and display the student's transcript
        # Sort assignments based on score in ascending or descending order
        sort = sorted(self.assignments, key=lambda x: x.score, reverse=(order == "descending"))
        print(f"\nThe Transcript for {self.name} {self.surname}:")
        print("\n")
        print("Assignment          Type            Score(%)    Weight (%)")
        print("-" * 59)
        for assignment in sort:
            print(f"{assignment.name:<15} {assignment.type:<10} {assignment.score:<10} {assignment.weight}")
        print("-" * 59)
        print(f"Final Grade: {self.total_sum():.2f}")

# Create the Instance objects for Student class

students =[
    Student("Proculla", "Giramata", "Y1T2"),
    Student("Rodrigo", "Gisubizo", "Y1T2"),
    Student("Bosco", "Eketike", "Y1T2"),
    Student("Nelea", "Wambua", "Y1T2"),
    Student("Eliab", "Tuyishime", "Y1T2")
]

# Create the object for assignment class

students[0].add_assignment(Assignment("Assignment 01", "formative", 97, 10))
students[0].add_assignment(Assignment("Assignment 02", "formative", 100, 20))
students[0].add_assignment(Assignment("Mid-term", "summative", 87, 20))
students[0].add_assignment(Assignment("Assignment 03", "formative", 75, 30))
students[0].add_assignment(Assignment("Final exam", "summative", 92, 20))

students[1].add_assignment(Assignment("Assignment 01", "formative", 90, 10))
students[1].add_assignment(Assignment("Assignment 02", "formative", 100, 20))
students[1].add_assignment(Assignment("Mid-term", "summative", 75, 20))
students[1].add_assignment(Assignment("Assignment 03", "formative", 75, 30))
students[1].add_assignment(Assignment("Final exam", "summative", 96, 20))

students[2].add_assignment(Assignment("Assignment 01", "formative", 55, 10))
students[2].add_assignment(Assignment("Assignment 02", "formative", 25, 20))
students[2].add_assignment(Assignment("Mid-term", "summative", 68, 20))
students[2].add_assignment(Assignment("Assignment 03", "formative", 15, 30))
students[2].add_assignment(Assignment("Final exam", "summative", 92, 20))
           
students[3].add_assignment(Assignment("Assignment 01", "formative", 90, 10))
students[3].add_assignment(Assignment("Assignment 02", "formative", 60, 20))
students[3].add_assignment(Assignment("Mid-term", "summative", 30, 20))
students[3].add_assignment(Assignment("Assignment 03", "formative", 75, 30))
students[3].add_assignment(Assignment("Final exam", "summative", 12, 20))

students[4].add_assignment(Assignment("Assignment 01", "formative", 93, 10))
students[4].add_assignment(Assignment("Assignment 02", "formative", 80, 20))
students[4].add_assignment(Assignment("Mid-term", "summative", 87, 20))
students[4].add_assignment(Assignment("Assignment 03", "formative", 75, 30))
students[4].add_assignment(Assignment("Final Exam", "summative", 72, 20))

# Define a method to prompt the user inputs and run a program
def ask():
    print("Available Students:")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student.name} {student.surname}")

    choice = input("Select a student by number (or type 'exit' to quit): ").strip()
    if choice.lower() == "exit":
        print("Goodbye!")
        return

    try:
        choice = int(choice) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 <= choice < len(students):
        selected_student = students[choice]
    else:
        print("Invalid choice\nPlease try again!")
        return
    
    print(f"\n{selected_student.name} {selected_student.surname} - Progress check:")
    if selected_student.course_prog():
        print("Student has passed the course.")
    else:
        print("Student has failed and must retake the course.")

    resubmissions = selected_student.resubm()
    if resubmissions:
        print("\nAssignments eligible for resubmission:")
        for a in resubmissions:
            print(f"{a.name} - Score: {a.score}%")
    else:
        print("\nNo assignments eligible for resubmission.")
    
    order = input("Display transcript in ascending or descending order? ").strip().lower()
    order = order if order in ["ascending", "descending"] else "ascending"
    selected_student.transcript_gen(order=order)

ask()

