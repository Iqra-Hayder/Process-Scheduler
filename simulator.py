from tkinter import *
import tkinter.font as tkFont
import turtle as t
from scheduler_logic import (
    animate_FCFS, animate_SJFN, animate_SJF, animate_RR
)

mode = "None"
n = 5

def Simulate_Click():
    global proc1, proc2, proc3, proc4, proc5, at1, at2, at3, at4, at5, bt1, bt2, bt3, bt4, bt5, quantum, mode
    try:
        t.reset()
        proc1 = int(proc1En.get())
        proc2 = int(proc2En.get())
        proc3 = int(proc3En.get())
        if(n>=4):
            proc4 = int(proc4En.get())
            at4 = int(proc4Arriv.get())
            bt4 = int(proc4Burs.get())
            if(n==5):
                proc5 = int(proc5En.get())
                at5 = int(proc5Arriv.get())
                bt5 = int(proc5Burs.get())
        at1 = int(proc1Arriv.get())
        at2 = int(proc2Arriv.get())
        at3 = int(proc3Arriv.get())
        bt1 = int(proc1Burs.get())
        bt2 = int(proc2Burs.get())
        bt3 = int(proc3Burs.get())
        
        if(mode == "RR"):
            quantum = int(QuanEn.get())

        # Prepare process lists based on number of processes
        if(n<=3):
            procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
            temp2 = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3]]
        elif(n==4):
            procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
            temp2 = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4]]
        else:
            procList = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]
            temp2 = [[proc1,at1,bt1],[proc2,at2,bt2],[proc3,at3,bt3],[proc4,at4,bt4],[proc5,at5,bt5]]

        # Call appropriate scheduling algorithm
        if(mode == "FCFS"):
            animate_FCFS(procList, temp2, n)
        elif(mode == "SJFN"):
            temp = procList.copy()
            tempt = temp2.copy()
            animate_SJFN(procList, temp, tempt, n)
        elif(mode == "SJF"):
            temp = procList.copy()
            tempt = temp2.copy()
            animate_SJF(procList, temp, tempt, n)
        elif(mode == "RR"):
            temp = procList.copy()
            tempt = temp2.copy()
            animate_RR(procList, temp, tempt, n, quantum)
    except Exception as e:
        print(f"Error: {e}")
        pass

def FCFS_Click():
    global mode, TimeQuan, QuanEn
    mode = "FCFS"
    try:
        TimeQuan.destroy()
        QuanEn.destroy()
    except:
        pass

def SJFN_Click():
    global mode, TimeQuan, QuanEn
    mode = "SJFN"
    try:
        TimeQuan.destroy()
        QuanEn.destroy()
    except:
        pass

def SJF_Click():
    global mode, TimeQuan, QuanEn
    mode = "SJF"
    try:
        TimeQuan.destroy()
        QuanEn.destroy()
    except:
        pass

def RR_Click():
    global mode, QuanEn, TimeQuan
    mode = "RR"
    TimeQuan = Label(root)
    ft = tkFont.Font(family='Times', size=10)
    TimeQuan["font"] = ft
    TimeQuan["fg"] = "#333333"
    TimeQuan["justify"] = "center"
    TimeQuan["text"] = "Time quantum"
    TimeQuan.place(x=100, y=190, width=95, height=25)

    QuanEn = Entry(root)
    QuanEn["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    QuanEn["font"] = ft
    QuanEn["fg"] = "#333333"
    QuanEn["justify"] = "center"
    QuanEn.place(x=110, y=210, width=70, height=25)
    QuanEn.insert(END, "5")

def Add_Proc():
    global n
    if(n<=3):
        n = 3
    if(n>=5):
        n = 5
    n += 1
    root.after(10, addProc)

def Sub_Proc():
    global n
    if(n<=3):
        n = 3
    if(n>=5):
        n = 5
    n -= 1
    root.after(10, subProc)

def addProc():
    global proc4En, proc4Arriv, proc4Burs, proc5En, proc5Arriv, proc5Burs
    if(n == 4):
        proc4En = Entry(root)
        proc4En["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        proc4En["font"] = ft
        proc4En["fg"] = "#333333"
        proc4En["justify"] = "center"
        proc4En.place(x=320, y=220, width=70, height=25)
        proc4En.insert(END, "4")

        proc4Arriv = Entry(root)
        proc4Arriv["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        proc4Arriv["font"] = ft
        proc4Arriv["fg"] = "#333333"
        proc4Arriv["justify"] = "center"
        proc4Arriv.place(x=400, y=220, width=70, height=25)

        proc4Burs = Entry(root)
        proc4Burs["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        proc4Burs["font"] = ft
        proc4Burs["fg"] = "#333333"
        proc4Burs["justify"] = "center"
        proc4Burs.place(x=480, y=220, width=70, height=25)
    if(n == 5):
        proc5En = Entry(root)
        proc5En["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        proc5En["font"] = ft
        proc5En["fg"] = "#333333"
        proc5En["justify"] = "center"
        proc5En.place(x=320, y=260, width=70, height=25)
        proc5En.insert(END, "5")

        proc5Arriv = Entry(root)
        proc5Arriv["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        proc5Arriv["font"] = ft
        proc5Arriv["fg"] = "#333333"
        proc5Arriv["justify"] = "center"
        proc5Arriv.place(x=400, y=260, width=70, height=25)

        proc5Burs = Entry(root)
        proc5Burs["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        proc5Burs["font"] = ft
        proc5Burs["fg"] = "#333333"
        proc5Burs["justify"] = "center"
        proc5Burs.place(x=480, y=260, width=70, height=25)

def subProc():
    if(n==3):
        proc4En.destroy()
        proc4Arriv.destroy()
        proc4Burs.destroy()
    if(n==4):
        proc5En.destroy()
        proc5Arriv.destroy()
        proc5Burs.destroy()

# Create main window
root = Tk()
root.geometry('600x500')
root.title("Process Scheduling Simulator")
width = 600
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# Header Label
LabelHead = Label(root)
ft = tkFont.Font(family='Times', size=15)
LabelHead["font"] = ft
LabelHead["fg"] = "#333333"
LabelHead["justify"] = "center"
LabelHead["text"] = "Process Scheduling Simulator"
LabelHead.place(x=190, y=20, width=250, height=39)

# Simulate Button
SimulateBtn = Button(root)
SimulateBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
SimulateBtn["font"] = ft
SimulateBtn["fg"] = "#000000"
SimulateBtn["justify"] = "center"
SimulateBtn["text"] = "Simulate"
SimulateBtn.place(x=250, y=350, width=70, height=25)
SimulateBtn["command"] = Simulate_Click

# Add/Remove Process Buttons
AddBtn = Button(root)
AddBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
AddBtn["font"] = ft
AddBtn["fg"] = "#000000"
AddBtn["justify"] = "center"
AddBtn["text"] = "+"
AddBtn.place(x=280, y=180, width=30, height=30)
AddBtn["command"] = Add_Proc

SubBtn = Button(root)
SubBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
SubBtn["font"] = ft
SubBtn["fg"] = "#000000"
SubBtn["justify"] = "center"
SubBtn["text"] = "-"
SubBtn.place(x=280, y=140, width=30, height=30)
SubBtn["command"] = Sub_Proc

# Algorithm Radio Buttons
FCFSRadio = Radiobutton(root, value=1)
ft = tkFont.Font(family='Times', size=10)
FCFSRadio["font"] = ft
FCFSRadio["fg"] = "#333333"
FCFSRadio["justify"] = "center"
FCFSRadio["text"] = "FCFS"
FCFSRadio.place(x=50, y=70, width=85, height=25)
FCFSRadio["command"] = FCFS_Click

SJFNRadio = Radiobutton(root, value=2)
ft = tkFont.Font(family='Times', size=10)
SJFNRadio["font"] = ft
SJFNRadio["fg"] = "#333333"
SJFNRadio["justify"] = "center"
SJFNRadio["text"] = "SJF (Non-preemptive)"
SJFNRadio.place(x=35, y=100, width=200, height=32)
SJFNRadio["command"] = SJFN_Click

SJFRadio = Radiobutton(root, value=3)
ft = tkFont.Font(family='Times', size=10)
SJFRadio["font"] = ft
SJFRadio["fg"] = "#333333"
SJFRadio["justify"] = "center"
SJFRadio["text"] = "SJF (Preemptive)"
SJFRadio.place(x=32, y=130, width=180, height=30)
SJFRadio["command"] = SJF_Click

RRRadio = Radiobutton(root, value=4)
ft = tkFont.Font(family='Times', size=10)
RRRadio["font"] = ft
RRRadio["fg"] = "#333333"
RRRadio["justify"] = "center"
RRRadio["text"] = "Round Robin"
RRRadio.place(x=25, y=160, width=180, height=30)
RRRadio["command"] = RR_Click

# Column Headers
ProcNum = Label(root)
ft = tkFont.Font(family='Times', size=10)
ProcNum["font"] = ft
ProcNum["fg"] = "#333333"
ProcNum["justify"] = "center"
ProcNum["text"] = "Process#"
ProcNum.place(x=300, y=70, width=95, height=25)

ArriveTime = Label(root)
ft = tkFont.Font(family='Times', size=10)
ArriveTime["font"] = ft
ArriveTime["fg"] = "#333333"
ArriveTime["justify"] = "center"
ArriveTime["text"] = "ArriveTime"
ArriveTime.place(x=390, y=70, width=100, height=25)

BurstTime = Label(root)
ft = tkFont.Font(family='Times', size=10)
BurstTime["font"] = ft
BurstTime["fg"] = "#333333"
BurstTime["justify"] = "center"
BurstTime["text"] = "BurstTime"
BurstTime.place(x=480, y=70, width=100, height=25)

# Process 1 Entries
proc1En = Entry(root)
proc1En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc1En["font"] = ft
proc1En["fg"] = "#333333"
proc1En["justify"] = "center"
proc1En.place(x=320, y=100, width=70, height=25)
proc1En.insert(END, "1")

proc1Arriv = Entry(root)
proc1Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc1Arriv["font"] = ft
proc1Arriv["fg"] = "#333333"
proc1Arriv["justify"] = "center"
proc1Arriv.place(x=400, y=100, width=70, height=25)

proc1Burs = Entry(root)
proc1Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc1Burs["font"] = ft
proc1Burs["fg"] = "#333333"
proc1Burs["justify"] = "center"
proc1Burs.place(x=480, y=100, width=70, height=25)

# Process 2 Entries
proc2En = Entry(root)
proc2En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc2En["font"] = ft
proc2En["fg"] = "#333333"
proc2En["justify"] = "center"
proc2En.place(x=320, y=140, width=70, height=25)
proc2En.insert(END, "2")

proc2Arriv = Entry(root)
proc2Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc2Arriv["font"] = ft
proc2Arriv["fg"] = "#333333"
proc2Arriv["justify"] = "center"
proc2Arriv.place(x=400, y=140, width=70, height=25)

proc2Burs = Entry(root)
proc2Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc2Burs["font"] = ft
proc2Burs["fg"] = "#333333"
proc2Burs["justify"] = "center"
proc2Burs.place(x=480, y=140, width=70, height=25)

# Process 3 Entries
proc3En = Entry(root)
proc3En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc3En["font"] = ft
proc3En["fg"] = "#333333"
proc3En["justify"] = "center"
proc3En.place(x=320, y=180, width=70, height=25)
proc3En.insert(END, "3")

proc3Arriv = Entry(root)
proc3Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc3Arriv["font"] = ft
proc3Arriv["fg"] = "#333333"
proc3Arriv["justify"] = "center"
proc3Arriv.place(x=400, y=180, width=70, height=25)

proc3Burs = Entry(root)
proc3Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc3Burs["font"] = ft
proc3Burs["fg"] = "#333333"
proc3Burs["justify"] = "center"
proc3Burs.place(x=480, y=180, width=70, height=25)

# Process 4 Entries
proc4En = Entry(root)
proc4En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc4En["font"] = ft
proc4En["fg"] = "#333333"
proc4En["justify"] = "center"
proc4En.place(x=320, y=220, width=70, height=25)
proc4En.insert(END, "4")

proc4Arriv = Entry(root)
proc4Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc4Arriv["font"] = ft
proc4Arriv["fg"] = "#333333"
proc4Arriv["justify"] = "center"
proc4Arriv.place(x=400, y=220, width=70, height=25)

proc4Burs = Entry(root)
proc4Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc4Burs["font"] = ft
proc4Burs["fg"] = "#333333"
proc4Burs["justify"] = "center"
proc4Burs.place(x=480, y=220, width=70, height=25)

# Process 5 Entries
proc5En = Entry(root)
proc5En["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc5En["font"] = ft
proc5En["fg"] = "#333333"
proc5En["justify"] = "center"
proc5En.place(x=320, y=260, width=70, height=25)
proc5En.insert(END, "5")

proc5Arriv = Entry(root)
proc5Arriv["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc5Arriv["font"] = ft
proc5Arriv["fg"] = "#333333"
proc5Arriv["justify"] = "center"
proc5Arriv.place(x=400, y=260, width=70, height=25)

proc5Burs = Entry(root)
proc5Burs["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
proc5Burs["font"] = ft
proc5Burs["fg"] = "#333333"
proc5Burs["justify"] = "center"
proc5Burs.place(x=480, y=260, width=70, height=25)

root.mainloop()
