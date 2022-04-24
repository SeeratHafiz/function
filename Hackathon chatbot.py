from tkinter import *
root = Tk()
def send():
    send="You :"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hello "):
        txt.insert(END,"\n"+"computer : hii ")
    elif (e.get()=="hii"):
        txt.insert(END,"\n"+"computer: Hello ")
    elif (e.get()=="how are you"):
        txt.insert(END,"\n"+"computer: fine and u")
    elif (e.get()=="i am also fine"):
        txt.insert(END,"\n"+"computer : nice to hear u")
    elif (e.get()=="do you want tea or coffee"):
        txt.insert(END,"\n"+"computer :coffee")
    else:
        txt.insert(END,"\n"+"computer : sorry i didn't get it ")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()

