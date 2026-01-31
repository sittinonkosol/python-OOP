from tkinter import *
from tkinter import ttk

# This is a Tkinter example from the PDF, creating for completeness as requested.
# Page 6

mainFrm = Tk()
mainFrm.title("Hello GUI tkinter Python")
# mainFrm.mainloop() # In original code this was split

# Page 6 also shows a more complex example "Progam Calculator" (Calculations not shown but layout is)
# "Example 12.2"
# I will implement the code shown in the screenshot of the text block

# Reload module tkinter - from tkinter import * (Already done)
# from tkinter import ttk # (Already done)
# mainFrm = Tk() # Already done

mainFrm.title("โปรแกรมบวกเลข")

lblTitle = ttk.Label(mainFrm, text="โปรแกรมบวกเลข", font='20')
lblNum1 = ttk.Label(mainFrm, text="ป้อนตัวเลขที่ 1 :")
lblNum2 = ttk.Label(mainFrm, text="ป้อนตัวเลขที่ 2 :")
lblTotal = ttk.Label(mainFrm, text="ผลลัพธ์ :")

lblTitle.grid(column=0, columnspan=2, padx=150, pady=10)
lblNum1.grid(column=0, row=2, pady=5, sticky="NE")
lblNum2.grid(column=0, row=3, pady=5, sticky="NE")
lblTotal.grid(column=0, row=4, pady=5, sticky="NE")

entNum1 = ttk.Entry(mainFrm, width=25)
entNum2 = ttk.Entry(mainFrm, width=25)
entTotal = ttk.Entry(mainFrm, width=25)

entNum1.grid(column=1, row=2, sticky="W")
entNum2.grid(column=1, row=3, sticky="W")
entTotal.grid(column=1, row=4, sticky="W")

btnClick = ttk.Button(mainFrm, text="Click", width=10)
btnClear = ttk.Button(mainFrm, text="Clear", width=10)

btnClick.grid(column=0, row=5, pady=10, sticky="NE")
btnClear.grid(column=1, row=5, padx=10, sticky="W")

mainFrm.mainloop()
