class Bird:

    def __init__(self):
        print("The Bird is ready.")
    def Who(self):
        print("Bird")
    def swiming(self):
        print("Fly faster!")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("The Penguin is ready.")
        super().Who()
        
    def Who(self):
        print("Penguin")
    def Running(self):
        print("Run faster!")

var1 = Penguin()

var1.Who()
var1.swiming()
var1.Running()
