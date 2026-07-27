class Lion :
    def Sound(self):
        print("roar")

class Cow:
    def Sound(self):
        print("moo")

def Show(animal):
    animal.Sound()

lion=Lion()
cow=Cow()

Show(lion)
Show(cow)