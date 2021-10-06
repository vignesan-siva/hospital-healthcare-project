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
    
    import pandas as pd 
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    data=pd.read_csv("C:\\Users\\elcot\\Desktop\\machine learning tutorial\\classification\\wbcd.csv")
    
    
    from sklearn.preprocessing import LabelEncoder
    labelen=LabelEncoder()
    data['dia']=labelen.fit_transform(data['diagnosis'])
    x=data.iloc[:,[2,4,5,9,22,24,25,29]].values
    y=data.iloc[:,[-1]].values
    
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
    
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    x_train=sc.fit_transform(x_train)
    x_test=sc.transform(x_test)
    
    from sklearn.neighbors import KNeighborsClassifier
    classifier=KNeighborsClassifier(n_neighbors=19,metric='minkowski',p=2)
    classifier.fit(x_train,y_train)
    y_pred=classifier.predict(x_test)
    pred=classifier.predict([[b,c,d,e,f,g,h,i]])
    result.configure(text="Your Report:"+str(pred),bg="blue",fg='white')

def back():
    window.destroy()
    import main



result=widget.Label()
result.pack()
result.configure(bg="lightblue")
result.place(x=400,y=350,height=40,width=300)



label=widget.Label()
label.pack()
label.configure(text="Find Your Begin Cancer or Maligant Cancer",font=("bold",25),bg="lightblue",fg="maroon")
label.place(x=200,y=0)

label1=widget.Label()
label1.pack()
label1.configure(text="Radius_Mean:",font="bold,arial,20",fg="navy",bg="lightblue")
label1.place(x=30,y=70)

label2=widget.Label()
label2.pack()
label2.configure(text="Perimeter_Mean:",font="bold,arial,20",fg="navy",bg="lightblue")
label2.place(x=290,y=70)

label3=widget.Label()
label3.pack()
label3.configure(text="Area_Mean: ",font="bold,arial,20",fg="navy",bg="lightblue")
label3.place(x=550,y=70)

label4=widget.Label()
label4.pack()
label4.configure(text="Points_Mean:",font="bold,arial,20",fg="navy",bg="lightblue")
label4.place(x=30,y=130)

label5=widget.Label()
label5.pack()
label5.configure(text="Radius_Worst:",font="bold,arial,20",fg="navy",bg="lightblue")
label5.place(x=350,y=130)

label6=widget.Label()
label6.pack()
label6.configure(text="Perimeter_Worst: ",font="bold,arial,20",fg="navy",bg="lightblue")
label6.place(x=670,y=130)

label7=widget.Label()
label7.pack()
label7.configure(text="Area_Worst: ",font="bold,arial,20",fg="navy",bg="lightblue")
label7.place(x=30,y=190)

label8=widget.Label()
label8.pack()
label8.configure(text="Points_Worst:",font="bold,arial,20",fg="navy",bg="lightblue")
label8.place(x=400,y=190)


#entry box

entry1=widget.Entry()
entry1.pack()
entry1.place(x=140,y=70)

entry2=widget.Entry()
entry2.pack()
entry2.place(x=420,y=70)

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
entry7.place(x=200,y=190)

entry8=widget.Entry()
entry8.pack()
entry8.place(x=520,y=190)




#button
button1=widget.Button()
button1.pack()
button1.configure(text="Submit Report",font=("bold",18),bg="blue",fg="white",command=heart)
button1.place(x=400,y=300)
#back
button2=widget.Button()
button2.pack()
button2.configure(text="<<<<Back",font=("bold",12),bg="green",fg="white",command=back)
button2.place(x=10,y=400)

window.geometry('1000x600')
window.mainloop()

