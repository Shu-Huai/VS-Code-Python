import types


class Person(object):
    def __init__(self, name="", age=20, sex="man"):
        self.SetName(name)
        self.SetAge(age)
        self.SetSex(sex)

    def SetName(self, name):
        if not isinstance(name, str):
            print("name must be string.")
            return
        self.__name = name

    def SetAge(self, age):
        if not isinstance(age, int):
            print("age must be integer.")
            return
        self.__age = age

    def SetSex(self, sex):
        if sex != "man" and sex != "woman":
            print('sex must be "man" or "woman"')
            return
        self.__sex = sex

    def Show(self):
        print(self.__name)
        print(self.__age)
        print(self.__sex)


class Student(Person):
    def __init__(self, name="", age=30, sex="male", major="Computer"):
        super(Student, self).__init__(name, age, sex)
        self.SetMajor(major)

    def SetMajor(self, major):
        if not isinstance(major, str):
            print("Major must be a string.")
            return
        self.__major = major

    def Show(self):
        super(Student, self).Show()
        print(self.__major)


if __name__ == "__main__":
    liSi = Student("Li Si", 32, "male", "Math")
    liSi.Show()