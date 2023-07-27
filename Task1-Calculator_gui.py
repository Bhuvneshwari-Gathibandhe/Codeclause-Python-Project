from tkinter import*

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        
        scvalue.set(value)
        screen.update()
        
    elif text =="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    

root =Tk()
root.geometry("400x600")
root.title("Calculator")
#root.wm_iconbitmap("1.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="light blue")
b=Button(f,text="9",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
       
b=Button(f,text="7",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)  
b.bind("<Button-1>",click)
    
f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="6",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
       
b=Button(f,text="4",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)  
b.bind("<Button-1>",click)
    
f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="3",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
       
b=Button(f,text="1",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)  
b.bind("<Button-1>",click)
    
f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="0",padx=10,pady=7,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=10,pady=7,font="lucida 22 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
       
b=Button(f,text="-",padx=10,pady=7,font="lucida 22 bold")
b.pack(side=LEFT,padx=18,pady=5)  
b.bind("<Button-1>",click)
    
f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="*",padx=10,pady=5,font="lucida 24 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=10,pady=5,font="lucida 24 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
       
b=Button(f,text="%",padx=10,pady=10,font="lucida 18 bold")
b.pack(side=LEFT,padx=18,pady=7)  
b.bind("<Button-1>",click)
    
f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text=".",padx=10,pady=5,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)  
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=10,pady=5,font="lucida 20 bold",bg="Blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
 
b=Button(f,text="=",padx=10,pady=5,font="lucida 20 bold",bg="orange")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
    
f.pack()

root.mainloop()