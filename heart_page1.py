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
    f=int(entry5.get())
    g=int(entry6.get())
    h=int(entry7.get())
    i=int(entry8.get())
    j=int(entry9.get())
    k=int(entry10.get())
    l=int(entry11.get())
    m=int(entry12.get())
    a=int(entry13.get())
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    data=pd.read_csv("C:\\Users\\elcot\\Desktop\\machine learning tutorial\\hospital_project\\heart.csv")
    x=data.iloc[:,0:13].values
    y=data.iloc[:,[-1]].values
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    x_train=sc.fit_transform(x_train)
    x_test=sc.transform(x_test)

    from sklearn.svm import SVC
    classifier=SVC(C=1,kernel='rbf',gamma=0.2)
    classifier.fit(x_train,y_train)
    y_pred=classifier.predict(x_test)
    pred=classifier.predict([[b,c,d,e,f,g,h,i,j,k,l,m,a]])
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
label.configure(text="Find Your Heart Disease Level",font=("bold",25),bg="lightblue",fg="maroon")
label.place(x=200,y=0)

label1=widget.Label()
label1.pack()
label1.configure(text="Age:",font="bold,arial,20",fg="navy",bg="lightblue")
label1.place(x=30,y=70)

label2=widget.Label()
label2.pack()
label2.configure(text="Sex(1 and 0):",font="bold,arial,20",fg="navy",bg="lightblue")
label2.place(x=250,y=70)

label3=widget.Label()
label3.pack()
label3.configure(text="chest pain type: ",font="bold,arial,20",fg="navy",bg="lightblue")
label3.place(x=550,y=70)

label4=widget.Label()
label4.pack()
label4.configure(text="resting blood pressure:",font="bold,arial,20",fg="navy",bg="lightblue")
label4.place(x=30,y=130)

label5=widget.Label()
label5.pack()
label5.configure(text="serum cholestoral:",font="bold,arial,20",fg="navy",bg="lightblue")
label5.place(x=350,y=130)

label6=widget.Label()
label6.pack()
label6.configure(text="fasting blood sugar: ",font="bold,arial,20",fg="navy",bg="lightblue")
label6.place(x=670,y=130)

label7=widget.Label()
label7.pack()
label7.configure(text="resting electrocardiographic: ",font="bold,arial,20",fg="navy",bg="lightblue")
label7.place(x=30,y=190)

label8=widget.Label()
label8.pack()
label8.configure(text="maximum heart rate achieved:",font="bold,arial,20",fg="navy",bg="lightblue")
label8.place(x=400,y=190)

label9=widget.Label()
label9.pack()
label9.configure(text="exercise induced angina:",font="bold,arial,20",fg="navy",bg="lightblue")
label9.place(x=30,y=250)

label10=widget.Label()
label10.pack()
label10.configure(text="oldpeak :",font="bold,arial,20",fg="navy",bg="lightblue")
label10.place(x=350,y=250)

label11=widget.Label()
label11.pack()
label11.configure(text="the slope of the peak exercise :",font="bold,arial,20",fg="navy",bg="lightblue")
label11.place(x=530,y=250)

label12=widget.Label()
label12.pack()
label12.configure(text="number of major vessels (0-3): ",font="bold,arial,20",fg="navy",bg="lightblue")
label12.place(x=30,y=310)

label3=widget.Label()
label3.pack()
label3.configure(text="thal:(0,1,2):",font="bold,arial,20",fg="navy",bg="lightblue")
label3.place(x=480,y=310)

#entry box

entry1=widget.Entry()
entry1.pack()
entry1.place(x=80,y=70)

entry2=widget.Entry()
entry2.pack()
entry2.place(x=350,y=70)

entry3=widget.Entry()
entry3.pack()
entry3.place(x=680,y=70)

entry4=widget.Entry()
entry4.pack()
entry4.place(x=200,y=130)


entry5=widget.Entry()
entry5.pack()
entry5.place(x=490,y=130)

entry6=widget.Entry()
entry6.pack()
entry6.place(x=820,y=130)

entry7=widget.Entry()
entry7.pack()
entry7.place(x=240,y=190)

entry8=widget.Entry()
entry8.pack()
entry8.place(x=630,y=190)


entry9=widget.Entry()
entry9.pack()
entry9.place(x=210,y=250)

entry10=widget.Entry()
entry10.pack()
entry10.place(x=430,y=250)

entry11=widget.Entry()
entry11.pack()
entry11.place(x=760,y=250)

entry12=widget.Entry()
entry12.pack()
entry12.place(x=290,y=310)

entry13=widget.Entry()
entry13.pack()
entry13.place(x=590,y=310)

#button
button1=widget.Button()
button1.pack()
button1.configure(text="Submit Report",font=("bold",18),bg="blue",fg="white",command=heart)
button1.place(x=400,y=400)
#back
button2=widget.Button()
button2.pack()
button2.configure(text="<<<<Back",font=("bold",12),bg="green",fg="white",command=back)
button2.place(x=10,y=500)

window.geometry('1000x600')
window.mainloop()
