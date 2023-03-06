class Dog:

    legs_no = 4

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    @staticmethod
    def speak():
        return "ham ham ham"

    def __str__(self):
        return self.name


caine = Dog("Rex")
print()

