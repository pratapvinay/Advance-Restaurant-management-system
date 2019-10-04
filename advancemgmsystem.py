from tkinter import*
root = Tk()
root.title("Restaurant Management System")
root.geometry("1350x750")
root.configure(bg= "powder blue")
Title_frame = Frame(root,bd=20,bg="powder blue",relief= RIDGE,pady=5)
Title_frame.pack(side=TOP)
Title = Label(Title_frame ,text = "Restaurant Management System",font=("aerial",62,"bold"),bd=21,justify=CENTER,relief=RIDGE)
Title.pack()

Menu_frame =  Frame(root,bd=20,bg="powder blue",relief= RIDGE,pady=5)
Menu_frame.pack(side=LEFT)

DrinkCakes_f =  Frame(Menu_frame,bd=20,bg="powder blue")
DrinkCakes_f.pack(side=TOP)

Drinks_frame= Frame(DrinkCakes_f,bd=20,bg="powder blue",relief= RIDGE,pady=5)
Drinks_frame.pack(side=LEFT)

#variable
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()

Dateoforder = StringVar()
Cost_Of_Drinks = StringVar()
Cost_Of_Cakes = StringVar()
Service_Charge = StringVar()
Paid_Tax = StringVar()
Sub_Total = StringVar()
Total_Cost = StringVar()
Receipt_Ref = StringVar()


text_input=StringVar()
operator=""

E_cold_Drink = StringVar()
E_Coffee = StringVar()
E_Ice_tea = StringVar()
E_Leamon_tea = StringVar()
E_Cold_coffee = StringVar()
E_Nimmbu_pani = StringVar()


E_Butter_scotch_cake = StringVar()
E_Choclate_cake = StringVar()
E_Pineapple_cake = StringVar()
E_Blackforest_cake = StringVar() 
E_Strwaberry_Cake = StringVar()
E_Redvelvet_cake = StringVar()

E_cold_Drink.set("0")
E_Coffee.set("0")
E_Ice_tea.set("0")
E_Leamon_tea.set("0")
E_Cold_coffee.set("0")
E_Nimmbu_pani.set("0")

E_Butter_scotch_cake.set("0")
E_Choclate_cake.set("0")
E_Pineapple_cake.set("0")
E_Blackforest_cake.set("0")
E_Strwaberry_Cake.set("0")
E_Redvelvet_cake.set("0")

#Dateoforder.set(time.strftime("%d/%m/%Y"))

#DRINKS CHECKBOX
cold_Drink = Checkbutton(Drinks_frame,text="Cold Drink",font=("aerial",10,"bold"),variable=var1,onvalue=1,offvalue=0,bg="powder blue",command=chckcoldDrink)
cold_Drink.grid(row=0,column=0,sticky=W)
Coffee = Checkbutton(Drinks_frame,text="Coffee",font=("aerial",10,"bold"),variable=var2,onvalue=1,offvalue=0,bg="powder blue",command=chckCoffee)
Coffee.grid(row=1,column=0,sticky=W)
Ice_tea = Checkbutton(Drinks_frame,text="Ice_tea",font=("aerial",10,"bold"),variable=var3,onvalue=1,offvalue=0,bg="powder blue",command=chckIcetea)
Ice_tea.grid(row=2,column=0,sticky=W)
Leamon_tea = Checkbutton(Drinks_frame,text="Leamon_tea",font=("aerial",10,"bold"),variable=var4,onvalue=1,offvalue=0,bg="powder blue",command=chckLeamontea)
Leamon_tea.grid(row=3,column=0,sticky=W)
Cold_coffee = Checkbutton(Drinks_frame,text="Cold_coffee",font=("aerial",10,"bold"),variable=var5,onvalue=1,offvalue=0,bg="powder blue",command=chckColdcoffee)
Cold_coffee.grid(row=4,column=0,sticky=W)
Nimmbu_pani = Checkbutton(Drinks_frame,text="Nimmbu_pani",font=("aerial",10,"bold"),variable=var6,onvalue=1,offvalue=0,bg="powder blue",command=chckNimmbupani)
Nimmbu_pani.grid(row=5,column=0,sticky=W)

#DRINKS ENTRY
cold_Drinktext = Entry(Drinks_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_cold_Drink)
cold_Drinktext.grid(row=0,column=1)
Coffeetext = Entry(Drinks_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Coffee)
Coffeetext.grid(row=1,column=1)
Ice_teatext = Entry(Drinks_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Ice_tea)
Ice_teatext.grid(row=2,column=1)
Leamon_teatext = Entry(Drinks_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED, textvariable=E_Leamon_tea)
Leamon_teatext.grid(row=3,column=1)
Cold_coffeetext = Entry(Drinks_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Cold_coffee)
Cold_coffeetext.grid(row=4,column=1)
Nimmbu_panitext = Entry(Drinks_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Nimmbu_pani)
Nimmbu_panitext.grid(row=5,column=1)


Cakes_frame = Frame(DrinkCakes_f,bd=20,bg="powder blue",relief= RIDGE,pady=5)
Cakes_frame.pack(side=RIGHT)

#CAKES CHECKBOX
Butter_scotch_cake = Checkbutton(Cakes_frame,text="Butterscotch_cake",font=("aerial",10,"bold"),variable=var7,onvalue=1,offvalue=0,bg="powder blue",command=chckButter_scotch_cake)
Butter_scotch_cake.grid(row=0,column=0,sticky=W)
Choclate_cake = Checkbutton(Cakes_frame,text="Choclate_cake ",font=("aerial",10,"bold"),variable=var8,onvalue=1,offvalue=0,bg="powder blue",command=chckChoclate_cake)
Choclate_cake.grid(row=1,column=0,sticky=W)
Pineapple_cake = Checkbutton(Cakes_frame,text="Pineapple_cake",font=("aerial",10,"bold"),variable=var9,onvalue=1,offvalue=0,bg="powder blue",command=chckPineapple_cake)
Pineapple_cake.grid(row=2,column=0,sticky=W) 
Blackforest_cake = Checkbutton(Cakes_frame,text="Blackforest_cake",font=("aerial",10,"bold"),variable=var10,onvalue=1,offvalue=0,bg="powder blue",command=chckBlackforest_cake)
Blackforest_cake.grid(row=3,column=0,sticky=W)
Strwaberry_Cake = Checkbutton(Cakes_frame,text="Strwaberry_cake ",font=("aerial",10,"bold"),variable=var11,onvalue=1,offvalue=0,bg="powder blue",command=chckStrwaberry_Cake)
Strwaberry_Cake.grid(row=4,column=0,sticky=W)
Redvelvet_cake = Checkbutton(Cakes_frame,text="Redvelvet_cake",font=("aerial",10,"bold"),variable=var12,onvalue=1,offvalue=0,bg="powder blue",command=chckRedvelvet_cake)
Redvelvet_cake.grid(row=5,column=0,sticky=W)


#CAKES ENTERY
Butter_scotch_caketext = Entry(Cakes_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Butter_scotch_cake)
Butter_scotch_caketext.grid(row=0,column=1)
Choclate_caketext   =  Entry(Cakes_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Choclate_cake)
Choclate_caketext.grid(row=1,column=1)
Pineapple_caketext  = Entry(Cakes_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Pineapple_cake)
Pineapple_caketext.grid(row=2,column=1)
Blackforest_caketext = Entry(Cakes_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Blackforest_cake)
Blackforest_caketext.grid(row=3,column=1)
Strwaberry_Caketext  = Entry(Cakes_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Strwaberry_Cake)
Strwaberry_Caketext.grid(row=4,column=1)
Redvelvet_caketext   = Entry(Cakes_frame,bd=8,width=6,font=("aerial",16,"bold"),justify="left",state = DISABLED,textvariable=E_Redvelvet_cake)
Redvelvet_caketext.grid(row=5,column=1)
#RECEIPT FRAME
Receipet_frame = Frame(root,bd=10,bg="powder blue",relief=RIDGE)
Receipet_frame.pack(side=RIGHT)

#BUTTON FRAME
Buttonframe =  Frame(Receipet_frame,bd=3,bg="powder blue",relief=RIDGE)
Buttonframe.pack(side=BOTTOM)


def Exit():
    Exit = messagebox.askyesno("Exit","Confirm")
    if Exit > 0:
        root.destroy()
        return
    
def Reset():
    
    Dateoforder.set("")
    Cost_Of_Drinks.set("")
    Cost_Of_Cakes.set("")
    Service_Charge.set("")
    Paid_Tax.set("")
    Sub_Total.set("")
    Total_Cost.set("")
    Textfield.delete("1.0",END)
    
    E_cold_Drink.set("0")
    E_Coffee.set("0")
    E_Ice_tea.set("0")
    E_Leamon_tea.set("0")
    E_Cold_coffee.set("0")
    E_Nimmbu_pani.set("0")
    
    E_Butter_scotch_cake.set("0")
    E_Choclate_cake.set("0")
    E_Pineapple_cake.set("0")
    E_Blackforest_cake.set("0")
    E_Strwaberry_Cake.set("0")
    E_Redvelvet_cake.set("0")
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    
    
    
    cold_Drinktext.configure(state=DISABLED)
    Coffeetext.configure(state=DISABLED) 
    Ice_teatext.configure(state=DISABLED)
    Leamon_teatext.configure(state=DISABLED)
    Cold_coffeetext.configure(state=DISABLED)
    Nimmbu_panitext.configure(state=DISABLED)
    
    
    Butter_scotch_caketext.configure(state=DISABLED)
    Choclate_caketext.configure(state=DISABLED)
    Pineapple_caketext.configure(state=DISABLED)
    Redvelvet_caketext.configure(state=DISABLED)
    Blackforest_caketext.configure(state=DISABLED)
    Strwaberry_Caketext.configure(state=DISABLED)
    Redvelvet_caketext.configure(state=DISABLED)

def Costofitem():
    item1 = float(E_cold_Drink.get())
    item2= float(E_Coffee.get())
    item3 = float( E_Ice_tea.get())
    item4 = float(E_Leamon_tea.get())
    item5 = float( E_Cold_coffee.get())
    item6 = float(E_Nimmbu_pani.get())
        
    item7 = float(E_Butter_scotch_cake.get())
    item8 = float(E_Choclate_cake.get())
    item9 = float(E_Pineapple_cake.get())
    item10 = float(E_Redvelvet_cake.get())
    item11= float(E_Strwaberry_Cake.get())
    item12 = float(E_Blackforest_cake.get()) 
    
    PriceofDrinks = (item1*50)+(item2*30)+(item3*30)+(item4*30)+(item5*50)+(item6*30) 
    
    PriceofCakes = (item7*200)+(item8*250)+(item9*250)+(item10*300)+(item11*250)+(item12*300)
    
    pricedrinks = "Rs",str("%.2f"%(PriceofDrinks))
    pricecakes = "Rs",str("%.2f"%(PriceofCakes))
    
    Cost_Of_Drinks.set( pricedrinks)
    Cost_Of_Cakes.set(pricecakes)
    
    Servicecharge = "Rs",str("%.2f"%(50))
    Service_Charge.set(Servicecharge)
    
    subtotal = "Rs",str("%.2f"%(PriceofDrinks+PriceofCakes+50))
    Sub_Total.set(subtotal)
    
    Taxpaid  = "Rs",str("%.2f"%((PriceofDrinks+PriceofCakes+50)+100))    
    Paid_Tax.set(Taxpaid)
    
    Totalco = "Rs",str("%.2f"%((PriceofDrinks+PriceofCakes+50)+100))
    Total_Cost.set(Totalco)


def chckcoldDrink():
    if(var1.get()==1):
        cold_Drinktext.configure(state=NORMAL)
        cold_Drinktext.focus()
        cold_Drinktext.delete("0",END)
        E_cold_Drink.set("")
    elif (var1.get()==0):
        cold_Drinktext.configure(state=DISABLED)
        E_cold_Drink.set("0")

def chckCoffee():
    if (var2.get()==1):
        Coffeetext.configure(state=NORMAL)
        Coffeetext.focus()
        Coffeetext.delete("0",END)
        E_Coffee.set("")
    elif  (var2.get()==0):
        Coffeetext.configure(state=DISABLED)
        E_Coffee.set("0")

def chckIcetea():
    if (var3.get()==1):
        Ice_teatext.configure(state=NORMAL)
        Ice_teatext.focus()
        Ice_teatext.delete("0",END)
        E_Ice_tea.set("")
    elif  (var3.get()==0):
        Ice_teatext.configure(state=DISABLED)
        E_Ice_tea.set("0")

def chckLeamontea():
    if (var4.get()==1):
       Leamon_teatext.configure(state=NORMAL)
       Leamon_teatext.focus()
       Leamon_teatext.delete("0",END)
       E_Leamon_tea.set("")
    elif  (var4.get()==0):
        Leamon_teatext.configure(state=DISABLED)
        E_Leamon_tea.set("0")
    
def chckColdcoffee():
    if (var5.get()==1):
        Cold_coffeetext.configure(state=NORMAL)
        Cold_coffeetext.focus()
        Cold_coffeetext.delete("0",END)
        E_Cold_coffee.set("")
    elif  (var5.get()==0):
        Cold_coffeetext.configure(state=DISABLED)
        E_Cold_coffee.set("0")
        

def chckNimmbupani():
    if (var6.get()==1):
        Nimmbu_panitext.configure(state=NORMAL)
        Nimmbu_panitext.focus()
        Nimmbu_panitext.delete("0",END)
        E_Nimmbu_pani.set("")
    elif  (var6.get()==0):
        Nimmbu_panitext.configure(state=DISABLED)
        E_Nimmbu_pani.set("0")
    

def chckButter_scotch_cake():
    if (var7.get()==1):
        Butter_scotch_caketext.configure(state=NORMAL)
        Butter_scotch_caketext.focus()
        Butter_scotch_caketext.delete("0",END)
        E_Butter_scotch_cake.set("")
    elif  (var7.get()==0):
        Butter_scotch_caketext.configure(state=DISABLED)
        E_Butter_scotch_cake.set("0")


def chckChoclate_cake():
    if (var8.get()==1):
        Choclate_caketext.configure(state=NORMAL)
        Choclate_caketext.focus()
        Choclate_caketext.delete("0",END)
        E_Choclate_cake.set("")
    elif  (var8.get()==0):
        Choclate_caketext.configure(state=DISABLED)
        E_Choclate_cake.set("0")
        

def chckPineapple_cake():
    if (var9.get()==1):
        Pineapple_caketext.configure(state=NORMAL)
        Pineapple_caketext.focus()
        Pineapple_caketext.delete("0",END)
        E_Pineapple_cake.set("")
    elif  (var9.get()==0):
        Pineapple_caketext.configure(state=DISABLED)
        E_Pineapple_cake.set("0")
        

def chckBlackforest_cake():
    if (var10.get()==1):
        Blackforest_caketext.configure(state=NORMAL)
        Blackforest_caketext.focus()
        Blackforest_caketext.delete("0",END)
        E_Blackforest_cake.set("")
    elif  (var10.get()==0):
        Blackforest_caketext.configure(state=DISABLED)
        E_Blackforest_cake.set("0")
        
        
def chckStrwaberry_Cake():
    if (var11.get()==1):
        Strwaberry_Caketext.configure(state=NORMAL)
        Strwaberry_Caketext.focus()
        Strwaberry_Caketext.delete("0",END)
        E_Strwaberry_Cake.set("")
    elif  (var11.get()==0):
        Strwaberry_Caketext.configure(state=DISABLED)
        E_Strwaberry_Cake.set("0")
        
def chckRedvelvet_cake():
    if (var12.get()==1):
        Redvelvet_caketext.configure(state=NORMAL)
        Redvelvet_caketext.focus()
        Redvelvet_caketext.delete("0",END)
        E_Redvelvet_cake.set("")
    elif  (var12.get()==0):
        Redvelvet_caketext.configure(state=DISABLED)
        E_Redvelvet_cake.set("0")
        
import random
def Receiptdata():
    Textfield.delete("1.0",END)
    x = random.randint(10903,609235)
    randomref=str(x)
    Receipt_Ref.set("BILL"+ randomref)
    Textfield.insert(END,'Receipt Ref : \t\t\t' + Receipt_Ref.get() +'\t')
    Textfield.insert(END,'Items : \t\t\t' + "Cost of items \n")
    Textfield.insert(END,'Cold drink : \t\t\t' + E_cold_Drink.get() +'\n')
    Textfield.insert(END,'coffee : \t\t\t' + E_Coffee.get() +'\n')
    Textfield.insert(END,'E_Ice_tea : \t\t\t' + E_Ice_tea.get() +'\n')
    Textfield.insert(END,'E_Leamon_tea  : \t\t\t' + E_Leamon_tea.get() +'\n')
    Textfield.insert(END,'E_Cold_coffee  : \t\t\t' + E_Cold_coffee.get() +'\n')
    Textfield.insert(END,'E_Nimmbu_pani  : \t\t\t' + E_Nimmbu_pani.get() +'\n')
    Textfield.insert(END,'E_Butter_scotch_cake  : \t\t\t' + E_Butter_scotch_cake.get() +'\n')
    Textfield.insert(END,'E_Choclate_cake  : \t\t\t' + E_Choclate_cake.get() +'\n')
    Textfield.insert(END,'E_Pineapple_cake  : \t\t\t' + E_Pineapple_cake.get() +'\n')
    Textfield.insert(END,'E_Blackforest_cake  : \t\t\t' + E_Blackforest_cake.get() +'\n')
    Textfield.insert(END,'E_Redvelvet_cake : \t\t\t' + E_Redvelvet_cake.get() +'\n')
    Textfield.insert(END,'Cost_Of_Drinks  : \t\t\t' + Cost_Of_Drinks.get() +'\n')
    Textfield.insert(END,'Cost_Of_Cakes  : \t\t\t' + Cost_Of_Cakes.get() +'\n')
    Textfield.insert(END,'Service_Charge  : \t\t\t' + Service_Charge.get() +'\n')
    Textfield.insert(END,'Sub_Total  : \t\t\t' + str(Sub_Total.get()) +'\n')
    Textfield.insert(END,'Paid_Tax Ref : \t\t\t' + Paid_Tax.get() +'\n')
    Textfield.insert(END,'Total_Cost Ref : \t\t\t' + str(Total_Cost.get()) +'\n')
        


        
        
        
    
    
    
    
#BUTTONS
Totalbutton = Button(Buttonframe,text ="Total",font=("aerial",16,"bold"),bg="powder blue",bd=7,padx=16,pady=1,command=Costofitem).grid(row=0,column=0)
Receiptbutton= Button(Buttonframe,text ="Receipt",font=("aerial",16,"bold"),bg="powder blue",bd=7,padx=16,pady=1,command=Receiptdata).grid(row=0,column=1)
Exitbutton = Button(Buttonframe,text ="Exit",font=("aerial",16,"bold"),bg="powder blue",bd=7,padx=16,pady=1,command=Exit).grid(row=0,column=2)
Resetbutton = Button(Buttonframe,text ="Reset",font=("aerial",16,"bold"),bg="powder blue",bd=7,padx=16,pady=1,command=Reset)
Resetbutton.grid(row=0,column=3)




#CAL funciton
def bclick(button):
    global operator
    operator = operator + str(button)
    text_input.set(operator)
    
def clear():
    operator=""
    text_input.set(operator)

def equal():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""
    


#CALCULATOR FRAME
cal_frame =  Frame(Receipet_frame,bd=6,bg="powder blue",relief=RIDGE)
cal_frame.pack(side=TOP)

#CALCULATOR ENTRY
Display = Entry(cal_frame,bg="white",width=45,bd=4,textvariable=text_input,font=("aerial",12,"bold"),justify=RIGHT).grid(row=0,column=0,columnspan=4,pady=1)


#CALCULATOR BUTTON
button9 = Button(cal_frame,text ="9",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(9)).grid(row=1,column=0)
button8 = Button(cal_frame,text ="8",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(8)).grid(row=1,column=1)
button7 = Button(cal_frame,text ="7",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(7)).grid(row=1,column=2)
buttonAdd = Button(cal_frame,text ="+",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick("+")).grid(row=1,column=3)

button6 = Button(cal_frame,text ="6",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(6)).grid(row=2,column=0)
button5 = Button(cal_frame,text ="5",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(5)).grid(row=2,column=1)
button4 = Button(cal_frame,text ="4",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(4)).grid(row=2,column=2)
buttonSub = Button(cal_frame,text ="-",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick("-")).grid(row=2,column=3)

button3 = Button(cal_frame,text ="3",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(3)).grid(row=3,column=0)
button2 = Button(cal_frame,text ="2",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(2)).grid(row=3,column=1)
button1 = Button(cal_frame,text ="1",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(1)).grid(row=3,column=2)
buttonDiv = Button(cal_frame,text ="/",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick("/")).grid(row=3,column=3)

button0 = Button(cal_frame,text ="0",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick(0)).grid(row=4,column=0)
buttonClear = Button(cal_frame,text ="C",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=clear).grid(row=4,column=1)
buttonEqual = Button(cal_frame,text ="=",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=equal).grid(row=4,column=2)
buttonMul = Button(cal_frame,text ="*",bg="powder blue",bd=7,font=("aerial",16,"bold"),padx=30,pady=2,command=lambda:bclick("*")).grid(row=4,column=3)

#TEXT FRAME
Textframe = Frame(Receipet_frame,bd=4,bg="powder blue",relief=RIDGE)
Textframe.pack(side=BOTTOM)

Textfield =Text(Textframe,font=("aerial",12,"bold"),height=8,width=46,relief=RIDGE,bd=4)
Textfield.grid(row=0,column=0)

#COST FRAME

cost_frame = Frame(Menu_frame,bd=4,bg="powder blue")
cost_frame.pack(side=LEFT)
labelCost_Of_Drinks = Label(cost_frame,text="Cost_Of_Drinks",bg="powder blue",fg="black",font=("aerial",10,"bold"))
labelCost_Of_Drinks.grid(row=0,column=0)
labelCost_Of_Cakes = Label(cost_frame,text="Cost_Of_Cakes",bg="powder blue",fg="black",font=("aerial",10,"bold"))
labelCost_Of_Cakes.grid(row=1,column=0)
labelService_Charge = Label(cost_frame,text="Service_Charge",bg="powder blue",fg="black",font=("aerial",10,"bold"))
labelService_Charge.grid(row=2,column=0)
 

#Entry Frame
Cost_Of_Drinks_Entry = Entry(cost_frame,font=("aerial",15,"bold"),width=15,bg ="white",justify=RIGHT,textvariable=Cost_Of_Drinks)
Cost_Of_Drinks_Entry.grid(row=0,column=1)
Cost_Of_Cakes_Entry = Entry(cost_frame,font=("aerial",15,"bold"),width=15,bg ="white",justify=RIGHT,textvariable=Cost_Of_Cakes)
Cost_Of_Cakes_Entry.grid(row=1,column=1)
Service_charge_Entry = Entry(cost_frame,font=("aerial",15,"bold"),width=15,bg ="white",justify=RIGHT,textvariable=Service_Charge)
Service_charge_Entry.grid(row=2,column=1)


#PAID TAX SUB TOTAL TOTAL COAST FRAME

PST_F = Frame(Menu_frame,bd=4,bg="powder blue")
PST_F.pack(side=RIGHT)
labelPaid_Tax = Label(PST_F,text="Paid_Tax",bg="powder blue",fg="black",font=("aerial",10,"bold"))
labelPaid_Tax.grid(row=0,column=0)
labelSub_Total = Label(PST_F,text="Sub_Total",bg="powder blue",fg="black",font=("aerial",10,"bold"))
labelSub_Total.grid(row=1,column=0)
labelTotal_Cost = Label(PST_F,text="Total_Cost",bg="powder blue",fg="black",font=("aerial",10,"bold"))
labelTotal_Cost.grid(row=2,column=0)

#ENTRY

Paid_Tax_Entry = Entry(PST_F,font=("aerial",15,"bold"),width=15,bg ="white",justify=RIGHT,textvariable=Paid_Tax)
Paid_Tax_Entry.grid(row=0,column=1)
Sub_Total_Entry = Entry(PST_F,font=("aerial",15,"bold"),width=15,bg ="white",justify=RIGHT,textvariable =Sub_Total)
Sub_Total_Entry.grid(row=1,column=1)
Total_Cost_Entry = Entry(PST_F,font=("aerial",15,"bold"),width=15,bg ="white",justify=RIGHT,textvariable =Total_Cost)
Total_Cost_Entry.grid(row=2,column=1)

root.mainloop()