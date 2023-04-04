from tkinter import *
from tkinter import ttk #Therm of Tk
from tkinter import messagebox
GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม

GUI.title('โปรแกรมบันทึกข้อมูล')#title name
GUI.geometry('510x500')# size 
#B1=ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)

###################
def Button2 () :
    text = 'ตอนนี้มี้งินอยู่ในบัญชี300บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1= LabelFrame(GUI,text ='Money')
FB1.place(x=20,y=10)
B2=ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
#########################
def Button3 () :
    text = 'ไม่บอกหรอก'
    messagebox.showwarning('วิชาเรียน',text)

FB2= LabelFrame(GUI,text='การศึกษา')
FB2.place(x=200,y=10)
B3=ttk.Button(FB2,text='การศึกษา',command=Button3)
B3.pack(ipadx=20,ipady=20)
#######################
def Button4 () :
    text = 'ต้มข่าไก่'
    messagebox.showwarning('วิชาเรียน',text)

FB4= LabelFrame(GUI,text='อาหาร')
FB4.place(x=380,y=10)
B4=ttk.Button(FB4,text='เมนู',command=Button4)
B4.pack(ipadx=20,ipady=20)
#######################
def Button5 () :
    text = 'ห่า'
    messagebox.showerror('ตาย',text)

FB5= LabelFrame(GUI,text='ดูดวง')
FB5.place(x=200,y=100)
B5=ttk.Button(FB5,text='ดวงประจำราศี',command=Button5)
B5.pack(ipadx=20,ipady=20)
#######################
def Button6 () :
    text = 'อย่าทำวันนี้ให้ดัที่สุด'
    messagebox.showwarning('คำพูดให้กำลังใจ',text)

FB6= LabelFrame(GUI,text='คำพูดฮีลใจ')
FB6.place(x=200,y=400)
B6=ttk.Button(FB6,text='ตอนกำลังท้อ',command=Button6)
B6.pack(ipadx=20,ipady=20)
#######################
GUI.mainloop()
