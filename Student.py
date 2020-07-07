# Class = define your own datatype!

# class StudentClass:
#
#     def __init__(self, name, major, gpa, is_on_probation):
#       self.name = name
#       self.major = major
#       self.gpa = gpa
#       self.is_on_probation = is_on_probation


class StudentClass2:

    def __init__(self, name, major, gpa):
      self.name = name
      self.major = major
      self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
