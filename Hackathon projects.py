#import tkinter as tk
#window = tk.TK()

# from tkinter import *
# root=Tk()
# my_label=Label(root,text="Hello World i love python")
# my_label.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()
# root.title('MY BOX GUI')
# root.geometry("500x500")
# # root.iconbitmap('apple.ico)
# my_label1= Label(root, text='Hii').pack()
# my_label2= Label(root,text='How you doing today ?').pack()

# root.mainloop()


# from tkinter import *
# root=Tk()

# root.title("MY GUI APP")
# root.geometry("500x500")

# my_label = Label(root, text="My new GUI app !").grid(row=0,column=1)
# my_label = Label(root, text="This is line 2").grid(row=0,column=2)

# root.mainloop()

# from tkinter import *
# root=Tk()

# root.title("MY BUTTON")
# root.geometry("500x500")

# def my_click():
#     my_label =Label(root,text="WELCOME TO THE COURSE!",fg="blue")
#     my_label.pack()

# mybutton = Button(root, text= "HEY CLICK THIS!",command= my_click,fg="yellow",bg="black",padx=25,pady=30)
# mybutton.pack()

# root.mainloop()

# from tkinter import *
# root=Tk()

# root.title("MY BUTTON")
# root.geometry("800x800")


# e= Entry(root, width = 30, fg ='red')
# e.grid(row=0, column=1)

# ee= Entry(root, width =30, fg='black')
# e.grid(row=0,column=2)

# def clickme():
#     mylabel = Label(root, text='Hello'+''+ e.get())
#     mylabel.grid(row=3,column=1)

# def click2():
#     mylabel = Label(root, text='Hello'+''+ ee.get())
#     mylabel.grid(row=3,column=2)


# mybutton = Button(root, text="ENTER YOUR FIRST NAME",padx=10, pady=10,bg='white',fg='green',command=clickme)
# mybutton.grid(row=2,column=1)

# mybutton = Button(root, text="ENTER YOUR LAST NAME",padx=10, pady=10,bg='white',fg='green',command=click2)
# mybutton.grid(row=2,column=2)

# root.mainloop()




from tkinter import *
root=Tk()


root.geometry("800x800")

q=IntVar()
q.get()
q.set('2')



def clickme(value):
    my_label=Label(root, text=value)
    my_label.pack()

Radiobutton(root, text="Option 1", variable=q , value =1).pack(anchor="w")
Radiobutton(root, text="Option 2", variable=q , value =2).pack(anchor="w")
Radiobutton(root, text="Option 3", variable=q , value =3).pack(anchor="w")
Radiobutton(root, text="Option 4", variable=q , value =4).pack(anchor="w")

my_label= Label(root, text= q.get())
my_label.pack()

my_button = Button(root, text ="SUBMIT!",command=lambda:clickme(q.get()))
my_button.pack()

root.mainloop()




