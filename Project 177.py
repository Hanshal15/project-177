# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:33:41 2021

@author: tripp
"""

from tkinter import *

root = Tk()
root.geometry = ("700x700")
root.title("Encapsulation")

label_name = Label(root,text = "Name : ")
enter_name = Entry(root)

label_name.place(relx = 0.3,rely = 0.2,anchor = CENTER)
enter_name.place(relx = 0.6,rely = 0.2,anchor = CENTER)

label_pass = Label(root,text = "Password : ")
enter_pass = Entry(root)

label_pass.place(relx = 0.3,rely = 0.3,anchor = CENTER)
enter_pass.place(relx = 0.6,rely = 0.3,anchor = CENTER)

label_captcha = Label(root,text = "Captcha : ")
enter_captcha = Entry(root)

label_captcha.place(relx = 0.3,rely = 0.4,anchor = CENTER)
enter_captcha.place(relx = 0.6,rely = 0.4,anchor = CENTER)

label_name_store = Label(root)

label_name_store.place(relx = 0.5,rely = 0.7,anchor = CENTER)

label_pass_store = Label(root)

label_pass_store.place(relx = 0.5,rely = 0.8,anchor = CENTER)

label_captcha_store = Label(root)

label_captcha_store.place(relx = 0.5,rely = 0.9,anchor = CENTER)

class userDB:
    def __init__(self):
        self.__username = "asdf"
        self.__password = "asdf_M()v!E"
        self.__captcha = "fdsa"
        
    def showUser():
        label_name_store["text"] = "Name : " + self.__username    
        label_pass_store["text"] = "password : " + self.__username    
        label_captcha_store["text"] = "captcha : " + self.__username  
        
user_db  = userDB()
def add_user(self):
    global user_db
    user_db.username = enter_name.get()
    user_db.password = enter_pass.get()
    user_db.captcha = enter_captcha.get()
    print("Values Updated")
    
btn_update = Button(root, text = "Update Login Details", command = add_user)    
btn_update.place(relx = 0.3, rely = 0.5, anchor = CENTER) 

btn_show = Button(root, text = "Show Profile", command = user_db.showUser)    
btn_show.place(relx = 0.6, rely = 0.5, anchor = CENTER)       

root.mainloop()