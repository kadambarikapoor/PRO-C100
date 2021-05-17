from typing import Mapping


class ATM:
    def __init__(self, cardNumber, pin):
        self.cardNumber=cardNumber
        self.pin=pin

    def CheckBalance(self):
        print("Your balance is 50,000")

    def whithdrawl(self, ammount):
        new_ammount=50000-ammount
        print("You have withdrawn"+str(ammount)+"Your remaining balance is"+str(new_ammount))
    
def main():
        cardNummber=input("Card Number ")
        pin=input("Pin ")
        new_user=ATM(cardNummber,pin)
        print("Choose Activity ")
        print("1:", "2")
        activity=int(input("Enter Activity Number "))
        if(activity==1):
            new_user.CheckBalance()
        elif(activity==2):
            ammount=int(input("Enter the ammount "))
            new_user.whithdrawl(ammount)
        else:
            print("Enter a valid number.")

if __name__== "__main__" :
    main()