'''hints
list of images,use label.grid_forget() to erease current label,
use list of images, use buttons to navigate back and forth, and customise accordingly,
disable forward and last button(Make it initially disabled) when you reach the last image'''
from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.title("Image viewer")
root.iconbitmap('icon.ico')
root.geometry("350x380")

def forwards(img_num):
    global label
    global forward
    global back
    global num_display
    
    label.grid_forget()
    label=Label(image=imgage_list[img_num-1])
    label.grid(row=1,column=0,columnspan=3,padx=20,pady=10)
    num_display.grid_forget()
    num_display=Label(root,text=str(imgage_list.index(imgage_list[img_num-1])+1)+" of "+str(len(imgage_list)),font=("Arial", 12, "bold"))
    num_display.grid(row=0,column=1)
    
    if (img_num==len(imgage_list)):
        forward=Button(root,text=">>",command=lambda: forwards(img_num+1),state=DISABLED,width=8,bg='#0A0A0A',fg='white').grid(row=2,column=2)
    else:
        forward=Button(root,text=">>",command=lambda: forwards(img_num+1),width=8,bg='#0A0A0A',fg='white').grid(row=2,column=2)
        
    back=Button(root,text="<<",command=lambda: backs(img_num-1),width=8,bg='#0A0A0A',fg='white').grid(row=2,column=0)
    
def backs(img_num):
    global label
    global forward
    global back
    global num_display
    
    label.grid_forget()
    label=Label(image=imgage_list[img_num-1])
    label.grid(row=1,column=0,columnspan=3,padx=20,pady=10)
    forward=Button(root,text=">>",command=lambda: forwards(img_num+1),width=8,bg='#0A0A0A',fg='white')
    back=Button(root,text="<<",command=lambda: backs(img_num-1),width=8,bg='#0A0A0A',fg='white')
    
    num_display.grid_forget()
    num_display=Label(root,text=str(imgage_list.index(imgage_list[img_num-1])+1)+" of "+str(len(imgage_list)),font=("Arial", 12, "bold"))
    num_display.grid(row=0,column=1)
    
    if img_num==1:
        back=Button(root,text="<<",state=DISABLED,command=lambda: backs(img_num-1),width=8,bg='#0A0A0A',fg='white')
    forward.grid(row=2,column=2)
    back.grid(row=2,column=0)


#initials images
im1 =Image.open("a.jpg").resize((300,300))
im2 =Image.open("b.jpg").resize((300,300))
im3 =Image.open("c.jpg").resize((300,300))
im4 =Image.open("d.jpg").resize((300,300))
im5 =Image.open("e.jpg").resize((300,300))

im1=ImageTk.PhotoImage(im1)
im2=ImageTk.PhotoImage(im2)
im3=ImageTk.PhotoImage(im3)
im4=ImageTk.PhotoImage(im4)
im5=ImageTk.PhotoImage(im5)

imgage_list=[im1,im2,im3,im4,im5]

#image number displayer
label=Label(image=im1)
label.grid(row=1,column=0,columnspan=3,padx=20,pady=10)
num_display=Label(root,text=" 1 of "+str(len(imgage_list)),font=("Arial", 12, "bold"))
num_display.grid(row=0,column=1)

#initial buttons
forward=Button(root,text=">>",command=lambda: forwards(2),width=8,bg='#0A0A0A',fg='white').grid(row=2,column=2)
exit=Button(root,text="Exit",command=root.quit,width=8,bg='red',fg='yellow').grid(row=2,column=1)
back=Button(root,text="<<",command=lambda: backs(2),state= DISABLED,width=8,bg='#0A0A0A',fg='white').grid(row=2,column=0)



root.mainloop()





