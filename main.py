import tkinter
from PIL import Image,ImageTk
window=tkinter.Tk()
widget=tkinter
window.title("personal doctor")
img1=Image.open("C:\\Users\\elcot\Desktop\\machine learning tutorial\\hospital_project\\banner.jpg")
hello=img1.resize((800,600))
img=ImageTk.PhotoImage(hello)



def page1():
    window.destroy()
    import heart_page1

def page2():
    window.destroy()
    import sugar_page2

def page3():
    window.destroy()
    import cancer_page4

def page4():
    window.destroy()
    import bmi_page3
    
    
label=widget.Label()
label.pack()
label.configure(image=img,)
label.place(x=0)

#nav bar
button1=widget.Button()
button1.pack()
button1.configure(text="Heart Disease ",font="bold,20",bg="lightblue",fg='white',command=page1)
button1.place(x=0,y=0)


button2=widget.Button()
button2.pack()
button2.configure(text="Sugar Level Check ",font="bold,20",bg="lightblue",fg='white',command=page2)
button2.place(x=200,y=0)


button3=widget.Button()
button3.pack()
button3.configure(text="Cancer(B&M) Check ",font="bold,20",bg="lightblue",fg='white',command=page3)
button3.place(x=450,y=0)

button4=widget.Button()
button4.pack()
button4.configure(text="BMI Calculate ",font="bold,20",bg="lightblue",fg='white',command=page4)
button4.place(x=680,y=0)

window.geometry("800x600")
window.mainloop()
