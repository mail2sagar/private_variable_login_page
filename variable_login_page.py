from tkinter import *

root = Tk()

root.title("Private Variable Login Page")
root.geometry("600x500")
root.config(background="light cyan")


name_label = Label(root,text="Name- ",bg="powder blue",font=("Bahnschrift Light",15))
name_label.place(relx=0.3,rely=0.15,anchor=CENTER)


pass_label = Label(root,text="Password- ",bg="powder blue",font=("Bahnschrift Light",15))
pass_label.place(relx=0.3,rely=0.25,anchor=CENTER)


cap_label = Label(root,text="Captcha- ",bg="powder blue",font=("Bahnschrift Light",15))
cap_label.place(relx=0.3,rely=0.35,anchor=CENTER)


ent1 = Entry(root)
ent1.place(relx=0.7,rely=0.15,anchor=CENTER)


ent2 = Entry(root)
ent2.place(relx=0.7,rely=0.25,anchor=CENTER)


ent3 = Entry(root)
ent3.place(relx=0.7,rely=0.35,anchor=CENTER)


class UserDB:
    def __init__(self):
      self.__username = ent1.get()
      self.__password = ent2.get()
      self.__captcha = ent3.get()

      label_show_name["text"] = "Name: "+self.__username
      label_show_pass["text"] = "Name: "+self.__password
      label_show_cap["text"] = "Name: "+self.__captcha




btn_user_details = Button(root,text="Update Login Details",bg="powder blue",font=("Bahnschrift Light",15,"bold"))
btn_user_details.place(relx=0.3,rely=0.6,anchor=CENTER)

btn_show_profile = Button(root,text="Show Profile",bg="powder blue",font=("Bahnschrift Light",15,"bold"))
btn_show_profile.place(relx=0.7,rely=0.6,anchor=CENTER)


root.mainloop()