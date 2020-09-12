from tkinter import *

root = Tk()
root.geometry("600x600")
root.title(" DB converter ")

def func(s):  

    dic={
    "$$SLSORDVWDB":["SLSORDVWDB_TS1","SLSORDVWDB_TS2","SLSORDVWDB_TS3","SLSORDVWDB_TS4","SLSORDVWDB_DV1","SLSORDVWDB_DV2","SLSORDVWDB_DV3","SLSORDVWDB_DV4","slsordvwdb_TS1","slsordvwdb_TS2","slsordvwdb_TS3","slsordvwdb_TS4","slsordvwdb_DV1","slsordvwdb_DV2","slsordvwdb_DV3","slsordvwdb_DV4"],
    "$$STGDB":["STGDB_TS1","STGDB_TS2","STGDB_TS3","STGDB_TS4","STGDB_DV1","STGDB_DV2","STGDB_DV3","STGDB_DV4"],
    "$$COMREFVWDB":["COMREFVWDB_TS1","COMREFVWDB_TS2","COMREFVWDB_TS3","COMREFVWDB_TS4","COMREFVWDB_DV1","COMREFVWDB_DV2","COMREFVWDB_DV3","COMREFVWDB_DV4"],
    "$$ETLVWDB":["ETLVWDB_TS1","ETLVWDB_TS2","ETLVWDB_TS3","ETLVWDB_TS4","ETLVWDB_DV1","ETLVWDB_DV2","ETLVWDB_DV3","ETLVWDB_DV4"],
    "$$SLSORDDB":["SLSORDDB_TS1","SLSORDDB_TS2","SLSORDDB_TS3","SLSORDDB_TS4","SLSORDDB_DV1","SLSORDDB_DV2","SLSORDDB_DV3","SLSORDDB_DV4"],
     "$$ETLONLYDB":["ETLONLYDB_TS1","ETLONLYDB_TS2","ETLONLYDB_TS3","ETLONLYDB_TS4","ETLONLYDB_DV1","ETLONLYDB_DV2","ETLONLYDB_DV3","ETLONLYDB_DV4"],
    "$$COMREFDB":["COMREFDB_TS1","COMREFDB_TS2","COMREFDB_TS3","COMREFDB_TS4","COMREFDB_DV1","COMREFDB_DV2","COMREFDB_DV3","COMREFDB_DV4"],
    "$$WORKDB":["WORKDB_TS1","WORKDB_TS2","WORKDB_TS3","WORKDB_TS4","WORKDB_DV1","WORKDB_DV2","WORKDB_DV3","WORKDB_DV4"],
    "$$EXCEPDB":["EXCEPDB_TS1","EXCEPDB_TS2","EXCEPDB_TS3","EXCEPDB_TS4","EXCEPDB_DV1","EXCEPDB_DV2","EXCEPDB_DV3","EXCEPDB_DV4"],
    "$$FINLGLVWDB":["FINLGLVWDB_TS1","FINLGLVWDB_TS2","FINLGLVWDB_TS3","FINLGLVWDB_TS4","FINLGLVWDB_DV1","FINLGLVWDB_DV2","FINLGLVWDB_DV3","FINLGLVWDB_DV4"],
    "$$NRTNCRVWDB":["NRTNCRVWDB_TS1","NRTNCRVWDB_TS2","NRTNCRVWDB_TS3","NRTNCRVWDB_TS4","NRTNCRVWDB_DV1","NRTNCRVWDB_DV2","NRTNCRVWDB_DV3","NRTNCRVWDB_DV4"],
    }
    s=s.upper()
    global string1
    string1=s
    for i,j in dic.items():
        for k in j:
            if k in s:
                string1=s.replace(k,i)
                s=str(string1)
    return (string1)


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    Delete_input(Output)
    Output.insert(END, func(INPUT))

def Delete_input(val):
    val.delete('1.0', END)


l = Label(text="Enter The SQL:")
l2 = Label(text="Converted SQL:")
inputtxt = Text(root, height=10,
                width=50,
                bg="light yellow")

Output = Text(root, height=50,
              width=50,
              bg="light cyan")

Display1 = Button(root, height=2,
                 width=20,
                 text="Convert database to $$",
                 command=lambda: Take_input())


Display2 = Button(root,height=2,width=20,text="Delete content",command= lambda: Delete_input(Output))

l.pack()
inputtxt.pack()
Display1.pack()
Display2.pack()
l2.pack()
Output.pack()

mainloop()
