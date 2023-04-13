class student:
    '''This is a class'''
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def __str__(self):
        return "This is student class"
    def display(self):
        print("Student Name : ",self.name)
        print("Student Roll : ",self.roll)
        print("Student Marks : ",self.marks)

S=[student('aaa',77,8.9),
   student('bbb',79,8.6),
   student('ccc',78,8.5)]

for  i in S :
   i.display()
