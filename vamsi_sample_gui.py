from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My first Gui Application")
root.configure(background="light blue")
root.geometry("500x200")
headlabel = Label(root, text="Live Extreme!!!",
                  fg='black', bg='light green', relief='flat')
label1 = Label(root, text="First name : ",
               fg='purple', bg='pink', relief='ridge')
label2 = Label(root, text="Middle name : ",
               fg='purple', bg='pink', relief='ridge')
label3 = Label(root, text="Last name: ", fg='purple',
               bg='pink', relief='ridge')
headlabel.grid(row=0, column=1)
label1.grid(row=2, column=0, sticky="E")
label2.grid(row=3, column=0, sticky="E")
label3.grid(row=4, column=0, sticky="E")

first_name_field = Entry(root)
middle_name_field = Entry(root)
last_name_field = Entry(root)

first_name_field.grid(row=2, column=1, ipadx="70")
middle_name_field.grid(row=3, column=1, ipadx="70")
last_name_field.grid(row=4, column=1, ipadx="70")

def print_fields():
    tkinter.messagebox.showinfo("Message for you!!","The values you have inputed have been printed in the output screen.")
    print(first_name_field.get())
    print(middle_name_field.get())
    print(last_name_field.get())
    tkinter.messagebox.showinfo("Here is a secret!!!","You are Awesome!!!")

button1 = Button(root, text="Submit", bg="light yellow",
                 fg="black", command=print_fields, relief='groove')

button1.grid(row=10, column=1)
root.mainloop()
