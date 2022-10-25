import random
import tkinter.messagebox


class WashingCard:
    ''' Class to represent a washing card that the user will use '''

    # Initializer
    def __init__(self, cardDigit, balance=0.0, points=0, typeUser='', userID = 0):
        self.cardDigit = cardDigit
        self.balance = balance
        self.points = points
        # self.user = User
        self.typeUser = typeUser
        self.userID = userID

    # setter and getter methods
    def setcardDigit(self, cardDigit):
        self.cardDigit = cardDigit

    def getcardDigit(self):
        return self.cardDigit

    def setbalance(self, balance):
        self.balance = balance

    def getbalance(self):
        return self.balance

    def setpoints(self, points):
        self.points = points

    def getpoints(self):
        return self.points

    def settypeUser(self, typeUser):
        self.typeUser = typeUser

    def gettypeUser(self):
        return self.typeUser

    def setuserID(self, userID):
        self.userID = userID

    def getuserID(self):
        return self.userID


    # Generate unique digit ID for the wash card
    def UniqueDigit(self):
        generateDigit = str(random.randint(0, 999999))
        return "ID" + generateDigit

    # Create a washing card for the user
    def CreateWashCard(self):

        # check card digit if it is unique or not
        store = self.UniqueDigit()
        find = open("records.txt", "r")
        for line in find:
            print(line)
            word = line.split(",")
            if (word[6]) == store:
                self.CreateWashCard()

        # Set card id number, balance, and points
        self.setbalance(0)
        self.setcardDigit(self.UniqueDigit())
        if self.gettypeUser() == 'Gold Member':
            self.setpoints(500)
        elif self.gettypeUser() == 'Silver Member':
            self.setpoints(300)
        else:
            self.setpoints(0)


class User:
    ''' Class to represent the users of CleanCar.com '''

    # Initializer
    def __init__(self, fullName='', userName='', password='', address='', telephone='', email='', accountCategory="",
                 recordNum=0):
        self.fullName = fullName
        self.username = userName
        self.password = password
        self.address = address
        self.telephone = telephone
        self.email = email
        self.accountCategory = accountCategory
        self.recordNum = recordNum
        # composition with class WashingCard
        self.washCard = WashingCard(None, None)

    # setter and getter methods
    def setfullName(self, fullName):
        self.fullName = fullName

    def getfullName(self):
        return self.fullName

    def setuserName(self, userName):
        self.userName = userName

    def getuserName(self):
        return self.userName

    def setpassword(self, password):
        self.password = password

    def getpassword(self):
        return self.password

    def setaddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def settelephone(self, telephone):
        self.telephone = telephone

    def gettelephone(self):
        return self.telephone

    def setemail(self, email):
        self.email = email

    def getemail(self):
        return self.email

    def setaccountCategory(self, accountCategory):
        self.accountCategory = accountCategory

    def getaccountCategory(self):
        return self.accountCategory

    def setrecordNum(self, recordNum):
        self.recordNum = recordNum

    def getrecordNum(self):
        return self.recordNum

    # function for new user registration
    def Registration(self, rgFullName, rgUsername, rgPassword, rgAddress, rgEmail, rgphone, rgType="Manager"):
        # set values to each attributes
        self.setfullName(rgFullName)
        self.setuserName(rgUsername)
        self.setpassword(rgPassword)
        self.setaddress(rgAddress)
        self.setemail(rgEmail)
        self.settelephone(rgphone)
        self.setaccountCategory(rgType)
        self.washCard.settypeUser(rgType)
        self.washCard.CreateWashCard()

        # set record number
        rgrecordNum = 0
        find = open("webUser.txt", "r")
        for num in find:
            numSplit = num.split(",")
            if int(numSplit[0]) >= rgrecordNum:
                rgrecordNum += 1

        self.setrecordNum(str(rgrecordNum))

        # write all user details in the records file

        write = open("webUser.txt", "a", newline='')
        write.writelines(
            str(self.getrecordNum()) + "," +
            self.getuserName() + "," +
            self.getpassword() + "\n"
        )

        # write all user details in the records file

        write = open("records.txt", "a", newline='')
        write.writelines(
            str(self.getrecordNum()) + "," +
            self.getfullName() + "," +
            self.getaccountCategory() + "," +
            self.getaddress() + "," +
            self.getemail() + "," +
            self.gettelephone() + "," +
            self.washCard.getcardDigit() + "," +
            str(self.washCard.getbalance()) + "," +
            str(self.washCard.getpoints()) + "\n"
        )
        tkinter.messagebox.showinfo(title="Registration Info",
                                    message="Congrats, you have been successfully registered with CleanCar.com!. You can login right away!")

    # Funtion for user log in
    def LogIn(self, username, password):
        check = False
        find = open("webUser.txt", "r")
        for num in find:
            numSplit = num.split(",")
            print(numSplit[1] + "-" + numSplit[2] + "-")
            global idValue
            idValue = numSplit[0]
            self.setrecordNum(idValue)
            # self.washCard.setuserID(self.getrecordNum)
            ##########################################################################################################
            print('!!!!!!!!!', self.washCard.getuserID())
            if numSplit[1] == username and numSplit[2] == password + "\n":
                session = open("session.txt", "w")
                session.write(idValue)

                print('IDIDIDIDIDID', numSplit[0], self.getrecordNum())
                tkinter.messagebox.showinfo(title="Login Info ", message="You have successfully Logged In!")
                check = True
                return check
        if check == False:
            tkinter.messagebox.showerror(title="Login Error ",
                                         message="Your account not found, please check your Username or Password. If you are a new user, please Register")

    # function to Update user info
    def modifyUserInfo(self, fullname, username, password, address, email, phone):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())

        # edit records file
        global Split
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        Split[1] = fullname
        Split[3] = address
        Split[4] = email
        Split[5] = phone
        fullString = ','.join([str(i) for i in Split])
        lines[updateID] = fullString
        # write to replace
        write = open("records.txt", "w")
        write.writelines(lines)
        write.close()

        # edit wordUser file
        file = open("webUser.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        Split[1] = username
        Split[2] = password + "\n"
        fullString = ','.join([str(i) for i in Split])
        lines[updateID] = fullString
        # write to replace
        write = open("webUser.txt", "w")
        write.writelines(lines)
        write.close()
        tkinter.messagebox.showinfo(title="Update Info ",
                                    message="Success Updating Info")


    # function update the points of a user after modifying his details
    # def modifyPoints(self):
    #     print("Split 2 --", Split[2])
    #     print("Copycat--", copycat)
    #     if Split[2] != copycat:
    #         if copycat == 'Gold Member':
    #             return 500
    #         elif copycat == 'Silver Member':
    #             return 300
    #         else:
    #             return 0


    # function to show the user data
    def oldData(self, x):
        oldList = []
        ID = 1
        # read file
        file1 = open("records.txt", "r")
        lines1 = file1.readlines()
        Split1 = lines1[ID].split(",")
        oldList.append(Split1[1])
        oldList.append(Split1[2])
        oldList.append(Split1[3])
        oldList.append(Split1[4])
        oldList.append(Split1[5])
        file2 = open("webUser.txt", "r")
        lines1 = file2.readlines()
        Split2 = lines1[ID].split(",")
        oldList.append(Split2[1])
        oldList.append(Split2[2][:-2])
        return oldList[x]

    # function fro to check if employee or not
    def stuffOnly(self):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())

        # edit records file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        print(Split)
        print(Split[2])
        if Split[2] == "Regular Employee" or Split[2] == "Manager":

            return True
        else:
            tkinter.messagebox.showerror(title="Error Info ",
                                        message="This is stuff only! You are not a Manager or Employee.")

            return False



class RegularUser(User):
    ''' Class to represent a regular user of CleanCar '''

    # Initializer
    def __init__(self, fullName='', userName='', password='', address='', telephone='', email='', accountCategory="",
                 recordNum=0):
        User.__init__(self, fullName, userName, password, address, telephone, email, accountCategory, recordNum)


class Employee(User):
    ''' Class to represent an Employee of CleanCar Company '''

    # Initializer
    def __init__(self, fullName='', userName='', password='', address='', telephone='', email='', accountCategory="",
                 recordNum=0):
        User.__init__(self, fullName, userName, password, address, telephone, email, accountCategory, recordNum)

    # function to allows Manager to view all the users details
    def DisplayInfoPrivilage(self):
        display = ""
        file = open("records.txt", "r")
        lines = file.readlines()
        # print(lines, len(lines))
        # print(len(lines))
        # print(lines[0])
        for i in range(0, len(lines)):
            # print("iiiii", i)
            display = display + lines[i] + '\n'
        return display


class RegularEmployee(Employee):
    ''' Class to represent a Regular Employee of CleanCar Company '''

    # Initializer
    def __init__(self, fullName='', userName='', password='', address='', telephone='', email=''):
        Employee.__init__(self, fullName, userName, password, address, telephone, email)


class Manager(Employee):
    """ Class to represent a Manager in CleanCar Company """

    # Initializer
    def __init__(self, fullName='', userName='', password='', address='', telephone='', email=''):
        Employee.__init__(self, fullName, userName, password, address, telephone, email)

    # function to delete all the user data stored in the record and washUser files
    def DeleteAll(self):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())

        # edit records file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        # print(Split[2])
        # print(Split)
        if Split[2] == "Manager":
            remove1 = open("records.txt", "r+")
            remove1.truncate(0)
            remove1.close()
            remove2 = open("webUser.txt", "r+")
            remove2.truncate(0)
            remove2.close()
            remove3 = open("products&prices.txt", "r+")
            remove3.truncate(0)
            remove3.close()

        else:
            tkinter.messagebox.showerror(title="Privileges Info ",
                                        message="You don't have the right to delete accounts! You are not a Manager.")


class CleaningServices:
    """ Class to represent the Cleaning Services available"""

    # Initializer
    def __init__(self, serviceName='', servicePrice=0.0, serviceDescription=''):
        self.serviceName = serviceName
        self.servicePrice = servicePrice
        self.serviceDescription = serviceDescription
        # WashingCard.__init__(cardDigit, balance, points, typeUser)

    # getter and setter

    def setserviceName(self, serviceName):
        self.serviceName = serviceName

    def getserviceName(self):
        return self.serviceName

    def setservicePrice(self, servicePrice):
        self.servicePrice = servicePrice

    def getservicePrice(self):
        return self.servicePrice

    def setserviceDescription(self, serviceDescription):
        self.serviceDescription = serviceDescription

    def getserviceDescription(self):
        return self.serviceDescription

    # displaying
    def displayService(self):
        return self.serviceName + ", " + str(self.servicePrice) + ", " + self.serviceDescription


class RegularWash(CleaningServices):
    """ Class to represent Regular wash service"""

    # Initializer
    def __init__(self, serviceName='Regular Wash', servicePrice=50.0, serviceDescription='Typical normal wash'):
        CleaningServices.__init__(self, serviceName, servicePrice, serviceDescription)


class DeepWash(CleaningServices):
    """ Class to represent Deep wash service"""

    # Initializer
    def __init__(self, serviceName='Deep Wash', servicePrice=70.0, serviceDescription='A vey detailed deep cleaning'):
        CleaningServices.__init__(self, serviceName, servicePrice, serviceDescription)


class SteamCleaning(CleaningServices):
    """ Class to represent Steam cleaning service"""

    # Initializer
    def __init__(self, serviceName='Steam Cleaning', servicePrice=100.0,
                 serviceDescription='Cleaning using only steam'):
        CleaningServices.__init__(self, serviceName, servicePrice, serviceDescription)


class EngineOiling(CleaningServices):
    """ Class to represent Regular wash service"""

    # Initializer
    def __init__(self, serviceName='EngineOiling', servicePrice=90.0,
                 serviceDescription='Refill the oil in the engine'):
        CleaningServices.__init__(self, serviceName, servicePrice, serviceDescription)


class TireCheckUp(CleaningServices):
    """ Class to represent Tire checkup service"""

    # Initializer
    def __init__(self, serviceName='Tire CheckUp', servicePrice=60.0, serviceDescription='Check for tire status'):
        CleaningServices.__init__(self, serviceName, servicePrice, serviceDescription)


class Transaction:
    """ Class to represent all the transactions that a user makes """

    # Initializer
    # def __init__(self, amountTopUp=0, amountPay=0, fullName='', userName='', password='', address='', telephone='', email='', accountCategory="",
    #              recordNum=0):
    #     self.amountTopUp = amountTopUp
    #     self.amountPay = amountPay
    #     User.__init__(self, fullName, userName, password, address, telephone, email, accountCategory, recordNum)

    def __init__(self, amountTopUp=0, amountPay=0):
        self.amountTopUp = amountTopUp
        self.amountPay = amountPay
        self.card = WashingCard(None, None)

    # getter and setter
    def setamountTopUp(self, amountTopUp):
        self.amountTopUp = amountTopUp

    def getamountTopUp(self):
        return self.amountTopUp

    def setamountPay(self, amountPay):
        self.amountPay = amountPay

    def getamountPay(self):
        return self.amountPay


    # Function for money top up
    def TopUp(self, amount):
        userID = open("session.txt", "r")
        ID = int(userID.read())
        # read file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[ID].split(",")
        Split[7] = str(float(Split[7]) + amount)
        fullString = ','.join([str(i) for i in Split])
        lines[ID] = fullString
        # write to replace
        write = open("records.txt", "w")
        write.writelines(lines)
        write.close()
        tkinter.messagebox.showinfo(title="Top Up Info ",
                                    message="Success Top Up")

    # function to calculate the discount a user have
    def Discount(self):
        userID = open("session.txt", "r")
        ID = int(userID.read())
        # print("IDIDIDIDIDIDIDID", ID)
        # read file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[ID].split(",")
        # print("SSSSSSSplit", Split[2] + "---")
        if Split[2] == "Regular Member":
            return 0.15
        elif Split[2] == "Regular Employee":
            return 0.30
        elif Split[2] == "Manager":
            return 0.50
        elif Split[2] == "Gold Member":
            return 0.35
        elif Split[2] == "Silver Member":
            return 0.25
        else:
            return 0.0

    # function to calculate the price with Discount
    def PriceWithDiscount(self):
        return service.getservicePrice() - self.Discount() * service.getservicePrice()

    # Function of user payment of services
    def Payment(self, Name):
        # specify the price
        global service
        if Name == "Regular Wash":
            service = RegularWash()
        elif Name == "Deep Wash":
            service = DeepWash()
        elif Name == "Steam Cleaning":
            service = SteamCleaning()
        elif Name == "Engine Oiling":
            service = EngineOiling()
        elif Name == "Tire CheckUp":
            service = TireCheckUp()

        # price including discount
        cashDiscount = self.PriceWithDiscount()
        # price without discount
        cash = service.getservicePrice()

        # check if user have enough money
        userID = open("session.txt", "r")
        ID = int(userID.read())
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[ID].split(",")

        if float(Split[7]) < cashDiscount:
            tkinter.messagebox.showinfo(title="Payment Info ", message="You don't have enough money, please recharge your balance")
        else:
            purch = open("products&prices.txt", 'a')
            purch.write(' ' + Name + '\n')

            self.purchaseList()

            userID = open("session.txt", "r")
            ID = int(userID.read())
            # read file
            file = open("records.txt", "r")
            lines = file.readlines()
            Split = lines[ID].split(",")
            Split[7] = str(float(Split[7]) - self.PriceWithDiscount())
            fullString = ','.join([str(i) for i in Split])
            lines[ID] = fullString
            # write to replace
            write = open("records.txt", "w")
            write.writelines(lines)
            write.close()
            tkinter.messagebox.showinfo(title="Payment Info ", message="Congrats, you bought a service")


    # function to show all the user details
    def showpurchaseList(self):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())

        # edit records file
        f = open("records.txt", "r")
        lines = f.readlines()
        Split = lines[updateID].split(",")
        if Split[2] == "Manager":
            display = ""
            file = open("products&prices.txt", "r")
            lines = file.readlines()
            for i in range(0, len(lines)):
                # print("iiiii", i)
                display = display + lines[i] + '\n'
            return display

        else:
            tkinter.messagebox.showerror(title="Privileges Info ",
                                        message="You don't have the right to see purchase! You are not a Manager.")



    # function to store all the purchase of the company
    def purchaseList(self):
        purch = open("products&prices.txt", 'a')
        purch.write(str(self.PriceWithDiscount()))
