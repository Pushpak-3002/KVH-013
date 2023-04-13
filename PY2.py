class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.roll)
        print(self.marks)

    def profile(self):
        self.city="Kolkata"

S=student('aaa',28,75)
print(S.__dict__)
S.marks=45
print(S.__dict__)
S.grade="A"
print(S.__dict__)
S.profile()
print(S.__dict__)
del S.marks
print(S.__dict__)
        
