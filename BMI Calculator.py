# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:44:43 2024

@author: achar
"""

import customtkinter
from tkinter import *
from tkinter import messagebox

app=customtkinter.CTk()
app.title('BMI Calculator')
app.geometry('330x400')
app.config(bg='#000')

font1=('Verdana',30,'bold')
font2=('Verdana',18,'bold')
font3=('Verdana',25,'bold')

def calculate_bmi():
    try:
        height=float(height_entry.get())
        weight=float(weight_entry.get())
        if v2.get()=="ft":
            height*=30.48
        if v1.get()=="lbs":
            weight*=0.453592
        bmi=weight/((height/100)**2)
        if bmi<18.5:
            result_label2.configure(text="You are Underweight")
        elif (bmi>18.5) and (bmi<24.9):
            result_label2.configure(text="You are having\nNormal weight")
        elif(bmi>24.9) and (bmi<29.9):
            result_label2.configure(text="You are Overweight")
        else:
            result_label2.configure(text="You are Obese")
        result_label.configure(text="Your BMI is: {:.1f}".format(bmi))
    except ValueError:
        messagebox.showerror('Error','Enter a valid number!')
    except ZeroDivisionError:
        messagebox.showerror('Error','Height cannot be zero!')

title_label=customtkinter.CTkLabel(app,font=font1,text='BMI Calculator',text_color='#fff',bg_color='#000')
title_label.place(x=40,y=20)

weight_label=customtkinter.CTkLabel(app,font=font2,text='Weight',text_color='#fff',bg_color='#000')
weight_label.place(x=20,y=80)

height_label=customtkinter.CTkLabel(app,font=font2,text='Height',text_color='#fff',bg_color='#000')
height_label.place(x=20,y=150)

weight_entry=customtkinter.CTkEntry(app,font=font2,text_color='#000',bg_color='#000')
weight_entry.place(x=20,y=110)

height_entry=customtkinter.CTkEntry(app,font=font2,text_color='#000',bg_color='#000')
height_entry.place(x=20,y=180)

weight_options=['kg','lbs']
height_options=['cm','ft']
v1=StringVar()
v2=StringVar()

weight_option=customtkinter.CTkComboBox(app,font=font2,text_color='#fff',fg_color='#000',dropdown_hover_color='#06911f',values=weight_options,variable=v1,width=80)
weight_option.place(x=180,y=110)
weight_option.set('kg')

height_option=customtkinter.CTkComboBox(app,font=font2,text_color='#fff',fg_color='#000',dropdown_hover_color='#06911f',values=height_options,variable=v2,width=80)
height_option.place(x=180,y=180)
height_option.set('cm')

calculate_button=customtkinter.CTkButton(app,command=calculate_bmi,font=font2,text_color='#fff',text='Calculate BMI',fg_color='#06911f',hover_color='#06911f',bg_color='#000',cursor='hand2',corner_radius=5,width=200)
calculate_button.place(x=50,y=230)

result_label=customtkinter.CTkLabel(app,text='',font=font3,text_color='#fff',bg_color='#000')
result_label.place(x=30,y=280)
result_label2=customtkinter.CTkLabel(app,text='',font=font3,text_color='#fff',bg_color='#000')
result_label2.place(x=30,y=320)

app.mainloop()