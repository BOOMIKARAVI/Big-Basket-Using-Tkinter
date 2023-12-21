from tkinter import *
from tkinter import messagebox
import tempfile
import os
from tkinter import scrolledtext
from PIL import ImageTk, Image
root=Tk()
root.title('Boomika Stores')
root.geometry('1600x900')
bg='#2D9290'

#------------------Variable-------------------
Oil=IntVar()
Rice=IntVar()
Wheat=IntVar()
Milk=IntVar()
Nuts=IntVar()
total=IntVar()

oi=StringVar()
ri=StringVar()
wh=StringVar()
mi=StringVar()
nu=StringVar()
total_cost=StringVar()







title=Label(root,text='BOOMIKA STORES',bg=bg,fg='white',font=('times  new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

# Background img
# --------------
url = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Downloads\1624873 (1).jpg"))
p1 = Label(root, image = url)
p1.pack(side = "left",fill = "both")

# product details
def item():
        F1=LabelFrame(root,text='Product Details',font=('times new romman',18,'bold'),fg='gold',relief=RIDGE,bd=15)
        F1.place(x=5,y=170,width=800,height=550)

        # Headings
        i=Label(F1,text='Items',font=('Helvetic',25,'bold','underline'),fg='black')
        i.grid(row=0,column=0,padx=20,pady=15)
        n=Label(F1,text='No of Items',font=('Helvetic',25,'bold','underline'),fg='black')
        n.grid(row=0,column=1,padx=20,pady=15)
        cost=Label(F1,text='Cost of Items',font=('Helvetic',25,'bold','underline'),fg='black')
        cost.grid(row=0,column=2,padx=20,pady=15)

        # product

        oil=Label(F1,text='Oil',font=('times new romman',20,'bold','underline'),fg='purple')
        oil.grid(row=1,column=0,padx=20,pady=15)
        o_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Oil)
        o_txt.grid(row=1,column=1,padx=20,pady=15)
        oi_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=oi)
        oi_txt.grid(row=1,column=2,padx=20,pady=15)

        rice=Label(F1,text='Rice',font=('times new romman',20,'bold','underline'),fg='purple')
        rice.grid(row=2,column=0,padx=20,pady=15)
        r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Rice)
        r_txt.grid(row=2,column=1,padx=20,pady=15)
        ri_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=ri)
        ri_txt.grid(row=2,column=2,padx=20,pady=15)

        wheat=Label(F1,text='Wheat',font=('times new romman',20,'bold','underline'),fg='purple')
        wheat.grid(row=3,column=0,padx=20,pady=15)
        w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Wheat)
        w_txt.grid(row=3,column=1,padx=20,pady=15)
        wh_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=wh)
        wh_txt.grid(row=3,column=2,padx=20,pady=15)

        milk=Label(F1,text='Milk',font=('times new romman',20,'bold','underline'),fg='purple')
        milk.grid(row=4,column=0,padx=20,pady=15)
        m_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Milk)
        m_txt.grid(row=4,column=1,padx=20,pady=15)
        mi_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=mi)
        mi_txt.grid(row=4,column=2,padx=20,pady=15)

        nuts=Label(F1,text='Nuts',font=('times new romman',20,'bold','underline'),fg='purple')
        nuts.grid(row=5,column=0,padx=20,pady=15)
        n_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Nuts)
        n_txt.grid(row=5,column=1,padx=20,pady=15)
        nu_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=nu)
        nu_txt.grid(row=5,column=2,padx=20,pady=15)

        t=Label(F1,text='Total Amount',font=('times new romman',20,'bold','underline'),fg='green')
        t.grid(row=6,column=0,padx=20,pady=15)
        t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total)
        t_txt.grid(row=6,column=1,padx=20,pady=15)
        ct_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total_cost)
        ct_txt.grid(row=6,column=2,padx=20,pady=15)

        #------------functions-------------

        def Total():
            if Oil.get()==0 and Rice.get()==0 and Wheat.get()==0 and Milk.get()==0 and Nuts.get()==0:
                messagebox.showerror('Error','Please select number of quantity')
            else:
                o=Oil.get()
                r=Rice.get()
                w=Wheat.get()
                m=Milk.get()
                n=Nuts.get()

            t=float(o*80.0+r*95.0+w*34.0+m*40.0+n*220.0)
            total.set(o+r+w+m+n)
            total_cost.set('Rs '+str(round(t,2)))

            oi.set('Rs '+str(round(o*80.0,2)))
            ri.set('Rs '+str(round(r*95.1,2)))
            wh.set('Rs '+str(round(w*34.2,2)))
            mi.set('Rs '+str(round(m*40.5,2)))
            nu.set('Rs '+str(round(n*220.0,2)))

        def receipt():
                textarea.delete(1.0,END)
                textarea.insert(END,'Items\tNo of Items \tCost of Items')
                textarea.insert(END,f'\n\nOil\t\t{Oil.get()}\t{oi.get()}')
                textarea.insert(END,f'\n\nRice\t\t{Rice.get()}\t{ri.get()}')
                textarea.insert(END,f'\n\nWheat\t\t{Wheat.get()}\t{wh.get()}')
                textarea.insert(END,f'\n\nMilk\t\t{Milk.get()}\t{mi.get()}')
                textarea.insert(END,f'\n\nNuts\t\t{Nuts.get()}\t{nu.get()}')
                textarea.insert(END,'\n\n==================================')
                textarea.insert(END,f'\nTotal Amount:\t\t{total.get()}\t{total_cost.get()}')
                textarea.insert(END,'\n\n==================================')

        def print():
                
                q=textarea.get('1.0','end-1c',)
                filename=tempfile.mktemp('.txt')
                open(filename,'w').write(q)
                os.startfile(filename,'Print')

        def reset():
                textarea.delete(1.0,END)
                Oil.set(0)
                Rice.set(0)
                Wheat.set(0)
                Milk.set(0)
                Nuts.set(0)
                total.set(0)

                oi.set('')
                ri.set('')
                wh.set('')
                mi.set('')
                nu.set('')
                total_cost.set('')


        def exit():
                if messagebox.askyesno('Exit','DO you really want to exit'):
                        root.destroy()

        #-----------------------Bill Area------------------------

        F2=Frame(root,relief=GROOVE,bd=10)
        F2.place(x=820,y=170,width=460,height=550)
        bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F2,orient=VERTICAL)
        textarea=Text(F2,font='arial 15 bold',yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        #textarea=Text(F2,font='arial 15 bold',yscrollcommand=scrol.set)
        scroll_y.config(command=textarea.yview)
        textarea.pack(fill=BOTH)
        receipt()
        

        
        #----------------------Button------------------------------

        F3=Frame(root,relief=GROOVE,bd=10)
        F3.place(x=5,y=710,width=1250,height=120)

        b1=Button(F3,text='Total',font='arial 25 bold',bg='black',fg='crimson',padx=5,pady=5,width=7,command=Total)
        b1.grid(row=0,column=0,padx=10,pady=10)

        b2=Button(F3,text='Receipt',font='arial 25 bold',bg='black',fg='crimson',padx=5,pady=5,width=7,command=receipt)
        b2.grid(row=0,column=1,padx=10,pady=10)

        b3=Button(F3,text='Print',font='arial 25 bold',bg='black',fg='crimson',padx=5,pady=5,width=7,command=print)
        b3.grid(row=0,column=2,padx=10,pady=10)

        b4=Button(F3,text='Reset',font='arial 25 bold',bg='black',fg='crimson',padx=5,pady=5,width=7,command=reset)
        b4.grid(row=0,column=3,padx=10,pady=10)

        b5=Button(F3,text='Exit',font='arial 25 bold',bg='black',fg='crimson',padx=5,pady=5,width=7,command=exit)
        b5.grid(row=0,column=4,padx=10,pady=10)


        
        



# Button          
# ------
B3 = Button(root,text='New Order',bg='pink',font=20,command=item)
B3.place(x=650,y=90)





root.mainloop()

