#Need to complete questions 5 and 7 of Pupil Information / Testing / Refinement of nested if statements

#ParkWood School - AddTeachers function used as base template
from tkinter import *
from tkinter import messagebox
import os
#Replaced Teacher with Pupil
def SavePupil() :

    PupilIDSave = PupilIDVar.get()
    #Added check if pupil exists
    if PupilIDSave.strip() == "" :
        messagebox.showinfo("Error","Pupil ID does not exist")
    PupilIDSave = PupilIDSave.ljust(50)
    
    FirstnameSave = FirstnameVar.get()
    #Added check to ensure that pupil's first name does not contain a number
    if FirstnameSave.strip() == [1,2,3,4,5,6,7,8,9]:
        messagebox.showinfo("Error","Pupil first name should not contain any numbers")
    FirstnameSave = FirstnameSave.ljust(50)

    SurnameSave = SurnameVar.get()
    SurnameSave = SurnameSave.ljust(50)
    #Added Form Class
    FormClassSave = FormClassVar.get()
    FormClassSave = FormClassSave.ljust(50)
    #Added Date of Birth
    DateOfBirthSave = DateOfBirthVar.get()
    DateOfBirthSave = DateOfBirthSave.ljust(50)

    fileObject = open("PupilDetails.txt","a")
    
    fileObject.write(PupilIDSave + FirstnameSave + SurnameSave + FormClassSave + DateOfBirthSave + "\n")
    fileObject.close()
    
    messagebox.showinfo("Confirmation","Pupil details successfully saved")

AddPupilWin=Tk()
AddPupilWin.title("Add Pupil")
AddPupilWin.geometry("300x300")

frame1=Frame(AddPupilWin)
frame1.pack()
   
Label(frame1, text="Pupil ID").grid(row=3, column=0, sticky=W)
PupilIDVar=StringVar()
PupilIDVar= Entry(frame1, textvariable=PupilIDVar)
PupilIDVar.grid(row=3,column=1,sticky=W)

Label(frame1, text="Firstname").grid(row=4, column=0, sticky=W)
FirstnameVar=StringVar()
FirstnameVar= Entry(frame1, textvariable=FirstnameVar)
FirstnameVar.grid(row=4,column=1,sticky=W)

Label(frame1, text="Surname").grid(row=5, column=0, sticky=W)
SurnameVar=StringVar()
SurnameVar= Entry(frame1, textvariable=SurnameVar)
SurnameVar.grid(row=5,column=1,sticky=W)
#Added Form Class
Label(frame1, text="Form Class").grid(row=6, column=0, sticky=W)
FormClassVar=StringVar()
FormClassVar= Entry(frame1, textvariable=FormClassVar)
FormClassVar.grid(row=6,column=1,sticky=W)
#Added Date of Birth
Label(frame1, text="Date of Birth").grid(row=7, column=0, sticky=W)
DateOfBirthVar=StringVar()
DateOfBirthVar= Entry(frame1, textvariable=DateOfBirthVar)
DateOfBirthVar.grid(row=7,column=1,sticky=W)

frame2 = Frame(AddPupilWin)
frame2.pack()
b1= Button(frame2, text=" Back ", command=AddPupilWin.destroy)
b2= Button(frame2, text=" Save ", command=SavePupil)
b1.pack(side=LEFT); b2.pack(side=LEFT)

#Added main loop
AddPupilWin.mainloop()