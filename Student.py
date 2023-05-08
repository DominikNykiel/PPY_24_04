class Student:
    def __init__(self, all_grade, email, name, surname):
        self.all_grade = all_grade
        self.email = email
        self.name = name
        self.surname = surname
        self.status = None

    def __str__(self):
        return "Email: " + self.email + "\nName: " + self.name + "\nSurname: " + self.surname + "\nAll grades: " + str(
            self.all_grade) + "\nStatus: " + str(self.status)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.email == other.email

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def compareStudentsNames(x, y):
        return x.name >= y.name

    @staticmethod
    def compareStudentsSurname(x, y):
        return x.surname >= y.surname

    @staticmethod
    def getPersonalData(self):
        return self.email, self.name, self.surname

