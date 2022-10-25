from tkinter import *
import main_car_wash


class LoginPage:
    """class to represent Login Page"""

    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to CleanCar.com")
        self.root.geometry("500x300")
        self.photo = PhotoImage(file="background.PNG")
        self.label_photo = Label(root, image=self.photo)
        self.label_photo.grid()

        self.label = Label(self.root, font="helvatica 10 bold", text="Welcome to CleanCar.com", bg="#4B4E6D", width=62,
                           height=3, anchor=CENTER)
        self.label.place(x=0, y=0)

        self.label_username = Label(self.root, text="Username: ", bg="#9AC1B5", fg="darkgreen")
        self.label_username.place(x=160, y=150)
        self.label_password = Label(self.root, text="Password: ", bg="#9AC1B5", fg="darkgreen")
        self.label_password.place(x=161, y=190)
        self.entry_username = Entry(self.root, bg="#5A5353")
        self.entry_password = Entry(self.root, bg="#5A5353")
        self.entry_username.place(x=225, y=151)
        self.entry_password.place(x=224, y=191)

        self.LoginButton = Button(self.root, text="Log in", command=lambda: self.printMessage())
        self.LoginButton.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.SignupButton = Button(self.root, text="Sign up", command=lambda: self.signupMessage())
        self.SignupButton.place(x=45, relx=0.5, rely=0.8, anchor=CENTER)

    def printMessage(self):
        save = main_car_wash.User().LogIn(self.entry_username.get(), self.entry_password.get())
        if save == True:
            print("hi")
            self.userhome()
        else:
            pass

    def signupMessage(self):
        self.signhome()

    # function to change page
    def userhome(self):
        self.minor = Toplevel(self.root)
        self.homepage = homePage(self.minor, self.root)
        self.root.withdraw()

    def signhome(self):
        self.minor = Toplevel(self.root)
        self.homepage = userSignupPage(self.minor, self.root)
        self.root.withdraw()


class userSignupPage:
    """Class to represent signup page"""

    def __init__(self, root, homepage):
        self.root = root
        self.homepage = homepage

        self.root.title("Welcome to CleanCar.com")
        self.root.geometry("500x300")
        self.photo = PhotoImage(file="background.PNG")
        self.label_photo = Label(root, image=self.photo)
        self.label_photo.grid()

        self.frame = Frame(self.root)
        self.frame.place(x=200, y=50)
        self.frame_left = Frame(root)
        self.frame.place(x=200, y=50)
        self.label_username = Label(self.frame, text="Username:")
        self.label_username.grid()
        self.entry_username = Entry(self.frame)
        self.entry_username.grid(row=0, column=1)
        self.label_password = Label(self.frame, text="Password:")
        self.label_password.grid()
        self.entry_password = Entry(self.frame)
        self.entry_password.grid(row=1, column=1)
        self.label_fName = Label(self.frame, text="Full Name:")
        self.label_fName.grid()
        self.entry_fName = Entry(self.frame)
        self.entry_fName.grid(row=2, column=1)
        # self.label_lName = Label(self.frame, text="Last Name:")
        # self.label_lName.grid()
        # self.entry_lName= Entry(self.frame)
        # self.entry_lName.grid(row=3, column=1)
        self.label_address = Label(self.frame, text="Address:")
        self.label_address.grid()
        self.entry_address = Entry(self.frame)
        self.entry_address.grid(row=3, column=1)
        self.label_tel = Label(self.frame, text="Telphone:")
        self.label_tel.grid()
        self.entry_tel = Entry(self.frame)
        self.entry_tel.grid(row=4, column=1)
        self.label_email = Label(self.frame, text="Email:")
        self.label_email.grid()
        self.entry_email = Entry(self.frame)
        self.entry_email.grid(row=5, column=1)
        # self.label_washCard = Label(self.frame,text="hello")
        # self.label_washCard.grid(row=6,column=1)

        # Choosing type
        self.service = StringVar()
        self.service.set(None)
        self.regularMember = Radiobutton(self.frame, text="Regular Member", variable=self.service,
                                         value="Regular Member")
        self.regularMember.grid(row=0, column=3, sticky=W)
        self.GoldMember = Radiobutton(self.frame, text="Gold Member", variable=self.service, value="Gold Member")
        self.GoldMember.grid(row=1, column=3, sticky=W)
        self.SilverMember = Radiobutton(self.frame, text="Silver Member", variable=self.service,
                                        value="Silver Member")
        self.SilverMember.grid(row=2, column=3, sticky=W)
        self.RegularEmployee = Radiobutton(self.frame, text="Regular Employee", variable=self.service,
                                           value="Regular Employee")
        self.RegularEmployee.grid(row=3, column=3, sticky=W)
        self.Manager = Radiobutton(self.frame, text="Manager", variable=self.service, value="Manager")
        self.Manager.grid(row=4, column=3)

        entry_EEL = Entry()
        entry_EEL.grid(row=20, column=1)

        self.value1 = self.entry_fName
        self.value2 = self.entry_username
        self.value3 = self.entry_password
        self.value4 = self.entry_address
        self.value5 = self.entry_email
        self.value6 = self.entry_tel
        self.value7 = self.service

        self.SignupBtn = Button(self.frame, text="Sign up",
                                command=lambda: self.reister(self.value1, self.value2, self.value3, self.value4,
                                                             self.value5, self.value6, self.value7))
        self.SignupBtn.grid(row=15, column=1, sticky=W)
        self.BackBtn = Button(self.frame, text="Back", command=lambda: [self.homepage.deiconify(), self.root.destroy()])
        self.BackBtn.grid(row=15, column=1)

    def reister(self, a, s, d, f, g, h, j):
        main_car_wash.User().Registration(a.get(), s.get(), d.get(), f.get(), g.get(), h.get(), j.get())


class userDetailsPage:
    """Class to represent signup page"""

    def __init__(self, root, homepage):
        self.root = root
        self.homepage = homepage

        self.root.title("Welcome to CleanCar.com")
        self.root.geometry("500x300")
        self.photo = PhotoImage(file="background.PNG")
        self.label_photo = Label(self.root, image=self.photo)
        self.label_photo.grid()

        self.frame = Frame(self.root)
        self.frame.place(x=200, y=50)
        self.label_username = Label(self.frame, text="Username:")
        self.label_username.grid(row=1, column=0)
        self.label_oldusername = Label(self.frame, text=self.logInDetails(1))
        self.label_oldusername.grid(row=1, column=1)
        self.entry_username = Entry(self.frame)
        self.entry_username.grid(row=1, column=2)
        self.label_password = Label(self.frame, text="Password:")
        self.label_password.grid(row=2, column=0)
        self.label_oldpassword = Label(self.frame, text=self.logInDetails(2))
        self.label_oldpassword.grid(row=2, column=1)
        self.entry_password = Entry(self.frame)
        self.entry_password.grid(row=2, column=2)
        self.label_fName = Label(self.frame, text="Full Name:")
        self.label_fName.grid(row=3, column=0)
        self.label_oldfName = Label(self.frame, text=self.detailsGet(1))
        self.label_oldfName.grid(row=3, column=1)
        self.entry_fName = Entry(self.frame)
        self.entry_fName.grid(row=3, column=2)
        self.label_address = Label(self.frame, text="Address:")
        self.label_address.grid(row=5, column=0)
        self.label_oldaddress = Label(self.frame, text=self.detailsGet(3))
        self.label_oldaddress.grid(row=5, column=1)
        self.entry_address = Entry(self.frame)
        self.entry_address.grid(row=5, column=2)
        self.label_tel = Label(self.frame, text="Telphone:")
        self.label_tel.grid(row=6, column=0)
        self.label_oldtel = Label(self.frame, text=self.detailsGet(5))
        self.label_oldtel.grid(row=6, column=1)
        self.entry_tel = Entry(self.frame)
        self.entry_tel.grid(row=6, column=2)
        self.label_email = Label(self.frame, text="Email:")
        self.label_email.grid(row=7, column=0)
        self.label_oldemail = Label(self.frame, text=self.detailsGet(4) )
        self.label_oldemail.grid(row=7, column=1)
        self.entry_email = Entry(self.frame)
        self.entry_email.grid(row=7, column=2)

        self.label_oldwashCard = Label(self.frame, text="Card Number: " + self.detailsGet(6))
        self.label_oldwashCard.grid(row=8, column=1)

        # self.oldBtn = Button(self.frame, text="Show old Data", command=lambda: self.store())
        # self.oldBtn.grid(row=9, column=0)

        self.UpdateBtn = Button(self.frame, text="Update",
                                command=lambda: self.modify(self.entry_fName, self.entry_username, self.entry_password,
                                                            self.entry_address, self.entry_email, self.entry_tel))
        self.UpdateBtn.grid(row=9, column=1, sticky=W)
        self.BackBtn = Button(self.frame, text="Back", command=lambda: [self.homepage.deiconify(), self.root.destroy()])
        self.BackBtn.grid(row=9, column=2)

    def modify(self, a, s, d, f, g, h):
        main_car_wash.User().modifyUserInfo(a.get(), s.get(), d.get(), f.get(), g.get(), h.get())

    def detailsGet(self, index):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())
        # edit records file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        return Split[index]

    def logInDetails(self, index):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())
        # edit records file
        file = open("webUser.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        return Split[index]


    def store(self):
        pass

    def hello(self):
        return "hi"



class homePage:
    """Class to represent home page"""

    def __init__(self, root, homepage):
        self.root = root
        self.homepage = homepage

        self.root.title("Welcome to CleanCar.com")
        self.root.geometry("500x300")
        # self.root.configure(background="#9E9CAB")
        # self.photo = PhotoImage(file="background.PNG")
        # self.label_photo = Label

        # self.background = Canvas(self.root, bg="blue", height=250, width=300)
        # filename = PhotoImage(file="background.PNG")
        # background_label = Label(self.root, image=filename)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # self.background.grid(row=0)

        self.frame_left = Frame(self.root)
        self.frame_right = Frame(self.root)

        self.frame_left.grid(row=0, column=0, sticky="NSEW")
        self.frame_right.grid(row=0, column=1, sticky="NSEW")

        def checkService():
            print("You have chosen" + self.service.get())

        self.service = StringVar()
        self.service.set("Regular Wash")
        self.regularWash = Radiobutton(self.frame_left, text="Regular wash", variable=self.service,
                                       value="Regular Wash", command=checkService)
        self.regularWash.grid(row=4, column=0, sticky=W)
        self.regularWash = Label(self.frame_left, text="40dhs")
        self.regularWash.grid(row=4, column=1)
        self.DeepWash = Radiobutton(self.frame_left, text="Deep Wash", variable=self.service, value="Deep Wash",
                                    command=checkService)
        self.DeepWash.grid(row=5, column=0, sticky=W)
        self.DeepWash = Label(self.frame_left, text="80dhs")
        self.DeepWash.grid(row=5, column=1)
        self.SteamClean = Radiobutton(self.frame_left, text="Steam Cleaning", variable=self.service,
                                      value="Steam Cleaning", command=checkService)
        self.SteamClean.grid(row=6, column=0, sticky=W)
        self.SteamClean = Label(self.frame_left, text="200dhs")
        self.SteamClean.grid(row=6, column=1)
        self.EngineOil = Radiobutton(self.frame_left, text="Engine Oiling", variable=self.service,
                                     value="Engine Oiling", command=checkService)
        self.EngineOil.grid(row=7, column=0, sticky=W)
        self.EngineOil = Label(self.frame_left, text="20dhs")
        self.EngineOil.grid(row=7, column=1)
        self.TyreCheck = Radiobutton(self.frame_left, text="Tyre CheckUp", variable=self.service, value="Tyre CheckUp",
                                     command=checkService)
        self.TyreCheck.grid(row=8, column=0)
        self.TyreCheck = Label(self.frame_left, text="40dhs")
        self.TyreCheck.grid(row=8, column=1)
        self.label_washCard = Label(self.frame_left, text="Your Wash Card ID:%s" % self.IDwashCard())
        self.label_washCard.grid(row=10, column=0)
        self.label_AvailableAmt = Label(self.frame_left, text="Your Available Amount:%s" % self.availableAmount())
        self.label_AvailableAmt.grid(row=10, column=3)


        # Other Functions
        self.userDetails = Button(self.frame_right, text="User Details", command=lambda: self.print1Message(3))
        self.userDetails.grid(row=0, column=1, sticky=W)
        self.addMoney = Button(self.frame_right, text="Top up", command=lambda: self.print1Message(2))
        self.addMoney.grid(row=1, column=1, sticky=W)
        self.staffonly = Button(self.frame_right, text="StaffOnly", command=lambda: self.print1Message(4))
        self.staffonly.grid(row=2, column=1, sticky=W)
        # self.logout = Button(self.frame_right,text="logout", command=lambda : [self.homepage.deiconify(),self.root.destroy()])
        # self.logout.grid(row=3,column=1,sticky=W)

        # Submit button
        self.BuyBtn = Button(self.frame_left, text="Pay", command=lambda: self.money(self.service))
        self.BuyBtn.grid(sticky=E)

    def money(self, x):
        main_car_wash.Transaction().Payment(x.get())

    # Function to change page

    def print1Message(self, x):
        if x == 2:
            print("hi")
            self.gototopUpPage()
        elif x == 3:
            print("details")
            self.gotouserDetailsPage()
        elif x == 4:
            if main_car_wash.User().stuffOnly() == True:
                print("signup", main_car_wash.User().stuffOnly())
                self.gotostaffonly()
        else:
            print("no value")

    # function to change page
    def gototopUpPage(self):
        self.master = Toplevel(self.root)
        self.homepage = topUpPage(self.master, self.root)
        self.root.withdraw()

    def gotouserDetailsPage(self):
        self.minor = Toplevel(self.root)
        self.homepage = userDetailsPage(self.minor, self.root)
        self.root.withdraw()

    def gotostaffonly(self):
        self.minor = Toplevel(self.root)
        self.homepage = staffOnly(self.minor, self.root)
        self.root.withdraw()

    def IDwashCard(self):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())
        # edit records file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        return Split[6]

    def availableAmount(self):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())
        # edit records file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        return str(Split[7]) + "AED"




class staffOnly:
    """Class to represent home page"""

    def __init__(self, root, homepage):
        self.root = root
        self.homepage = homepage

        self.root.title("Welcome to CleanCar.com")
        self.root.geometry("500x300")
        # self.root.configure(background="#9E9CAB")
        # self.photo = PhotoImage(file="background.PNG")
        # self.label_photo = Label

        # self.background = Canvas(self.root, bg="blue", height=250, width=300)
        # filename = PhotoImage(file="background.PNG")
        # background_label = Label(self.root, image=filename)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # self.background.grid(row=0)

        self.frame_left = Frame(self.root)
        self.frame_right = Frame(self.root)

        self.frame_left.grid(row=0, column=0, sticky="NSEW")
        self.frame_right.grid(row=0, column=1, sticky="NSEW")

        self.textBox = Text(self.frame_left, width=25, height=10)
        self.textBox.configure(state="disabled")
        self.textBox.grid()

        # Other Functions
        self.showAll = Button(self.frame_right, text="Show All", command=lambda: self.show())
        self.showAll.grid(row=0, column=1, sticky=W)
        self.delAll = Button(self.frame_right, text="Delete All", command=lambda: self.delete())
        self.delAll.grid(row=2, column=1, sticky=W)
        self.purchase = Button(self.frame_right, text="Purchase List", command=lambda: self.purc())
        self.purchase.grid(row=3, column=1, sticky=W)
        self.BackBtn = Button(self.frame_right, text="Back",
                              command=lambda: [self.homepage.deiconify(), self.root.destroy()])
        self.BackBtn.grid(row=9, column=1)

        # def see(self, x):
        #     return x

    def delete(self):
        main_car_wash.Manager().DeleteAll()
        self.textBox.configure(state="normal")
        self.textBox.delete(0.0, END)
        self.textBox.configure(state="disabled")


    def purc(self):
        y = main_car_wash.Transaction().showpurchaseList()
        self.textBox.configure(state="normal")
        self.textBox.delete(0.0, END)
        self.textBox.insert(END, y)
        self.textBox.configure(state="disabled")

    def show(self):
        x = main_car_wash.Employee().DisplayInfoPrivilage()
        self.textBox.configure(state="normal")
        self.textBox.delete(0.0, END)
        self.textBox.insert(END, x)
        self.textBox.configure(state="disabled")



class topUpPage:
    """Class to represent signup page"""

    def __init__(self, root, homepage):
        self.root = root
        self.homepage = homepage

        self.root.title("Welcome to CleanCar.com")
        self.root.geometry("500x300")
        self.photo = PhotoImage(file="background.PNG")
        self.label_photo = Label(root, image=self.photo)
        self.label_photo.grid()

        self.frame = Frame(root)
        self.frame.place(x=200, y=50)
        self.label_cardNum = Label(self.frame, text="Card Number:")
        self.label_cardNum.grid()
        self.entry_cardNum = Entry(self.frame)
        self.entry_cardNum.grid(row=0, column=1)
        self.label_name = Label(self.frame, text="Name on Card:")
        self.label_name.grid()
        self.entry_name = Entry(self.frame)
        self.entry_name.grid(row=1, column=1)
        self.label_cvv = Label(self.frame, text="Cvv:")
        self.label_cvv.grid()
        self.entry_cvv = Entry(self.frame)
        self.entry_cvv.grid(row=2, column=1)
        self.label_Amount = Label(self.frame, text="Amount:")
        self.label_Amount.grid()
        self.entry_Amount = Entry(self.frame)
        self.entry_Amount.grid(row=3, column=1)

        self.label_washCard = Label(self.frame, text="Your Wash Card ID is: " + self.IDwashCard())
        self.label_washCard.grid(row=7, column=1)

        self.topUpBtn = Button(self.frame, text="top Up", command=lambda: self.top(self.entry_Amount))
        self.topUpBtn.grid(row=8, column=1, sticky=W)
        self.BackBtn = Button(self.frame, text="Back", command=lambda: [self.homepage.deiconify(), self.root.destroy()])
        self.BackBtn.grid(row=8, column=1)

    def top(self, x):
        main_car_wash.Transaction().TopUp(float(x.get()))

    def IDwashCard(self):
        file_session = open("session.txt", "r")
        updateID = int(file_session.read())
        # edit records file
        file = open("records.txt", "r")
        lines = file.readlines()
        Split = lines[updateID].split(",")
        return Split[6]



root = Tk()
b = LoginPage(root)
root.mainloop()
