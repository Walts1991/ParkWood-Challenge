from tkinter import *

    
PayrollWin=Tk()
PayrollWin.title("Payroll")
PayrollWin.geometry("300x500")

GrossPay=IntVar()
Tax=DoubleVar()
Tax.set('0.0')
NatIns=DoubleVar()
NatIns.set('0.0')
Pension=DoubleVar()
Pension.set('0.0')
StudentLoan=DoubleVar()
StudentLoan.set('0.0')
Deducts=DoubleVar()
Deducts.set('0.0')
NetPay=DoubleVar()
NetPay.set('0.0')

def CalcPay():

    Gross = float(GrossPay.get())
    #Tax rate increase from 0.2 to 0.22 and National Insurance (NI) decrease from 0.14 to 0.085
    Tax.set(Gross * 0.22)
    NatIns.set(Gross * 0.085)
    Pension.set(Gross * 0.08)
    StudentLoan.set(Gross * 0.1)
    #Chanses to Deducts and NatPay in relation to above tax increase and NI decrease
    Deducts.set(Gross * 0.22 + Gross * 0.085 + Gross * 0.08 + Gross * 0.1)
    NetPay.set(Gross - (Gross * 0.22 + Gross * 0.085 + Gross * 0.08 + Gross * 0.1)
        
   
GrossPayLabel=Label(PayrollWin, text="Gross Pay").grid(row=3, column=0, sticky=W)
GrossPayEntry= Entry(PayrollWin, textvariable=GrossPay)
GrossPayEntry.grid(row=3,column=1)


b1= Button(PayrollWin, text=" Calculate ", command=CalcPay).grid(row=4)
 

TaxLabelText=Label(PayrollWin, text="Tax: ").grid(row=5, column=0, sticky=W)
TaxLabelValue=Label(PayrollWin, textvariable=Tax).grid(row=5, column=1, sticky=W)
NatInsLabelText =Label(PayrollWin, text="National Insurance: ").grid(row=6, column=0, sticky=W)
NatInsLabelValue=Label(PayrollWin, textvariable=NatIns).grid(row=6, column=1, sticky=W)
PensionLabeltext=Label(PayrollWin, text="Pension Contribution: " ).grid(row=7, column=0, sticky=W)
PensionLabelValue=Label(PayrollWin, textvariable=Pension).grid(row=7, column=1, sticky=W)
StudentLoanLabeltext=Label(PayrollWin, text="Student Loan: " ).grid(row=8, column=0, sticky=W)
StudentLoanLabelValue=Label(PayrollWin, textvariable=StudentLoan).grid(row=8, column=1, sticky=W)
DeductsLabelText=Label(PayrollWin, text="Deductions: " ).grid(row=9, column=0, sticky=W)
DeductsLabelValue=Label(PayrollWin, textvariable=Deducts).grid(row=9, column=1, sticky=W)
NetPayLabelText=Label(PayrollWin, text="Net Pay: ").grid(row=10, column=0, sticky=W)
NetPayLabelValue=Label(PayrollWin, textvariable=NetPay).grid(row=10, column=1, sticky=W)


b2= Button(PayrollWin, text=" Back ", command=PayrollWin.destroy).grid(row=10)
   
    
PayrollWin.mainloop()
