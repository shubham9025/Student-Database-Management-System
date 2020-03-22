#Frontend
from tkinter import*
import tkinter.messagebox
import stdDatabase_BackEnd

class Student:
    
    def __init__(self, root):
     self.root = root
     self.root.title("Student Database Management System")
     self.root.geometry("1350x1000+0+0")
     self.root.config(bg = "cadet blue")
     
     StdID = StringVar()
     Firstname = StringVar()
     Secondname = StringVar()
     DOB = StringVar()
     Age = StringVar()
     Gender = StringVar()
     Address = StringVar()
     Mobile = StringVar()

     def iExit():
         iExit=tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
         if iExit >0:
            root.destroy()
            return

     def clearData():
        self.txtStdID.delete(0,END)
        self.txtfna.delete(0,END)
        self.txtsna.delete(0,END)
        self.txtDoB.delete(0,END)
        self.txtAge.delete(0,END)
        self.txtGender.delete(0,END)
        self.txtAdress.delete(0,END)
        self.txtMobile.delete(0,END)
    def AddData():
        if(len(StdID.get())!=0):
            stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(),Surname.get(),DoB.get(),Age.get(), Gender.get(),Address.get(),Mobile.get()):
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(), Address.get(),Mobile.get()))
        


    def DisplayData():
        studentlist.delete(0,END)
        for row in stdDatabase_BackEnd.viewData():
         studentlist.insert(END,row,str(""))


                     
    def StudentRec(event):
        global sd
        searchStd = studentlist.curselection()[0]
        sd = studentlist.get(searchStd)

        self.txtStdID.delete(0,END)
        self.txtStdID.insert(END,sd[0])
        self.txtfna.delete(0,END)
        self.txtfna.insert(END,sd[0])
        self.txtsna.delete(0,END)
        self.txtsna.insert(END,sd[0])
        self.txtDoB.delete(0,END)
        self.txtDoB.insert(END,sd[0])
        self.txtAge.delete(0,END)
        self.txtAge.insert(END,sd[0])
        self.txtGender.delete(0,END)
        self.txtGender.insert(END,sd[0])
        self.txtAdress.delete(0,END)
        self.txtAddress.insert(END,sd[0])
        
        self.txtMobile.delete(0,END)
        self.txtMobile.insert(END,sd[0])
    
       def DeleteData():
        if(len(StdID.get())!=0):
            stdDatabase_BackEnd.deleteRec(sd[0])

     MainFrame = Frame(self.root,bg="cadet blue")
     MainFrame.grid()

     TitFrame = Frame(MainFrame,bd=2,padx=54,pady=8,bg="ghost white",relief=RIDGE)
     TitFrame.pack(side=TOP)

     self.lblTit = Label(TitFrame,font=('arial',47,'bold'),text="Student Database Management Stsyem",bg=
                        "Ghost White")
     self.lblTit.grid()

     ButtonFrame = Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="ghost White",relief=RIDGE)
     ButtonFrame.pack(side = BOTTOM)

     DataFrame = Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE,bg="cadet blue")
     DataFrame.pack(side=BOTTOM)

     DataFrameLEFT = LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White", font=('arial',47,'bold'),text="student info\n")
     DataFrameLEFT.pack(side=LEFT)

     
     DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=3,pady=3,relief=RIDGE,bg="Ghost White",font=('arial',20,'bold'),text="Student Details\n")
     DataFrameRIGHT.pack(side=RIGHT)


     self.lblstdID = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Student ID",padx=2,pady=2,bg="Ghost White")
     self.lblstdID.grid(row=0,column=0,sticky=W)

     self.txtStdID = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="StuID",width=39)
     self.txtStdID.grid(row=0,column=1)

     self.lblfna = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Firstname:",padx=2,pady=2,bg="Ghost White")
     self.lblfna.grid(row=1,column=0,sticky=W)

     self.txtfna= Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="Firstname",width=39)
     self.txtfna.grid(row=1,column=1)

     self.lblSna = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Surname:",padx=2,pady=2,bg="Ghost White")
     self.lblSna.grid(row=2,column=0,sticky=W)

     self.txtSna= Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="Surname",width=39)
     self.txtSna.grid(row=2,column=1)

     self.lblDOB = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Date Of Birth:",padx=2,pady=2,bg="Ghost White")
     self.lblDOB.grid(row=3,column=0,sticky=W)

     self.txtDOB= Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="DoB",width=39)
     self.txtDOB.grid(row=3,column=1)

     self.lblAge = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Age:",padx=2,pady=2,bg="Ghost White")
     self.lblAge.grid(row=4,column=0,sticky=W)

     self.txtAge= Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="Age",width=39)
     self.txtAge.grid(row=4,column=1)

     self.lblGender = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Gender:",padx=2,pady=2,bg="Ghost White")
     self.lblGender.grid(row=5,column=0,sticky=W)

     self.txtGender= Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="Gender",width=39)
     self.txtGender.grid(row=5,column=1)


     self.lblAddress = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Address:",padx=2,pady=2,bg="Ghost White")
     self.lblAddress.grid(row=6,column=0,sticky=W)

     self.txtAddress= Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="Address",width=39)
     self.txtAddress.grid(row=6,column=1)

     self.lblMobile = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Mobile:",padx=2,pady=2,bg="Ghost White")
     self.lblMobile.grid(row=7,column=0,sticky=W)

     self.txtMobile= Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable="Mobile",width=39)
     self.txtMobile.grid(row=7,column=1)

     scrollbar = Scrollbar(DataFrameRIGHT)
     scrollbar.grid(row=0,column=1,sticky='ns')

     studentlist = Listbox(DataFrameRIGHT,width=41, height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
     studentlist.grid(row=0,column=0,padx=8)
     scrollbar.config(command = studentlist.yview)

     self.btnAddData = Button(ButtonFrame,text = "Add New",font=('arial',20,'bold'),height=1,width=10,bd=4 ,command=addData)
     self.btnAddData.grid(row=0,column=0)

     self.btnDisplayData = Button(ButtonFrame,text = "Display",font=('arial',20,'bold'),height=1,width=10,bd=4, command=DisplayData)
     self.btnDisplayData.grid(row=0,column=1)

     self.btnClearData = Button(ButtonFrame,text = "Clear",font=('arial',20,'bold'),height=1,width=10,bd=4)
     self.btnClearData.grid(row=0,column=2)

     self.btnDeleteData = Button(ButtonFrame,text = "Delete",font=('arial',20,'bold'),height=1,width=10,bd=4)
     self.btnDeleteData.grid(row=0,column=3)

     self.btnSearchData = Button(ButtonFrame,text = "Search",font=('arial',20,'bold'),height=1,width=10,bd=4)
     self.btnSearchData.grid(row=0,column=4)

     self.btnUpdateData = Button(ButtonFrame,text = "Update",font=('arial',20,'bold'),height=1,width=10,bd=4)
     self.btnUpdateData.grid(row=0,column=5)

     self.btnExitData = Button(ButtonFrame,text = "Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iExit)
     self.btnExitData.grid(row=0,column=6)
     
     
if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
     
