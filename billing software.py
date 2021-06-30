# final software
from tkinter import *
import random
import os
from tkinter import messagebox                       

class b():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("billing software")
        bg_color='royalBlue3' #this is the color for bg
        title=Label(self.root,text='Billing software',bd=2,relief=GROOVE,font=('times new roamn',30),pady=2,bg=bg_color,fg='white')
        title.pack(fill=X)
        # frame 1 

        self.soap=IntVar()
        self.soap1=IntVar()
        self.soap2=IntVar()

        #kinds items
        self.dom1=IntVar()
        self.dom2=IntVar()
        self.dom3=IntVar()
        self.dom4=IntVar()
        self.dom5=IntVar()
        self.dom6=IntVar()


        # customer details
        self.cname_lab1=StringVar()
        self.cname_con_no=StringVar()
              
        self.cname_bill=StringVar()
        x=random.randint(10000,99999)
        self.cname_bill.set(str(x))
        self.cname_btn=StringVar()

        # billing

        self.cosmatic_price = StringVar()
        self.kids_price = StringVar()
        







        

        # this is for customer details f1 is ''' frame 1'''
        f1 = LabelFrame(self.root,text='customer details',font=('times new roamn',15,'bold'),fg='gold',bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)

        cname_lab1=Label(f1,text='customer name',font=('times new roman',12))
        cname_lab1.grid(row=0,column=0)
        cname_text=Entry(f1,textvariable=self.cname_lab1,width=20,font='arial 15',bd=7,relief=SUNKEN)
        cname_text.grid(row=0,column=1,padx=10,pady=5)

        cname_con_no=Label(f1,text='contact No',font=('times new roman',12))
        cname_con_no.grid(row=0,column=3)
        cname_text=Entry(f1,textvariable=self.cname_con_no,width=20,font='arial 15',bd=7,relief=SUNKEN)
        cname_text.grid(row=0,column=4,padx=10,pady=5)

        cname_bill=Label(f1,text='Bill No',font=('times new roman',12))
        cname_bill.grid(row=0,column=5)
        cname_text=Entry(f1,textvariable=self.cname_bill,width=20,font='arial 15',bd=7,relief=SUNKEN)
        cname_text.grid(row=0,column=6,padx=10,pady=5)
            


        # this is the frame2
        f2=LabelFrame(self.root,text='products list',font=('times new roamn',15,'bold'),fg='gold',bg=bg_color)
        f2.place(x=0,y=180,width=325,heigh=380)

        soap=Label(f2,text='rice',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        soap.grid(row=0,column=3)
        soap=Entry(f2,textvariable=self.soap,width=5,font='arial 15',bd=2,relief=SUNKEN)
        soap.grid(row=0,column=4,padx=10,pady=5)

        soap1=Label(f2,text='sugar',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        soap1.grid(row=1,column=3)
        soap1=Entry(f2,textvariable=self.soap1,width=5,font='arial 15',bd=2,relief=SUNKEN)
        soap1.grid(row=1,column=4,padx=10,pady=5)

        soap2=Label(f2,text='foot oil',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        soap2.grid(row=2,column=3)
        soap2=Entry(f2,textvariable=self.soap2,width=5,font='arial 15',bd=2,relief=SUNKEN)
        soap2.grid(row=2,column=4,padx=10,pady=5)

        





        
                        

        #this is the frame 3


        f3=LabelFrame(self.root,text='product list',font=('times new roamn',15,'bold'),fg='gold',bg=bg_color)
        f3.place(x=350,y=180,width=325,heigh=380)

        dom1=Label(f3,text='diary',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        dom1.grid(row=2,column=3)
        dom1=Entry(f3,textvariable=self.dom1,width=5,font='arial 15',bd=2,relief=SUNKEN)
        dom1.grid(row=2,column=4,padx=10,pady=5)

        dom2=Label(f3,text='egg',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        dom2.grid(row=3,column=3)
        dom2=Entry(f3,width=5,textvariable=self.dom2,font='arial 15',bd=2,relief=SUNKEN)
        dom2.grid(row=3,column=4,padx=10,pady=5)

        dom3=Label(f3,text='bread',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        dom3.grid(row=4,column=3)
        dom3=Entry(f3,textvariable=self.dom3,width=5,font='arial 15',bd=2,relief=SUNKEN)
        dom3.grid(row=4,column=4,padx=10,pady=5)


        #frame 4

        f4=LabelFrame(self.root,text='kids items',font=('times new roamn',15,'bold'),fg='gold',bg=bg_color)
        f4.place(x=700,y=180,width=300,heigh=380)

        dom4=Label(f4,text='chocos',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        dom4.grid(row=2,column=3)
        dom4=Entry(f4,textvariable=self.dom4,width=5,font='arial 15',bd=2,relief=SUNKEN)
        dom4.grid(row=2,column=4,padx=10,pady=5)

        
        dom5=Label(f4,text='5 star',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        dom5.grid(row=3,column=3)
        dom5=Entry(f4,textvariable=self.dom5,width=5,font='arial 15',bd=2,relief=SUNKEN)
        dom5.grid(row=3,column=4,padx=10,pady=5)

        
        dom6=Label(f4,text='magi',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        dom6.grid(row=4,column=3)
        dom6=Entry(f4,textvariable=self.dom6,width=5,font='arial 15',bd=2,relief=SUNKEN)
        dom6.grid(row=4,column=4,padx=10,pady=5)
        
        
        

        #billing areas
        f5=Frame(self.root,relief=GROOVE,bd=10)
        f5.place(x=1010,y=180,width=325,heigh=380)
              
        bill_title=Label(f5,text='bill Area',font=('arial',15,'bold'),bd=7,relief=GROOVE)
        bill_title.pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #+++++++++++ button frame



        f6=LabelFrame(self.root,text='button area',font=('times new roamn',15,'bold'),fg='gold',bg=bg_color)
        f6.place(x=0,y=560,relwidth=1,heigh=140)


        b1=Label(f6,text='total cost',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        b1.grid(row=1,column=5)
        b1=Entry(f6,textvariable=self.cosmatic_price,width=10,font='arial 15',bd=2,relief=SUNKEN)
        b1.grid(row=1,column=8,padx=10,pady=5)

        #b2=Label(f6,text='kids items',font=('times new roman',15,'bold'),bg=bg_color,fg='black')
        #b2.grid(row=2,column=3)
        #b2=Entry(f6,textvariable=self.kids_price,width=10,font='arial 15',bd=2,relief=SUNKEN)
        #b2.grid(row=2,column=4,padx=10,pady=5)

        #buttons sections

        btn=Frame(f6,bd=7,relief=GROOVE)
        btn.place(x=750,width=580,height=105)

        total=Button(btn,text='total',command=self.total,bg='cadetblue',fg='white',pady=15,padx=15,font='bold''arial')
        total.grid(row=0,column=0,pady=15,padx=15)

        gbill=Button(btn,text='generate bill',command=self.bill_area,bg='cadetblue',fg='white',pady=15,padx=15,font='bold''arial')
        gbill.grid(row=0,column=1,pady=15,padx=15)

        clear=Button(btn,text='clear',bg='cadetblue',command=self.clear_data,fg='white',pady=15,padx=15,font='bold''arial')
        clear.grid(row=0,column=2,pady=15,padx=15)

        ext=Button(btn,text='Exit',bg='cadetblue',command=self.exit,fg='white',pady=15,padx=15,font='bold''arial')
        ext.grid(row=0,column=3,pady=15,padx=15)
    def total(self):
        
        self.c_s_p=self.soap.get()*100
        self.c_s1_p=self.soap1.get()*25
        self.c_s2_p=self.soap2.get()*105
        self.d_m1=self.dom1.get()*50
        self.d_m2=self.dom2.get()*5
        self.d_m3=self.dom3.get()*45
        self.d_m4=self.dom4.get()*10
        self.d_m5=self.dom5.get()*28
        self.d_m6=self.dom6.get()*15

        
        self.total_cosmatic_price=float(
                      self.c_s_p+
                      self.c_s1_p+
                      self.c_s2_p+
                      self.d_m1+
                      self.d_m2+
                      self.d_m3+
                      self.d_m4+
                      self.d_m5+
                      self.d_m6)
                     
                     
        self.cosmatic_price.set("Rs."+str(self.total_cosmatic_price))


        #this customise

        '''self.d_m1=self.dom1.get()*100
        self.d_m2=self.dom2.get()*200
        self.d_m3=self.dom3.get()*300'''

    
        '''self.total_kids_price=float(
                      self.d_m1+
                      self.d_m2+
                      self.d_m3)
                     
        self.kids_price.set(""+str(self.total_kids_price))'''


    def welcome_bill(self):
        self.txtarea.insert(END,"\t welcome tesa retail")
        self.txtarea.insert(END,f"\ncnumber   :{self.cname_bill.get()}")
        self.txtarea.insert(END,f"\ncustomer name :{self.cname_lab1.get()}")
        self.txtarea.insert(END,f"\nphone number  :{self.cname_con_no.get()}")
        self.txtarea.insert(END,f"\n============================")
        self.txtarea.insert(END,f"\n PRODUCT\t QTY\t price")
        self.txtarea.insert(END,f"\n============================")

        
        #self.txtarea.insert(END,f"\n---------------------")
        #self.txtarea.insert(END,f"\n GRAND TOTAL :\t\t{self.total_cosmatic_price}")
        #self.txtarea.insert(END,f"\n---------------------")



    def bill_area(self):
        if self.cosmatic_price.get()=='Rs.0.0':
            messagebox.showerror("error","please select products")
        
        
        elif self.cname_lab1.get()=='' or self.cname_con_no.get()=='':
            messagebox.showerror("ERROR", "please enter data" )
            
                 
        
        

            
        else:
            self.welcome_bill()
            
    
          
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n rice \t{self.soap.get()}\t{self.c_s_p}")

            if self.soap1.get()!=0:
                self.txtarea.insert(END,f"\n sugar \t{self.soap1.get()}\t{self.c_s1_p}")

            if self.soap2.get()!=0:
                self.txtarea.insert(END,f"\n food oil \t{self.soap2.get()}\t{self.c_s2_p}")

            if self.dom1.get()!=0:
                self.txtarea.insert(END,f"\n Diary \t{self.dom1.get()}\t{self.d_m1}")

            if self.dom2.get()!=0:
                self.txtarea.insert(END,f"\n Egges\t{self.dom2.get()}\t{self.d_m2}")

            if self.dom3.get()!=0:
                self.txtarea.insert(END,f"\n Breads\t{self.dom3.get()}\t{self.d_m3}")

            if self.dom4.get()!=0:
                self.txtarea.insert(END,f"\n Chocos\t{self.dom4.get()}\t{self.d_m4}")
                
            if self.dom5.get()!=0:
                self.txtarea.insert(END,f"\n 5 star\t{self.dom5.get()}\t{self.d_m5}")
                
            if self.dom6.get()!=0:
                self.txtarea.insert(END,f"\n Magi \t{self.dom5.get()}\t{self.d_m6}")




            self.txtarea.insert(END,f"\n---------------------")
            self.txtarea.insert(END,f"\n GRAND TOTAL :\t{self.total_cosmatic_price}")
            self.txtarea.insert(END,f"\n---------------------")
            self.g()
            
            
 
         # thia is bill printings

    def g(self):
            
                op=messagebox.askyesno("save bill","do you save the bill")
                if op>0:
                    self.bill_date=self.txtarea.get('1.0',END)
                    f1=open("F:\S\sft/"+str(self.cname_bill.get())+".txt","w")
                    f1.write(self.bill_date)
                    f1.close()
                    
                else:
                    return
    def clear_data(self):
        op=messagebox.askyesno(" clear","Do you want to clear data ?")
        if op>0:
            
            
            
        
            self.soap.set(0)
            self.soap1.set(0)
            self.soap2.set(0)

            #kinds items
            self.dom1.set(0)
            self.dom2.set(0)
            self.dom3.set(0)
            self.dom4.set(0)
            self.dom5.set(0)
            self.dom6.set(0)


            # customer details
            self.cname_lab1.set("")
            self.cname_con_no.set("")
                  
            
            
            

            # billing

            self.cosmatic_price.set("")
            self.txtarea.delete("1.0","end")
    def exit(self):
        op=messagebox.askyesno("Exit", "Do you want to exite")
        if op>0:
            self.root.destroy()
        
    
        

    
           
                
               
root = Tk()
obj=b(root)
root.mainloop()
