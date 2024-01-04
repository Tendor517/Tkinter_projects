from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.geometry("350x390")

#Entry field
e=Entry(root,width=50,bg='white',fg='black',borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
# e.insert(0,"Calculate")

first=0
op=""
#functions
def Ans(Res):
    e.delete(0,END)
    res=str(Res)
    e.insert(0,Res)
    return
    
def ButtonClick(number):
    prev=e.get()
    e.delete(0,END)
    e.insert(0,str(prev)+str(number))
    
def Add(sign):
    global first,op
    op=sign
    first=int(e.get())
    e.delete(0,END)
    
def Subtract(sign):
    global first,op
    op=sign
    first=int(e.get())
    e.delete(0,END)
    
def Multiply(sign):
    global first,op
    op=sign
    first=int(e.get())
    e.delete(0,END)
    
def Divide(sign):
    global first,op
    op=sign
    first=int(e.get())
    e.delete(0,END)

def Equal():
    global op,first
    match op:
        case '+':
            res=int(e.get())+first
            Ans(res)
        case '-':
            res=first-int(e.get())
            Ans(res)
        case '*':
            res=int(e.get())*first
            Ans(res)
        case '%':
            if (int(e.get())==0):
                #raise ValueError('Division Error!')
                e.delete(0,END)
                e.insert(0,"Division Error")
                Clear()
            else:
                res=first/int(e.get())
                Ans(res)
           
def Clear():
    e.delete(0,END)


#Buttons
But1=Button(root,text="1",width=5,padx=5,pady=5,command=lambda: ButtonClick(1),fg='white',bg='brown',font=('Times New Roman', 15, 'bold'))
But2=Button(root,text="2",width=5,padx=5,pady=5,command=lambda: ButtonClick(2),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But3=Button(root,text="3",width=5,padx=5,pady=5,command=lambda: ButtonClick(3),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But4=Button(root,text="4",width=5,padx=5,pady=5,command=lambda: ButtonClick(4),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But5=Button(root,text="5",width=5,padx=5,pady=5,command=lambda: ButtonClick(5),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But6=Button(root,text="6",width=5,padx=5,pady=5,command=lambda: ButtonClick(6),fg= 'white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But7=Button(root,text="7",width=5,padx=5,pady=5,command=lambda: ButtonClick(7),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But8=Button(root,text="8",width=5,padx=5,pady=5,command=lambda: ButtonClick(8),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But9=Button(root,text="9",width=5,padx=5,pady=5,command=lambda: ButtonClick(9),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
But0=Button(root,text="0",width=5,padx=5,pady=5,command=lambda: ButtonClick(0),fg='white',bg='brown',font=('Times New Roman', 15, 'bold')) 
Plus=Button(root,text="+",width=5,padx=5,pady=5,command=lambda: Add('+'),fg='white',bg='black',font=('Times New Roman', 15, 'bold')) 
Minus=Button(root,text="-",width=5,padx=5,pady=5,command=lambda: Subtract('-'),fg='white',bg='black',font=('Times New Roman', 15, 'bold')) 
Equal=Button(root,text="=",width=5,padx=5,pady=5,command=Equal,fg='white',bg='black',font=('Times New Roman', 15, 'bold')) 
Mult=Button(root,text="*",width=5,padx=5,pady=5,command=lambda: Multiply('*'),fg='white',bg='black',font=('Times New Roman', 15, 'bold'))
Div=Button(root,text="%",width=5,padx=5,pady=5,command=lambda: Divide('%'),fg='white',bg='black',font=('Times New Roman', 15, 'bold'))
Clear=Button(root,text="Clear",width=24,command=Clear,fg='yellow',bg='red',font=('Times New Roman', 15, 'bold'))
#Button grids
But7.grid(row=1,column=0,pady=5)
But8.grid(row=1,column=1,pady=5)
But9.grid(row=1,column=2,pady=5)
But4.grid(row=2,column=0,pady=5)
But5.grid(row=2,column=1,pady=5)
But6.grid(row=2,column=2,pady=5)
But1.grid(row=3,column=0,pady=5)
But2.grid(row=3,column=1,pady=5)
But3.grid(row=3,column=2,pady=5)
But0.grid(row=4,column=0,pady=5)
Plus.grid(row=4,column=1,pady=5)
Minus.grid(row=4,column=2,pady=5)
Mult.grid(row=5,column=0,pady=5)
Div.grid(row=5,column=1,pady=5)
Equal.grid(row=5,column=2,pady=5)
Clear.grid(row=6,column=0,columnspan=3,padx=10,pady=10)



root.mainloop()
        