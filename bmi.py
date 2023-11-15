from packaging import version
from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()

root.title("BMI Calculator")
root.geometry("500x700")

meter = ImageTk.PhotoImage(Image.open("D:\\Meenu\\Projects\\bmi using tkinter\\bmi.png"))
meter_img=Label(root, image=meter, bd=0)
meter_img.pack(pady=20)

def get_bmi():
    height = h_enter.get()
    weight=w_enter.get()
    value1=combobox_h.get()
    value2=combobox_w.get()
    if (value1=="Select units" and value2=="Select units") and (height=="" and weight==""):
        results.configure(text=f"{str('Enter some value for units and height and weight')}")
        return
    if (value1=="Select units" or value2=="Select units") and (height!="" and weight!=""):
        results.configure(text=f"{str('Enter some value for units of height and weight')}")
        return
    elif (height=="" or weight=="") and (value1!="Select units" or value2!="Select units"):
        results.configure(text=f"{str('Enter some value for height and weight')}")
        return
    else:
        height=float(height)
        weight=float(weight)
        if combobox_h.get()=="Centimetres (cm)":
            height/=100
        elif combobox_h.get()=="Inches (in)":
            height*=0.0254
        elif combobox_h.get()=="Feet (ft)":
            height*=0.3048

        if combobox_w.get()=="Pounds (lb)":
            weight*=0.4536
        elif combobox_w.get()=="Grams (g)":
            weight*=0.001
        elif combobox_w.get()=="Ounces(oz)":
            weight*=0.0283
        print("Weight: ",weight)
        bmi=(weight/height**2)
        res=round(bmi,1)
        results.configure(text=f"{str(res)}")

        if res<18.5:
            results.configure(text=f"{str(res)}\nUnderweight", text_color="#54b1e1")
        elif res>=18.5 and res<24.9:
            results.configure(text=f"{str(res)}\nNormal", text_color="#b3d686")
        elif res>=24.9 and res<29.9:
            results.configure(text=f"{str(res)}\nOverweight", text_color="#fed429")
        elif res>=29.9:
            results.configure(text=f"{str(res)}\nObese", text_color="#fbaf42")

def clear_screen():
    h_enter.delete(0,END)
    w_enter.delete(0,END)
    combobox_h.set("Select units")
    combobox_w.set("Select units")
    results.configure(text="")

h_enter=customtkinter.CTkEntry(master=root,
                               placeholder_text="Height",
                               width=150,
                               height=30,
                               border_width=1,
                               corner_radius=10)
h_enter.place(x=150, y=230)
h_enter.pack(pady=10)
combobox_h = customtkinter.CTkComboBox(master=root,
                                     values=["Inches (in)", "Centimetres (cm)", "Metres (m)", "Feet (ft)"],
                                     border_width=1,
                                     width=170,
                                     corner_radius=10)
combobox_h.pack(padx=10, pady=10)
combobox_h.set("Select units")

w_enter=customtkinter.CTkEntry(master=root,
                               placeholder_text="Weight",
                               width=200,
                               height=30,
                               border_width=1,
                               corner_radius=10)
w_enter.pack(pady=10)
combobox_w = customtkinter.CTkComboBox(master=root,
                                     values=["Pounds (lb)", "Kilograms (kg)", "Grams (g)", "Ounces(oz)"],
                                     border_width=1,
                                     width=170,
                                     corner_radius=10)
combobox_w.pack(pady=10)
combobox_w.set("Select units")

btn_1=customtkinter.CTkButton(master=root,
                              text="Calculate BMI",
                              width=190,
                              height=40,
                              compound="top",
                              command=get_bmi)
btn_1.pack(pady=20)

btn_2=customtkinter.CTkButton(master=root,
                              text="Clear Screen",
                              width=190,
                              height=40,
                              fg_color="#D35858",
                              hover_color="#C77C78",
                              command=clear_screen)
btn_2.pack(pady=20)

results=customtkinter.CTkLabel(master=root,
                               text="",
                               font=("Helvitica",18))
results.pack(pady=10)

root.mainloop()
