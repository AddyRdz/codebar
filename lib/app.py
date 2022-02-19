# Write your code here!

class Member:
    def __init__(self, full_name):
        self.name = full_name
     

    def introduce(self):
        print(f"Hi, my name is {self.name}")

addy = Member ("Addy R.")
print(addy.name)
addy.introduce()

jane= Member("Jane Doe")
print(jane.name) #, jane.reason#

lena= Member("Lena Smith")
print(lena.name)

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
print(jane.reason)
lena = Student("lena Smitch", "I am really excited about learning to program!")
print(lena.reason)

class Instructor(Member):
    def __init__(self, full_name, bio, skills):
        super().__init_(full_name)
        self.bio = bio
        self.skills = ["Python, Javascript, C++"]
    
# Vicky Ruby - HTML, JavaScript
#    I want to help people learn coding.

#  Nicole McMillan - Ruby
#    I have been programming for 5 years in Ruby and want to spread the love

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

class Workshop:
    def __init__ (self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, participant):
        if isinstance(participant, Student):
            self.students.append(participant)

        elif isinstance(participant, Instructor):
            self.instructor.append(participant)

        # def print_details
        # .__class__
        # .__dict__
        # isinstance(...)
    
workshop = Workshop("12/03/2014", "Shutl")
workshop.add_participant(lena)
print(workshop.students)