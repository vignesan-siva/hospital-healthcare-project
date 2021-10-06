import tkinter
window=tkinter.Tk()
widget=tkinter
window.title("BMI")
window.configure(bg="lightblue")

def heart():
 
    b=int(entry1.get())
    c=int(entry2.get()) 
    bmi=(b/c/c)*10000
    

    result.configure(text="Your Report:"+str(bmi),bg="blue",fg='white')

def back():
    window.destroy()
    import main


result=widget.Label()
result.pack()
result.configure(bg="lightblue")
result.place(x=400,y=300,height=40,width=300)



label=widget.Label()
label.pack()
label.configure(text="Find Your BMI",font=("bold",25),bg="lightblue",fg="maroon")
label.place(x=340,y=0)

label1=widget.Label()
label1.pack()
label1.configure(text="Weight:",font="bold,arial,20",fg="navy",bg="lightblue")
label1.place(x=330,y=70)

label2=widget.Label()
label2.pack()
label2.configure(text="Height:",font="bold,arial,20",fg="navy",bg="lightblue")
label2.place(x=330,y=140)


#entry box

entry1=widget.Entry()
entry1.pack()
entry1.place(x=450,y=70)

entry2=widget.Entry()
entry2.pack()
entry2.place(x=450,y=140)


#button
button1=widget.Button()
button1.pack()
button1.configure(text="Submit Report",font=("bold",18),bg="blue",fg="white",command=heart)
button1.place(x=380,y=200)
#back
button2=widget.Button()
button2.pack()
button2.configure(text="<<<<Back",font=("bold",12),bg="green",fg="white",command=back)
button2.place(x=10,y=350)


window.geometry('1000x400')
window.mainloop()



