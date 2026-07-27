class Bird():
    def Fly(self):
        print("Bird is Flying")

class Parrot(Bird):
    def Talk(self):
        print("parrot is talking")
parrot1=Parrot()
parrot1.Talk()
parrot1.Fly()
