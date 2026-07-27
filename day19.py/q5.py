class ATM:
    def __init__(self):
        self.__pin=143

    def change_pin(self,new_pin):
        self.__pin=new_pin

    def show_pin(self):
        return self.__pin
        
atm=ATM()
atm.change_pin(678)
print(atm.show_pin())