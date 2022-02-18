# Write your code here!

class Member:
    def __init__(self, full_name):
        self.name = full_name
     

    def introduce(self):
        print(f"Hi, my name is {self.name}")

addy = Member ("Addy R.")
print(addy.name)
addy.introduce()

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

class Instructor(Member):
    def __init__(self, full_name, bio, skills):
        super().__init_(full_name)
        self.bio = bio
        self.skills = []
    
    def __init__(self, new_skill):
        self.skills.append(new_skill)
        
    