# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}.")

# Child class: Student
class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

# Child class: Teacher
class Teacher(Person):
    def __init__(self, name, subject):  # ✅ Fixed constructor name
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching.")

    def learn(self):  # ✅ Removed extra subject parameter
        print(f"{self.name} is a {self.subject} teacher.")  # ✅ Fixed spelling

# Using the classes
p = Person("Alex")
p.greet()

s = Student("Prabhu")
s.greet()
s.study()

t = Teacher("Ashish", "Math")  # ✅ Passed both name and subject
t.greet()
t.teach()
t.learn()


