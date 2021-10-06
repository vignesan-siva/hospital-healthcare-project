import tkinter
window=tkinter.Tk()
widget=tkinter
window.title("Heart Disease")
window.configure(bg="lightblue")

def heart():
 
    b=int(entry1.get())
    c=int(entry2.get()) 
    d=int(entry3.get())
    e=int(entry4.get())
  
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    data=pd.read_csv("C:\\Users\\elcot\\Desktop\\machine learning tutorial\\hospital_project\\SugarPrediction.csv")
    x=data.iloc[:,[0,4,6,9]].values
    y=data.iloc[:,[-1]].values
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    x_train=sc.fit_transform(x_train)
    x_test=sc.transform(x_test)

    from sklearn.ensemble import RandomForestRegressor
    classifier=RandomForestRegressor()
    classifier.fit(x_train,y_train)
    y_pred=classifier.predict(x_test)
    pred=classifier.predict([[b,c,d,e]])
    result.configure(text="Your Report:"+str(pred),bg="blue",fg='white')

def back():
    window.destroy()
    import main


result=widget.Label()
result.pack()
result.configure(bg="lightblue")
result.place(x=400,y=500,height=40,width=300)



label=widget.Label()
label.pack()
label.configure(text="Find Your Sugar Level",font=("bold",25),bg="lightblue",fg="maroon")
label.place(x=280,y=0)

label1=widget.Label()
label1.pack()
label1.configure(text="Age:",font="bold,arial,20",fg="navy",bg="lightblue")
label1.place(x=330,y=70)

label2=widget.Label()
label2.pack()
label2.configure(text="Eduration:",font="bold,arial,20",fg="navy",bg="lightblue")
label2.place(x=330,y=140)

label3=widget.Label()
label3.pack()
label3.configure(text="BMI: ",font="bold,arial,20",fg="navy",bg="lightblue")
label3.place(x=330,y=210)

label4=widget.Label()
label4.pack()
label4.configure(text="FBS:",font="bold,arial,20",fg="navy",bg="lightblue")
label4.place(x=330,y=280)


#entry box

entry1=widget.Entry()
entry1.pack()
entry1.place(x=450,y=70)

entry2=widget.Entry()
entry2.pack()
entry2.place(x=450,y=140)

entry3=widget.Entry()
entry3.pack()
entry3.place(x=450,y=210)

entry4=widget.Entry()
entry4.pack()
entry4.place(x=450,y=280)

#button
button1=widget.Button()
button1.pack()
button1.configure(text="Submit Report",font=("bold",18),bg="blue",fg="white",command=heart)
button1.place(x=400,y=400)
#back
button2=widget.Button()
button2.pack()
button2.configure(text="<<<<Back",font=("bold",12),bg="green",fg="white",command=back)
button2.place(x=10,y=450)

window.geometry('1000x600')
window.mainloop()


