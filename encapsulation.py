
class Student:
     def __init__(self, name, marks):
         self.name = name
 #Public variable
         self.marks = marks
 #Private variable
     def get_marks(self):
 #Public method
         return self.marks
     def set_marks(self, marks):
         if marks >= 0:
            self.marks = marks







