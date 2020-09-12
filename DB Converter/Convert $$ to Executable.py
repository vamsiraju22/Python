from tkinter import *

root = Tk()
root.geometry("600x600")
root.title(" DB converter ")
def func(s,t):
    import re
    table_list = re.findall(r'\$\$\w+\.\w+', s)
    set_table = set(table_list)

    db_tags = ["$$SLSORDVWDB", "$$STGDB", "$$COMREFVWDB", "$$ETLVWDB", "$$SLSORDDB", "$$ETLONLYDB","$$COMREFDB","$$WORKDB","$$EXCEPDB","$$FINLGLVWDB","$$NRTNCRVWDB","$$slsordvwdb"]

    ts1_tags = ["SLSORDVWDB_TS1", "STGDB_TS1", "COMREFVWDB_TS1", "ETLVWDB_TS1", "SLSORDDB_TS1", "ETLONLYDB_TS1","COMREFDB_TS1","WORKDB_TS1","EXCEPDB_TS1","FINLGLVWDB_TS1","NRTNCRVWDB_TS1","slsordvwdb_ts1"]

    ts3_tags = ["SLSORDVWDB_TS3", "STGDB_TS3", "COMREFVWDB_TS3", "ETLVWDB_TS3", "SLSORDDB_TS3", "ETLONLYDB_TS3","COMREFDB_TS3","WORKDB_TS3","EXCEPDB_TS3","FINLGLVWDB_TS3","NRTNCRVWDB_TS3","slsordvwdb_ts3"]

    dv3_tags = ["SLSORDVWDB_DV3", "STGDB_DV3", "COMREFVWDB_DV3", "ETLVWDB_DV3", "SLSORDDB_DV3", "ETLONLYDB_DV3","COMREFDB_DV3","WORKDB_DV3","EXCEPDB_DV3","FINLGLVWDB_DV3","NRTNCRVWDB_DV3","slsordvwdb_dv3"]

    tag=[]
    if t==1:
        tag=ts1_tags
    if t==3:
        tag=ts3_tags
    if t==2:
        tag=dv3_tags
    for ind, i in enumerate(db_tags):
        str = s.replace(db_tags[ind], tag[ind])
        s = str
    return (str)

def Take_input(val):
    INPUT = inputtxt.get("1.0", "end-1c")
    Delete_input(Output)
    Output.insert(END, func(INPUT,val))

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
                 text="TS3",
                 command=lambda: Take_input(3))

Display2 = Button(root, height=2,
                 width=20,
                 text="TS1",
                 command=lambda: Take_input(1))
Display3 = Button(root, height=2,
                 width=20,
                 text="DV3",
                 command=lambda: Take_input(2))

Display4 = Button(root,height=2,width=20,text="Delete content",command= lambda: Delete_input(Output))

l.pack()
inputtxt.pack()
Display1.pack()
Display2.pack()
Display3.pack()
Display4.pack()
l2.pack()
Output.pack()

mainloop()
