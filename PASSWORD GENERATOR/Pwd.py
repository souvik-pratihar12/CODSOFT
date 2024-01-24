#
from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry("500x300")


#generate random password
def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ''
    for x in range(pw_length):
        my_password += chr(randint(33,126))
    pw_entry.insert(0, my_password)

#copy to clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

#label frame
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

#create entry box to designate number of characters
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#create entry box for returned password
pw_entry = Entry(root, text='', font=("Helvetica",24))
pw_entry.pack(pady=20)

#create a frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#create buttons
my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
