#Bank Management System Project By Samarth Bagul
import pickle
import os
import time
import emoji
import pathlib
import pyttsx3
import speech_recognition as sr

os.system("cls")

# !voice
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def playVoices():
    if __name__ == "__main__":
        speak(addVoice)


global addVoice


class Account:
    accNo = 0
    name = ""
    deposit = 0
    type = ""

    def createAccount(self):
        self.accNo = int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = int(
            input("Enter The Initial amount(>=500 for Saving and >=1000 for current")
        )
        print("\n\n\nAccount Created")

    def showAccount(self):
        print("Account Number : ", self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account", self.type)
        print("Balance : ", self.deposit)

    def modifyAccount(self):
        print("Account Number : ", self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def intro():
    print("\t\t\t\t**************************")
    print("\t\t\t\t--BANK MANAGEMENT SYSTEM--")
    print("\t\t\t\t**************************")
    print("\t\t\t\t=====Brought To You By=====")
    print("\t\t\t\t\tSamarth Bagul")


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)
        infile.close()
    else:
        print("No records to display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("Your account Balance is = ", item.deposit)
                found = True
    else:
        print("No records to Search")
    if not found:
        print("No existing record with this number")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()
        os.remove("accounts.data")
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:

                        print("You cannot withdraw larger amount")
                        

    else:
        print("No records to Search")
    outfile = open("newaccounts.data", "wb")
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename("newaccounts.data", "accounts.data")


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove("accounts.data")
        outfile = open("newaccounts.data", "wb")
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename("newaccounts.data", "accounts.data")


def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        oldlist = pickle.load(infile)
        infile.close()
        os.remove("accounts.data")
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open("newaccounts.data", "wb")
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename("newaccounts.data", "accounts.data")


def writeAccountsFile(account):

    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove("accounts.data")
    else:
        oldlist = [account]
    outfile = open("newaccounts.data", "wb")
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename("newaccounts.data", "accounts.data")


# start of the program
ch = ""
num = 0
intro()
addVoice = """Welcome to our BANK MANAGEMENT SYSTEM
\nBrought To You By\n Samarth Bagul"""
playVoices()
time.sleep(5)


print("\tMAIN MENU")
print("\t1. NEW ACCOUNT")
print("\t2. DEPOSIT AMOUNT")
print("\t3. WITHDRAW AMOUNT")
print("\t4. BALANCE ENQUIRY")
print("\t5. ALL ACCOUNT HOLDER LIST")
print("\t6. CLOSE AN ACCOUNT")
print("\t7. MODIFY AN ACCOUNT")
print("\t8. EXIT")
print("\tSelect Your Option (1-8) ")
ch = input()


if ch == "1":
    addVoice = "Welcome Customer \n create your account here"
    playVoices()
    writeAccount()
    addVoice = "your account is successfully created "
    playVoices()
elif ch == "2":
    num = int(input("\tEnter the account No. : "))
    depositAndWithdraw(num, 1)
elif ch == "3":
    addVoice = "please enter your personal information with security"
    playVoices()
    num = int(input("\tEnter The account No. : "))
    if num:
        depositAndWithdraw(num, 2)
        addVoice = "withdrawing amount please wait"
        playVoices()
        print('press enter to know your remaining balance')
        input()
        print('----your current balance is as follows----')
        displaySp(num)
        addVoice = "thank you \n visit again"
        playVoices()

    else:
        addVoice = "there is no such account in directory"
        playVoices()


elif ch == "4":
    num = int(input("\tEnter The account No. : "))
    displaySp(num)
elif ch == "5":
    displayAll()
elif ch == "6":
    num = int(input("\tEnter The account No. : "))
    deleteAccount(num)
    addVoice = "dear Customer \n your account will be permanently deleted"
    playVoices()

elif ch == "7":
    num = int(input("\tEnter The account No. : "))
    modifyAccount(num)
    addVoice = " your account will be modified soon"
    playVoices()
elif ch == "8":
    addVoice = "Thanks for using bank management system \n see you   again"
    playVoices()
    print("\tThanks for using bank management system")
    exit()
else:
    addVoice = "dear Customer \n please enter valid information"
    playVoices()


