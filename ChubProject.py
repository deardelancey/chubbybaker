import sqlite3                                
conn = sqlite3.connect(r"C:\Users\pitch\Videos\Captures\projectchubby\sqldatachub.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS bill (

        id_bill INTEGER PRIMARY KEY NOT NULL,       
        order_total CHAR(20) NOT NULL,
        price INTEGER NOT NULL,
        date varchar(50) NOT NULL,
        month varchar(50) NOT NULL
               

    )
    ''')


c.execute('''CREATE TABLE IF NOT EXISTS myOrder (
        
        id_order INTEGER PRIMARY KEY NOT NULL,
        name CHAR(20) NOT NULL,
        Price INTEGER NOT NULL,
        picture BLOB NOT NULL
        
        
    )
    ''')

    
c.execute('''CREATE TABLE IF NOT EXISTS member (
    
        id_member INTEGER PRIMARY KEY NOT NULL,
        username CHAR(20) NOT NULL,
        Tel CHAR(10) NOT NULL,
        date varchar(50) NOT NULL
               
        
    )
    ''')


c.execute('''CREATE TABLE IF NOT EXISTS stock (
    
        id_stock INTEGER PRIMARY KEY NOT NULL,
        name CHAR(20) NOT NULL,
        price INTEGER ,
        picture BLOB NOT NULL
              
    )
    ''')


conn.commit()


from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import time 
from tkinter import messagebox, Listbox ,StringVar,font
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import Toplevel, Label, Entry, Button, filedialog
import tkinter.font as tkFont
import sqlite3
from tkinter import filedialog
import io
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import simpledialog

donuts_basket = []
total_price = 0
total = 0                               
image_tk = None 
receipt_window = None 
order_items = []


def checkint(P):
    if P.isdigit() or P == "":
        return True
    
    else:
        return False 
    
z=[]


############### หน้าแรกของโปรแกรม ###############

root = Tk()
root.title("CHUBBY BAKER")
root.geometry("1200x675+180+50")
root.resizable(False, False)
imggg = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\home2home.png")
root_imggg = ImageTk.PhotoImage(imggg)
Label(root,image=root_imggg).place(x=0)

def show():
    products_listbox.delete(0, tk.END)
    c.execute('''SELECT * FROM stock''')
    conn.commit()
    result = c.fetchall()
    i = 1
    z.clear()

    for x in result:
            products_listbox.insert(x[0]," Product No:  {}    {}    price:  {}    quantity: {} ".format(i,x[1],x[2],x[4]))
            z.append(x[0])
            i+=1 

def quit():
     root.destroy()

def backmainregis():
     regisbg.withdraw()
     root.deiconify()

def backmainlogin():
    loginbg.withdraw()
    root.deiconify()

def backmainstaff():
     staffbg.withdraw()
     root.deiconify()

def backmaindeveloper():
     delveloperbg.withdraw()
     root.deiconify()



def select_update(event):
    name_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)
    quantity_entry.delete(0, tk.END)
    update_listbox =[]  
    product_idd = products_listbox.curselection()  

    for index in product_idd:
        if index <0 or index >=len(z):
            messagebox.showerror(title=None,message=f"Invalid index: {index}")
            return
        
        stock_id = z[index]
        c.execute('SELECT name, price,quantity FROM stock WHERE id_stock = ?',(stock_id,))
        conn.commit()
        results = c.fetchone()

        for i in results:
            update_listbox.append(i)

        name_entry.insert(0,update_listbox[0])
        price_entry.insert(0,update_listbox[1])
        quantity_entry.insert(0,update_listbox[2])


def edit():
    product_idd = products_listbox.curselection()  

    for index in product_idd:
        if index <0 or index >=len(z):
            messagebox.showerror(title=None,message=f"Invalid index: {index}")
            return
        
        stock_id = z[index]
        name = name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        askimage = messagebox.askyesno("รูปภาพ","ต้องการเปลี่ยนรูปภาพไหม")

        if askimage == True:
            file_pic = filedialog.askopenfilename()

            if file_pic:
                with open(file_pic, 'rb') as file:
                    picture = file.read() 
            c.execute('''UPDATE stock SET name =?,price =?,picture=?,quantity=? WHERE id_stock =? ''',(name, price, picture,quantity, stock_id,))
            conn.commit()

        elif askimage == False :
            c.execute('''UPDATE stock SET name =?,price =?,quantity=? WHERE id_stock =? ''',(name, price,quantity, stock_id,))
            conn.commit()
        

        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        show()


def delete():
    product_idd = products_listbox.curselection()  

    for index in product_idd:
        if index <0 or index >=len(z):
            messagebox.showerror(title=None,message=f"Invalid index: {index}")
            return
        
        stock_id = z[index]
        c.execute("DELETE FROM stock WHERE id_stock=?", (stock_id,))
        conn.commit()
        show() 


def add():
    name = name_entry.get()
    price =price_entry.get()
    quantity = quantity_entry.get()
        
    if name and price:
        file_ = filedialog.askopenfilename()

        if file_:
            with open(file_, 'rb')as file:
                picture = file.read()

            if name and price  and picture:
                c.execute("INSERT INTO stock (name, price,picture,quantity) VALUES (?, ?, ?,?)", (name, price, picture,quantity))        
                conn.commit()
                name_entry.delete(0, tk.END) 
                price_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
                show()

    else:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูล")



############### developer ###############

def developer():
    global delveloperbg,photo  
    root.withdraw()
    delveloperbg = tk.Toplevel(root)
    delveloperbg.title("DELELOPER")
    delveloperbg.geometry("1200x675+180+50")  
    delveloperbg.resizable(False, False)
    img=Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\developerbg.png")
    photo =ImageTk.PhotoImage(img)
    lbl = Label(delveloperbg, image=photo)
    lbl.pack()

    Button(delveloperbg ,text="back", font=("Arial", 16), command=backmaindeveloper, bg='#DC416D', fg='#FFFFFF', bd=0).place(x=50, y=30, width=80, height=40)



############### staff ###############

def staff1():     
    global staffbg,photo
    root.withdraw()
    staffbg = tk.Toplevel(root)
    staffbg.title("FOR STAFF")
    staffbg.geometry("1200x675+180+50")  
    staffbg.resizable(False, False)
    img2=Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\staffbg.png")
    photo =ImageTk.PhotoImage(img2)
    lbl = Label(staffbg, image=photo)
    lbl.pack()


    def check_login():
        username = staff_usentry.get()
        password = staff_pasentry.get()

        if username==""and password =="" :
            messagebox.showerror("ข้อผิดพลาด","กรุณากรอกชื่อผู้ใช้และรหัสผ่าน")

        elif username == "":
            messagebox.showerror("ข้อผิดพลาด","กรุณากรอกชื่อผู้ใช้")

        elif password == "":
            messagebox.showerror("ข้อผิดพลาด","กรุณากรอกรหัสผ่าน")

        elif  password != "306" :
            messagebox.showerror("ข้อผิดพลาด","รหัสผ่านไม่ถูกต้อง")

        elif password == "306":   
             staffbg.withdraw()
             staffhome1()  
        
     
    staff_username = tk.StringVar()  
    staff_usentry = tk.Entry(staffbg, textvariable=staff_username,font=("Arial", 20),fg='#DC416D',bg="#F4F3BD",bd=0,width=14,) #Entryboxเป็นช่องให้พิมพ์ username
    staff_usentry.place(x=858,y=190)

    staff_password = tk.IntVar()
    staff_password.set("")
    staff_pasentry=tk.Entry(staffbg,textvariable=staff_password,font=("Arial", 20),fg='#DC416D',bg="#F4F3BD",bd=0,width=14,) #Entryboxเป็นช่องให้พิมพ์ password
    staff_pasentry.place(x=859,y=363)
    

    Button(staffbg, image=bttn_back, command=backmainstaff,bg='#DC416D',bd=0).place(x=31,y=15)
    Button(staffbg, image=bttn_done, command=check_login,bg='#DC416D',bd=0).place(x=890,y=525,width=145,height=46)


def staffhome1():
    global staffhomebg,photo
    staffbg.withdraw()
    staffhomebg = Toplevel(staffbg)
    staffhomebg.title("STAFF HOME")
    staffhomebg.geometry("1200x675+180+50")
    staffhomebg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\staffhome.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(staffhomebg, image=photo)
    lbl.pack()
   

    def staff_editcustomer():
        global staff_editcusbg,photo
        staffhomebg.withdraw()
        staff_editcusbg = Toplevel(staffhomebg)
        staff_editcusbg.title("EDIT CUSTOMER")
        staff_editcusbg.geometry("1200x675+180+50")
        staff_editcusbg.resizable(False, False)
        img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\editcus.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(staff_editcusbg, image=photo)
        lbl.pack()
        zaza=[]

        def show_member():
            custumer_listbox.delete(0, tk.END)
            c.execute('''SELECT * FROM member''')
            conn.commit()
            result = c.fetchall()
            i = 1
            zaza.clear()

            for x in result:
                    custumer_listbox.insert(x[0],f"\n {i}    uesrname: {x[1].ljust(20)}        \t\t\t tel: {x[2]} ")
                    zaza.append(x[0])
                    i+=1 

        def delete_member():
            member_idd = custumer_listbox.curselection()  

            for index in member_idd:
                if index <0 or index >=len(zaza):
                    messagebox.showerror(title=None,message=f"Invalid index: {index}")
                    return
                
                member_id = zaza[index]
                c.execute("DELETE FROM member WHERE id_member=?", (member_id,))
                conn.commit()
                show_member() 


        custumer_listbox = tk.Listbox(staff_editcusbg, bg="#ffffff", borderwidth=0, font=("Times", 14), fg="#333333", relief="sunken")
        custumer_listbox.place(x=640, y=110, width=420, height=400)
    
        def staff_backmenubg ():
            staffhome1()
            staff_editcusbg.withdraw()
        

        show_member()
        Button(staff_editcusbg ,image=bttn_back,command=staff_backmenubg,bg='#DC416D',bd=0).place(x=53,y=27,width=145,height=46)  
        Button(staff_editcusbg ,image=bttn_delete,command=delete_member,bg='#DC416D',bd=0).place(x=640,y=525,width=145,height=46)                   
        Button(staff_editcusbg ,image=bttn_done, command=staff_backmenubg,bg='#DC416D',bd=0).place(x=905,y=525,width=145,height=46)


    
    def staff_history():
        global staff_historybg,photo
        staffhomebg.withdraw()
        staff_historybg = Toplevel(staffhomebg)
        staff_historybg.title("HISTORY SALES")
        staff_historybg.geometry("1200x675+180+50")
        staff_historybg.resizable(False, False)
        img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\historybill.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(staff_historybg, image=photo)
        lbl.pack()


        def history_bill_staff():
            staff_history_listbox.delete(0,tk.END)
            c.execute("SELECT * FROM bill ")
            conn.commit()
            result = c.fetchall()
            i = 1
            z.clear()

            for x in result:
                    staff_history_listbox.insert(x[0],"  {}    date: {}    total price:  {} customer: {} ".format(i,x[3],x[2],x[5]))
                    z.append(x[0])
                    i+=1 

        def staff_backhistorybg ():
            staffhome1()
            staff_historybg.withdraw()


        staff_history_listbox = tk.Listbox(staff_historybg, bg="#ffffff", font=("Times", 14), fg="#333333",relief="flat")
        staff_history_listbox.place(x=335, y=180, width=550, height=420)


        history_bill_staff()
        Button(staff_historybg, image=bttn_back, command=staff_backhistorybg,bg='#DC416D',bd=0).place(x=62,y=590,width=145,height=46)
        Button(staff_historybg, image=bttn_done, command=staff_backhistorybg,bg='#DC416D',bd=0).place(x=993,y=590,width=145,height=46)
    
    
    
    def sales(): # สรุปยอดขาย
        global checksalesbg,photo
        staffhomebg.withdraw()
        checksalesbg = Toplevel(staffhomebg)
        checksalesbg.title("CHECK DAILY/MONTHLY SALES")
        checksalesbg.geometry("1200x675+180+50")
        checksalesbg.resizable(False, False)
        img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\dailymonthly.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(checksalesbg, image=photo)
        lbl.pack()
    
        
        #สร้างตัวแปรเพื่อเก็บวันที่
        selected_date = tk.StringVar()

        #แสดงประวัติคำสั่งซื้อรายวัน
        def show_daily_orders():
            date = selected_date.get() #ดึงวันที่จากตัวแปร selected_date
            #ดึงข้อมูลจากฐานข้อมูลและคำนวณยอดขายรายวัน
            daily_sales = calculate_daily_sales(date)
            daily_sales_label.config(text=f"ยอดขายในวันที่ {date}: {daily_sales} บาท")
            daily_sales_label.place(x=630, y=95)

        #คำนวณยอดขายรายวัน
        def calculate_daily_sales(date):
            c.execute("SELECT SUM(price) FROM bill WHERE date = ?", (date,)) #วิธีกรอก 12/09/2023
            conn.commit()
            result = c.fetchone() #fetchone คือการดึงข้อมูล
            return result[0] if result[0] else 0

        #สร้างตัวแปรเพื่อเก็บรายเดือน
        selected_month = tk.StringVar()

        #แสดงประวัติคำสั่งซื้อรายเดือน
        def show_monthly_orders():
            month = selected_month.get()  #ดึงเดือนจากตัวแปร selected_month
            #ดึงข้อมูลจากฐานข้อมูลและคำนวณยอดขายรายเดือน
            monthly_sales = calculate_monthly_sales(month)
            monthly_sales_label.config(text=f"ยอดขายในเดือน {month}: {monthly_sales} บาท")
            monthly_sales_label.place(x=630, y=220)

        #คำนวณยอดขายรายเดือน
        def calculate_monthly_sales(month):
            c.execute("SELECT SUM(price) FROM bill WHERE month = ?", (month,))  #วิธีกรอก 09/2023
            conn.commit()
            result = c.fetchone() #fetchone คือการดึงข้อมูล
            return result[0] if result[0] else 0 #ถ้าไม่มีข้อมูลจะขึ้น 0


        daily_sales_label = tk.Label( checksalesbg, text="", font=12,bg="#FFFFFF")
        daily_sales_label.place(x=630, y=75)


        date_entry = tk.Entry( checksalesbg, textvariable=selected_date, font=18,justify="center")
        date_entry.place(x=635, y=120,width=200,height=30)
        show_daily_button = tk.Button( checksalesbg, text="แสดงประวัติรายวัน",fg="#ffffff",bg="#DC416D",command=show_daily_orders,font=18)
        show_daily_button.place(x=665, y=155)


        monthly_sales_label = tk.Label( checksalesbg, text="", font=12,bg="#FFFFFF")
        monthly_sales_label.pack()

        
        month_entry = tk.Entry( checksalesbg, textvariable=selected_month, font=18,width=15,justify="center")
        month_entry.place(x=635, y=243,width=200,height=30)
        show_monthly_button = tk.Button( checksalesbg, text="แสดงประวัติรายเดือน",fg="#ffffff",bg="#DC416D", command=show_monthly_orders,font=18)
        show_monthly_button.place(x=660, y=280)


        def backcheckstock ():
            staffhome1()
            checksalesbg.withdraw()


        Button(checksalesbg ,image=bttn_back,command=backcheckstock,bg='#DC416D',bd=0).place(x=53,y=27,width=145,height=46)
        Button(checksalesbg ,image=bttn_done, command=backcheckstock,bg='#DC416D',bd=0).place(x=985,y=565,width=145,height=46)



    def staff_showmenu():
        global staff_menu_page,photo
        addstockbg.withdraw()
        staff_menu_page = Toplevel(addstockbg)  
        staff_menu_page.title("MENU")
        staff_menu_page.geometry("1200x675+180+50")
        staff_menu_page.resizable(False, False)
        img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\menu.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(staff_menu_page, image=photo)
        lbl.pack()

        canvas = tk.Canvas(staff_menu_page, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0, scrollregion=(0, 0, 700, 5000))
        canvas.place(x=180,y=150, width=850, height=470)
        product = tk.Frame(canvas, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0) 
        canvas.create_window((0, 0), window=product, anchor='nw')
        
        def on_mousewheel(event):      
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        staff_menu_page.bind("<MouseWheel>", on_mousewheel) 

        def staff_show_menu():
            c.execute("SELECT id_stock, name, price, picture FROM stock ")
            conn.commit()  
            pictures = c.fetchall() 

            for i, x in enumerate(pictures):   
                image = Image.open(BytesIO(x[3]))
                target_width, target_height = 117, 166  
                image = image.resize((target_width, target_height))  
                image = ImageTk.PhotoImage(image)  

                label = Label(product, image=image, width=117, height=164,highlightthickness=0,bd=0)  
                label.image = image
                label.grid(row=i // 6, column=i % 6, padx=10, pady=10)      

            def done_staffshowmenu():
                    staffhome1()
                    staff_menu_page.withdraw()

            def back_staffshowmenu():
                    addstock()
                    staff_menu_page.withdraw()
            

            Button(staff_menu_page, image=bttn_back, command=back_staffshowmenu,bg='#DC416D',bd=0).place(x=40,y=39,width=145,height=46)
            Button(staff_menu_page ,image=bttn_done, command=done_staffshowmenu,bg='#DC416D',bd=0).place(x=985,y=565,width=145,height=46)
        staff_show_menu()
     

    def addstock():
        global addstockbg,photo
        global products_listbox, name_entry, price_entry, z,quantity_entry
        staffhomebg.withdraw()
        addstockbg = Toplevel(staffhomebg)
        addstockbg.title("ADD DONUTS")
        addstockbg.geometry("1200x675+180+50")
        addstockbg.resizable(False, False)
        img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\addstock.png")
        photo = ImageTk.PhotoImage(img)
        lbl = Label(addstockbg, image=photo)
        lbl.pack()

        def backaddstock():
            staffhome1()
            addstockbg.withdraw()


        name_entry = tk.Entry(addstockbg, bg="#ffffff", borderwidth="1px", font=("Times", 17), fg="#000000", justify="center", relief="sunken")
        name_entry.place(x=800, y=110, width=250, height=35)

        validate_func = addstockbg.register(checkint)
        price_entry=tk.Entry(addstockbg,validate='key',validatecommand=(validate_func, "%P"),bg="#ffffff", borderwidth="1px", font=("Times", 17), fg="#000000", justify="center", relief="sunken")
        price_entry.place(x=800,y=160,width=250,height=35)
 
        quantity_entry = tk.Entry(addstockbg, bg="#ffffff", borderwidth="1px", font=("Times", 17), fg="#000000", justify="center", relief="sunken")
        quantity_entry.place(x=800,y=210,width=250,height=35)

        name_label = tk.Label(addstockbg, bg="#DC416D", font=("Times", 13), fg="#ffffff", justify="center",borderwidth=0, text="ชื่อสินค้า", relief="sunken")
        name_label.place(x=650, y=118, width=140, height=25)

        price_label = tk.Label(addstockbg, bg="#DC416D", font=("Times", 13), fg="#ffffff", justify="center",borderwidth=0, text="ราคาสินค้า", relief="sunken")
        price_label.place(x=650, y=168, width=140, height=25)

        quantity_label = tk.Label(addstockbg, text="จำนวนสินค้า", fg="#FFFFFF",bg= "#DC416D",font=13, justify="center", relief="sunken")
        quantity_label.place(x=650,y=218, width=140, height=25)

        products_listbox = tk.Listbox(addstockbg, bg="#FFFFFF", borderwidth=0, font=("Times", 13), fg="black", relief="sunken")
        products_listbox.place(x=700, y=300, width=420, height=220)
        products_listbox.bind('<Double-Button>',select_update)

        
        show()
        Button(addstockbg ,image=bttn_done, command=staff_showmenu,bg='#DC416D',bd=0).place(x=985,y=565,width=145,height=46)
        Button(addstockbg ,image=bttn_delete,command=delete,bg='#DC416D',bd=0).place(x=650,y=565,width=145,height=46)
        Button(addstockbg ,image=bttn_back,command=backaddstock,bg='#DC416D',bd=0).place(x=53,y=27,width=145,height=46)
        Button(addstockbg ,image=bttn_add,bg='#DC416D',command=add,bd=0).place(x=53,y=580,width=145,height=46)                      #ปุ่มadd
        Button(addstockbg ,image=bttn_edit,bg='#DC416D',command=edit,bd=0).place(x=350,y=580,width=145,height=46)                  #ปุ่มedit

    def backroot():
        staffhomebg.withdraw()
        root.deiconify()


    Button(staffhomebg, image=bttn_back, command=backroot,bg='#DC416D',bd=0).place(x=31,y=38,width=145,height=46)
    Button(staffhomebg, image=bttn_editcus, command=staff_editcustomer,bg='#DC416D',bd=0).place(x=205,y=420)
    Button(staffhomebg, image=bttn_historybill,command=staff_history,bg='#DC416D',bd=0).place(x=215,y=522)
    Button(staffhomebg, image=bttn_seles, command=sales,bg='#ffffff',bd=0).place(x=735,y=398)
    Button(staffhomebg, image=bttn_addstock, command=addstock,bg='#ffffff',bd=0).place(x=732,y=512)

    


############### Login ################

def login():
    global loginbg,photo
    root.withdraw()
    loginbg = Toplevel(root)  
    loginbg.title("LOGIN")
    loginbg.geometry("1200x675+180+50")
    loginbg.resizable(False, False)
    img3 = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\loginbg.png")
    photo = ImageTk.PhotoImage(img3)
    lbl = Label(loginbg, image = photo)
    lbl.pack()

    loginusername = tk.StringVar()  
    login_usentry = tk.Entry(loginbg, textvariable=loginusername,font=("Arial", 20),fg='#DC416D',bg="#F4F3BD",bd=0,width=14,) #Entryboxเป็นช่องให้พิมข้อความ
    login_usentry.place(x=858,y=188)

    login_tel = tk.IntVar()
    login_tel.set("")
    login_telentry=tk.Entry(loginbg,textvariable=login_tel,font=("Arial", 20),fg='#DC416D',bg="#F4F3BD",bd=0,width=14,) #Entryboxเป็นช่องให้พิมข้อความ
    login_telentry.place(x=859,y=358)


    def login_user():
        global Tel_login
        name_login = login_usentry.get()
        Tel_login = login_telentry.get()       

        if Tel_login.startswith("0"):     
            # วนลูปผ่านรายการสินค้าและเพิ่มลงใน Listbox
            error_massages=[]

            if not Tel_login.isdigit():
                error_massages.append("เบอร์โทรต้องเป็นตัวเลขเท่านั้น!!!")
        
            if len(Tel_login) > 10 :    # len คือขนาดของสิ่งที่อยู่ในวงเล็บ
                error_massages.append("เบอร์โทรต้องมี 10 หลัก!!!")

            if len(Tel_login) < 10 :    # len คือขนาดของสิ่งที่อยู่ในวงเล็บ
                error_massages.append("เบอร์โทรต้องมี 10 หลัก!!!")

            if not error_massages :
                c = conn.cursor()
                c.execute("SELECT * FROM member WHERE username=? AND Tel=?", (name_login,Tel_login,))
                conn.commit()
                result = c.fetchone()

                if result:
                    login_usentry.delete(0,tk.END)
                    login_telentry.delete(0,tk.END)  
                    login_menu()

                else:
                    messagebox.showerror("ข้อผิดพลาด", "รหัสไม่ถูกต้อง")
                    # ลบข้อมูลที่กรอกลงในช่อง entry
                    login_usentry.delete(0,tk.END)
                    
                    login_telentry.delete(0,tk.END)
                        
            else :
                # แสดงข้อความข้อผิดพลาด
                error_message = "\n".join(error_massages)
                messagebox.showerror("Error", error_message)   

                # ลบข้อมูลที่กรอกลงในช่อง entry
                login_usentry.delete(0,tk.END)
                
                login_telentry.delete(0,tk.END) 

        else:
            messagebox.showerror("ข้อผิดพลาด", "เบอร์โทรไม่ขึ้นต้นด้วย 0")
            # ลบข้อมูลที่กรอกลงในช่อง entry
            login_usentry.delete(0,tk.END)
            
            login_telentry.delete(0,tk.END)



    Button(loginbg, image=bttn_back, command=backmainlogin,bg='#DC416D',bd=0).place(x=31,y=15)
    Button(loginbg, image=bttn_done, command=login_user,bg='#DC416D',bd=0).place(x=885,y=520,width=145,height=46)


# Login main menu (menu buy historybill bill)
def login_menu():
    global loginmain,photo
    loginbg.withdraw()
    loginmain = Toplevel(loginbg)  
    loginmain.title("HOME CHUB")
    loginmain.geometry("1200x675+180+50")
    loginmain.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\home22home.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(loginmain, image=photo)
    lbl.pack()

    def backloginmain():
        loginbg.withdraw()
        loginmain.withdraw()
        root.deiconify()
    


    Button(loginmain, image=bttn_back, command=backloginmain,bg='#DC416D',bd=0).place(x=35,y=38,width=145,height=46)
    Button(loginmain, image=bttn_menu, command=login_showmenu,bg='#DC416D',bd=0).place(x=249,y=418)
    Button(loginmain, image=bttn_buy,  command=login_buy,bg='#ffffff',bd=0).place(x=770,y=418)
    Button(loginmain, image=bttn_bill, command=login_bill,bg='#ffffff',bd=0).place(x=770,y=535)
    Button(loginmain, image=bttn_historybill, command=login_historybill,bg='#DC416D',bd=0).place(x=215,y=522)

   
def login_showmenu():
    global menu_page,photo
    loginmain.withdraw()
    menu_page = Toplevel(loginmain)  
    menu_page.title("MENU")
    menu_page.geometry("1200x675+180+50")
    menu_page.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\menu.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(menu_page, image=photo)
    lbl.pack()
        
    def on_mousewheel(event):      
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas = tk.Canvas(menu_page, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0, scrollregion=(0, 0, 700, 5000))  #กล่องตรงกลาง
    canvas.place(x=180,y=150, width=850, height=470)
    product = tk.Frame(canvas, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0) 
    canvas.create_window((0, 0), window=product, anchor='nw')
    
    menu_page.bind("<MouseWheel>", on_mousewheel) 
    
    def show_menu():
        c.execute("SELECT id_stock, name, price, picture FROM stock ")
        conn.commit()  
        pictures = c.fetchall()  

        for i, x in enumerate(pictures):    #แปลงภาพ
            image = Image.open(BytesIO(x[3]))
            target_width, target_height = 117, 166  #ปรับความกว้างและความยาวของ product
            image = image.resize((target_width, target_height))   #ปรับขนาดรูปภาพให้ตรงกับขนาดเป้าหมาย
            image = ImageTk.PhotoImage(image)    #แปลงรูปภาพ Pillow เป็น ImageTk.PhotoImage
            label = Label(product, image=image, width=117, height=164,highlightthickness=0,bd=0)  #ปรับขนาดปุ่ม
            label.image = image
            label.grid(row=i // 6, column=i % 6, padx=10, pady=10)

    def backshowmenu():
        login_menu()
        menu_page.withdraw()

    
    show_menu()
    Button(menu_page, image=bttn_back, command=backshowmenu,bg='#DC416D',bd=0).place(x=40,y=39,width=145,height=46)
       

def login_buy():
    global login_selectmenubg,photo
    loginmain.withdraw()
    login_selectmenubg = Toplevel(loginmain)
    login_selectmenubg.title("SELECT MENU")
    login_selectmenubg.geometry("1200x675+180+50")
    login_selectmenubg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\selectmenu.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(login_selectmenubg, image=photo)
    lbl.pack() 

    buy_listbox = tk.Listbox(login_selectmenubg, bg="#ffffff", borderwidth=0, font=("Times", 14), fg="#333333", relief="sunken")
    buy_listbox.place(x=700, y=210, width=420, height=320)

    label_quantity = Label(login_selectmenubg, highlightthickness=0,bd=0,font=("Times", 14) ) #ปรับขนาดปุ่ม
    label_quantity.place(x=650, y=20, width=200, height=40)

    label_text = Label(login_selectmenubg,text="กรอกจำนวน :" ,bg="white", highlightthickness=0,bd=0,font=("Times", 14) ) #ปรับขนาดปุ่ม
    label_text.place(x=650, y=130, width=130, height=40)

    entry_quantity = Entry(login_selectmenubg,highlightthickness=0,bd=0,font=("Times", 14) )
    entry_quantity.place(x=800, y=130, width=200, height=40)


    def show_cart():
        buy_listbox.delete(0,tk.END)
        c.execute("SELECT  id_order ,name, Price,quantity FROM myOrder ")
        donuts_inbasket = c.fetchall()

        for x in donuts_inbasket:
            
            id_order,name_order, price_order,quantity_order = x
            donuts_basket.append(id_order)
            item_text = f"{name_order} ราคา: {price_order} บาท จำนวน: {quantity_order}"
            buy_listbox.insert(tk.END, item_text) #tk.END เพื่อให้ข้อมูลถูกเพิ่มไปด้านล่างของ Listbox.        


    def on_mousewheel(event):      
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas = tk.Canvas(login_selectmenubg, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0, scrollregion=(0, 0, 400, 5000))  #กล่องตรงกลาง
    canvas.place(x=60,y=100, width=490, height=470)
    product = tk.Frame(canvas, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0) 
    canvas.create_window((0, 0), window=product, anchor='nw')

    login_selectmenubg.bind("<MouseWheel>", on_mousewheel) 
    
    def show_menu():
        c.execute("SELECT id_stock, name, price, picture,quantity FROM stock ")
        conn.commit()  
        pictures = c.fetchall()     

        def pickedup_cart(item):
            def pickedup():
                def show_quantity():
                    c.execute("SELECT quantity FROM stock WHERE name=? ",(item[1],))
                    result = c.fetchall()  
                    label_quantity.configure(text="คงเหลือ : {}".format (result[0][0],))

                def add_to_order():
                    name = item[1]
                    quantity = int(entry_quantity.get())
                    c.execute("SELECT quantity FROM stock WHERE name=? ",(item[1],))
                    result = c.fetchall()

                    if quantity<result[0][0]:
                        c.execute("INSERT INTO myOrder (name,Price,quantity) VALUES (?,?,?)", (item[1], (item[2]),entry_quantity.get()))
                        conn.commit() 
                        c.execute("UPDATE stock SET quantity=quantity - ? WHERE name =? ",(quantity,name))
                        conn.commit()
                        show_quantity()
                        entry_quantity.delete(0,tk.END)
                        show_menu()
                        show_cart()
                     
                    else:
                        messagebox.showerror("error","สินค้าไม่เพียงพอ")
                        entry_quantity.delete(0,tk.END)
                show_quantity()
                button_quantity = tk.Button(login_selectmenubg,image=bttn_done, command=add_to_order,bg='#DC416D',bd=0).place(x=700,y=575,width=145,height=46)

            return pickedup

        for i, x in enumerate(pictures):    #แปลงภาพ
            image = Image.open(BytesIO(x[3]))
            target_width, target_height = 117, 166  #ปรับความกว้างและความยาวของ product
            image = image.resize((target_width, target_height))   #ปรับขนาดรูปภาพให้ตรงกับขนาดเป้าหมาย
            image = ImageTk.PhotoImage(image)    #แปลงรูปภาพ Pillow เป็น ImageTk.PhotoImage

            label = Button(product, image=image,command=pickedup_cart(x), width=117, height=166)  #ปรับขนาดปุ่ม
            label.configure(bd=0,borderwidth=0)
            label.image = image
            label.grid(row=i // 4, column=i % 4, padx=2, pady=2)

        
    def login_backselectmenu():
        login_menu()
        login_selectmenubg.withdraw()

    def delete_cart():  #ลบของในตะกร้า
            idd_order = buy_listbox.curselection()

            if not idd_order:
                messagebox.showinfo(title=None,message="โปรดเลือกสินค้าก่อน")
                return
            
            for index in idd_order:  
                id_order = donuts_basket[index]  
                c.execute("SELECT name,quantity FROM myOrder WHERE id_order=?", (id_order,))
                result = c.fetchone()

                name,quantity=result
                c.execute("UPDATE stock SET quantity=quantity + ? WHERE name =? ",(quantity,name))
                conn.commit()

                c.execute("SELECT quantity FROM stock WHERE name=? ",(name,))
                result = c.fetchall() 

                label_quantity.configure(text="คงเหลือ : {}".format (result[0][0],))
                c.execute("DELETE FROM myOrder WHERE id_order=?", (id_order,))
                conn.commit()
                
                # ลบรายการที่เลือกจาก Listbox
                buy_listbox.delete(index) 
                donuts_basket.clear()
            
                show_cart()



    show_menu()
    Button(login_selectmenubg, image= bttn_pay, command=login_buy_bill,bg='#DC416D',bd=0).place(x=973,y=575,width=145,height=46)
    Button(login_selectmenubg, image=bttn_back, command=login_backselectmenu,bg='#DC416D',bd=0).place(x=75,y=585,width=145,height=46)
    Button(login_selectmenubg, image=bttn_editorder, command=delete_cart,bg='#DC416D',bd=0).place(x=360,y=585)
    

def login_pay():
    global login_paybg,photo
    login_selectmenubg.withdraw()
    login_paybg = Toplevel(login_selectmenubg)
    login_paybg.title("BILL")
    login_paybg.geometry("1200x675+180+50")
    login_paybg.resizable(False,False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\bill.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(login_paybg, image=photo)
    lbl.pack()


def login_historybill():
    global login_historybg,photo
    loginmain.withdraw()
    login_historybg = Toplevel(loginmain)
    login_historybg.title("HISTORY BILL")
    login_historybg.geometry("1200x675+180+50")
    login_historybg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\historybill.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(login_historybg, image=photo)
    lbl.pack()
    
    def history_bill_login():
        history_bill_listbox.delete(0,tk.END)
        c.execute("SELECT * FROM bill WHERE customer_name=?",(Tel_login,))
        conn.commit()
        result = c.fetchall()
        i = 1
        z.clear()

        for x in result:
                history_bill_listbox.insert(x[0],"  {}    date: {}    total price:  {} ".format(i,x[3],x[2]))
                z.append(x[0])
                i+=1 

    def login_backhistorybg():
        login_menu()
        login_historybg.withdraw()

    history_bill_listbox = tk.Listbox(login_historybg, bg="#ffffff", font=("Times", 14), fg="#333333",relief="flat")
    history_bill_listbox.place(x=335, y=180, width=550, height=420)


    history_bill_login()
    Button(login_historybg, image=bttn_done, command=login_backhistorybg,bg='#DC416D',bd=0).place(x=980,y=585,width=145,height=46)
    Button(login_historybg, image=bttn_back, command=login_backhistorybg,bg='#DC416D',bd=0).place(x=75,y=585,width=145,height=46)


def login_buy_bill():
    global login_buy_billbg,photo
    loginmain.withdraw()
    login_selectmenubg.withdraw()
    login_buy_billbg = Toplevel(loginmain)
    login_buy_billbg.title("BILL")
    login_buy_billbg.geometry("1200x675+180+50")
    login_buy_billbg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\bill.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(login_buy_billbg, image=photo)
    lbl.pack()


    def total_bill():
        date = time.strftime("%d/%m/%Y",)
        month = time.strftime("%m/%Y",)
        c.execute("SELECT name,Price,quantity FROM myOrder ")
        result=c.fetchall()
        total_login_price = 0

        

        buy_bill_login =f"รายการ         จำนวน                   ราคา"
        
        for donut,price,quantity  in result:
            total=price*quantity 
            buy_bill_login += f"\n{str(donut).ljust(25)}{str(quantity).ljust(10)}           {total:.2f} บาท"    
            total_login_price = total_login_price + total

        buy_bill_login+= f"\nยอดรวม                              {total_login_price:.2f} บาท"
        buy_bill_login += f"\nวันที่                                 {date} "

        receipt_label_login = Label(login_buy_billbg, text=buy_bill_login, font=("Time", 16),bg="#FFFFFF",anchor='n')
        receipt_label_login.place(x=370,y=170,width=470,height=400)

        def submit_login():
                c.execute("INSERT INTO bill (order_total,price,date,month,customer_name) VALUES (?,?,?,?,?)", (buy_bill_login,total_login_price,date,month,Tel_login))
                conn.commit() 
                c.execute("DELETE FROM myOrder")
                conn.commit()
                print_receipt_login()


        def print_receipt_login():
                    receipt_buy_login=tk.Toplevel(login_buy_billbg)
                    receipt_buy_login.title("RECEIPT")
                    receipt_buy_login.geometry("470x400+370+170")
                    c.execute("SELECT order_total,customer_name FROM bill ")
                    results = c.fetchall()

                    for order,customer_name in results:
                    
                        receipt_login_for_customer =f"Receipt\n"
                        receipt_login_for_customer+=f"\n"
                        receipt_login_for_customer+=f"user : {customer_name}\n"
                        receipt_login_for_customer+=f"\n"
                        receipt_login_for_customer +=f"{order}"


                    receipt_label = Label(receipt_buy_login, text=receipt_login_for_customer, font=("Time", 16),bg="#FFFFFF",anchor='n')
                    receipt_label.place(x=0,y=0,width=470,height=400)

                    def back_login_receipt():
                        receipt_buy_login.withdraw()
                        login_menu()

                    Button(receipt_buy_login, text="Back", bg="#FFFFFF", command=back_login_receipt, fg='#DC416D', bd=0).place(x=30,y=350,width=80,height=50)

                    login_buy_billbg.withdraw()
                    receipt_buy_login.mainloop()


        def clear_login():  #เคลียร์ ตาราง
                c.execute("SELECT name FROM myOrder")
                result = c.fetchall()
                x=0

                for x in range(len(result)):
                    c.execute("SELECT quantity FROM myOrder WHERE name=?",(result[x][0],))
                    results = c.fetchone()
                    name=(result[x][0])
                    quantity=(results[0])
                    c.execute("UPDATE stock SET quantity=quantity + ? WHERE name =? ",(quantity,name))
                    conn.commit()
                    x+=1
                    row = str(x)
                    c.execute("DELETE FROM myOrder WHERE rowid = ?",row )
                    conn.commit()
                c.execute("DELETE FROM myOrder")
                conn.commit()

                login_buy()
                login_buy_billbg.withdraw()

        
        Button(login_buy_billbg, image= bttn_paid, command=submit_login,bg='#DC416D',bd=0).place(x=990,y=585,width=145,height=46)
        Button(login_buy_billbg, image=bttn_back, command=clear_login,bg='#DC416D',bd=0).place(x=75,y=585,width=145,height=46)
    total_bill()



def login_bill():
    global login_billbg,photo
    loginmain.withdraw()
    login_billbg = Toplevel(loginmain)
    login_billbg.title("RECEIPT")
    login_billbg.geometry("470x400+300+160")
    login_billbg.resizable(False, False)


    def last_bill():

        c.execute("SELECT order_total FROM bill WHERE customer_name=? ORDER BY id_bill DESC LIMIT 1",(Tel_login,))
        last_result_login=c.fetchall()  

        if last_result_login:
            last_receipt_label_register = Label(login_billbg, text=last_result_login[0][0], font=("Time", 16),bg="#FFFFFF",anchor='n')
            last_receipt_label_register.place(x=0,y=0,width=470,height=400)

        else:
            messagebox.showerror("แจ้งเตือน","กรุณาซื้อของก่อน")
            login_buy()
            login_billbg.withdraw()  

    def login_backbillbg():
        login_menu()
        login_billbg.withdraw()

    
    last_bill()
    Button(login_billbg, text="Back", bg="#FFFFFF", command=login_backbillbg, fg='#DC416D', bd=0).place(x=30,y=350,width=80,height=50)


def paid2():
    global paid,photo
    login_billbg.withdraw()
    paid = Toplevel(login_billbg)
    paid.title("THANK YOU")
    paid.geometry("1200x675+180+50")
    paid.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\home22home.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(paid, image=photo)
    lbl.pack()


############### regist ###############

def register():
    global regisbg,photo
    root.withdraw()
    regisbg = Toplevel(root)  
    regisbg.title("REGISTER")
    regisbg.geometry("1200x675+180+50")
    regisbg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\regisbg.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(regisbg, image=photo)
    lbl.pack()


    registusername = tk.StringVar()  
    regist_usentry = tk.Entry(regisbg, textvariable=registusername,font=("Arial", 20),fg='#DC416D',bg="#F4F3BD", bd=0,width=14,) #Entryboxเป็นช่องให้พิมข้อความ
    regist_usentry.place(x=840,y=170)

    regist_tel = tk.IntVar()
    regist_tel.set("")
    regist_telentry=tk.Entry(regisbg,textvariable=regist_tel,font=("Arial", 20),fg='#DC416D',bg="#F4F3BD",bd =0,width=14,) #Entryboxเป็นช่องให้พิมข้อความ
    regist_telentry.place(x=840,y=340)

    def add_user():
        global regist_Tel

        regist_name = regist_usentry.get()
        regist_Tel = regist_telentry.get()       

        if regist_Tel.startswith("0"):
            error_massages=[]

            if not regist_Tel.isdigit():
                error_massages.append("เบอร์โทรต้องเป็นตัวเลขเท่านั้น!!!")
        
            elif len(regist_Tel) > 10 :    # len คือขนาดของสิ่งที่อยู่ในวงเล็บ
                error_massages.append("เบอร์โทรต้องมี 10 หลัก!!!")

            elif len(regist_Tel) < 10 :    # len คือขนาดของสิ่งที่อยู่ในวงเล็บ
                error_massages.append("เบอร์โทรต้องมี 10 หลัก!!!")

            elif not error_massages :
                c = conn.cursor()
                c.execute("SELECT * FROM member WHERE Tel = ?",(regist_Tel,))
                result = c.fetchall()

                if result:
                    messagebox.showerror("ผิดพลาด","เบอร์นี้ถูกใช้งานแล้ว")
                    regist_usentry.delete(0,tk.END)
                    regist_telentry.delete(0,tk.END) 

                else :
                    data = (regist_name, regist_Tel) 
                    c.execute("INSERT INTO member (username, Tel) VALUES ( ?, ?)",data)
                    conn.commit()
                    regist_usentry.delete(0,tk.END)
                    regist_telentry.delete(0,tk.END)  
                    register_menu()
                
            else :
                # แสดงข้อความข้อผิดพลาด
                error_message = "\n".join(error_massages)
                messagebox.showerror("Error", error_message)   

                # ลบข้อมูลที่กรอกลงในช่อง entry
                regist_usentry.delete(0,tk.END)
                regist_telentry.delete(0,tk.END) 

        else:
            messagebox.showerror("ข้อผิดพลาด", "เบอร์โทรไม่ขึ้นต้นด้วย 0")
            # ลบข้อมูลที่กรอกลงในช่อง entry
            regist_usentry.delete(0,tk.END)
            regist_telentry.delete(0,tk.END)


    Button(regisbg,image=bttn_back, command=backmainregis,bg='#DC416D',bd=0).place(x=31,y=15)
    Button(regisbg,image=bttn_done,command=add_user,bg='#DC416D',bd=0).place(x=865,y=538,width=145,height=46)



# Register main menu (menu buy historybill bill)
def register_menu():
    global registermain,photo
    regisbg.withdraw()
    registermain = tk.Toplevel(regisbg)  
    registermain.title("HOME CHUB")
    registermain.geometry("1200x675+180+50")
    registermain.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\home22home.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(registermain, image=photo)
    lbl.pack()


    def backregishome():
        regisbg.withdraw()
        registermain.withdraw()
        root.deiconify()
    


    Button(registermain, image=bttn_back, command=backregishome,bg='#DC416D',bd=0).place(x=35,y=38,width=145,height=46)
    Button(registermain, image=bttn_menu, command=register_showmenu,bg='#DC416D',bd=0).place(x=249,y=418)
    Button(registermain, image=bttn_buy,  command=register_buy,bg='#ffffff',bd=0).place(x=770,y=418)
    Button(registermain, image=bttn_bill, command=register_bill,bg='#ffffff',bd=0).place(x=770,y=535)
    Button(registermain, image=bttn_historybill, command=register_historybill,bg='#DC416D',bd=0).place(x=210,y=523)


def register_showmenu():
    global register_menubg,photo
    registermain.withdraw()
    register_menubg = Toplevel(registermain)  
    register_menubg.title("MENU")
    register_menubg.geometry("1200x675+180+50")
    register_menubg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\menu.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(register_menubg, image=photo)
    lbl.pack()


    def on_mousewheel(event):      
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas = tk.Canvas(register_menubg, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0, scrollregion=(0, 0, 700, 5000))  #กล่องตรงกลาง
    canvas.place(x=180,y=150, width=850, height=470)
    product = tk.Frame(canvas, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0) 
    canvas.create_window((0, 0), window=product, anchor='nw')
    
    register_menubg.bind("<MouseWheel>", on_mousewheel) 
    
    def show_menu():
        c.execute("SELECT id_stock, name, price, picture FROM stock ")
        conn.commit()  
        pictures = c.fetchall() 
                   
        for i, x in enumerate(pictures):    #แปลงภาพ
            image = Image.open(BytesIO(x[3]))
            target_width, target_height = 117, 166  #ปรับความกว้างและความยาวของ product
            image = image.resize((target_width, target_height))   #ปรับขนาดรูปภาพให้ตรงกับขนาดเป้าหมาย
            image = ImageTk.PhotoImage(image)    #แปลงรูปภาพ Pillow เป็น ImageTk.PhotoImage
            label = Label(product, image=image, width=117, height=166)  #ปรับขนาดปุ่ม
            label.image = image
            label.grid(row=i // 6, column=i % 6, padx=10, pady=10)

    def register_backmenubg():
        register_menu()
        register_menubg.withdraw()


    show_menu() 
    Button(register_menubg, image=bttn_back, command=register_backmenubg,bg='#DC416D',bd=0).place(x=40,y=39,width=145,height=46)


def register_pay():
    global register_paybg,photo
    register_selectmenubg.withdraw()
    register_paybg = Toplevel(register_selectmenubg)
    register_paybg.title("BILL")
    register_paybg.geometry("1200x675+180+50")
    register_paybg.resizable(False,False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\bill.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(register_paybg, image=photo)
    lbl.pack()



def register_historybill():
    global register_historybg,photo
    registermain.withdraw()
    register_historybg = Toplevel(registermain)
    register_historybg.title("HISTORY BILL")
    register_historybg.geometry("1200x675+180+50")
    register_historybg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\historybill.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(register_historybg, image=photo)
    lbl.pack()

    def history_bill_register():
        history_bill_listbox.delete(0,tk.END)
        c.execute("SELECT * FROM bill WHERE customer_name=?",(regist_Tel,))
        conn.commit()
        result = c.fetchall()
        i = 1
        z.clear()

        for x in result:
                history_bill_listbox.insert(x[0],"  {}    date: {}    total price:  {} ".format(i,x[3],x[2]))
                z.append(x[0])
                i+=1 

    history_bill_listbox = tk.Listbox(register_historybg, bg="#ffffff", font=("Times", 14), fg="#333333",relief="flat")
    history_bill_listbox.place(x=335, y=180, width=550, height=420)

    history_bill_register()

    def register_backhistorybg():
        register_menu()
        register_historybg.withdraw()


    Button(register_historybg, image=bttn_back, command=register_backhistorybg,bg='#DC416D',bd=0).place(x=75,y=585,width=145,height=46)
    Button(register_historybg, image=bttn_done, command=register_backhistorybg,bg='#DC416D',bd=0).place(x=980,y=585,width=145,height=46)

  
def register_buy():
    global register_selectmenubg,photo
    registermain.withdraw()
    register_selectmenubg = Toplevel(registermain)
    register_selectmenubg.title("SELECT MENU")
    register_selectmenubg.geometry("1200x675+180+50")
    register_selectmenubg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\selectmenu.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(register_selectmenubg, image=photo)
    lbl.pack()

    register_buy_listbox = tk.Listbox(register_selectmenubg, bg="#ffffff", borderwidth=0, font=("Times", 14), fg="#333333", relief="sunken")
    register_buy_listbox.place(x=700, y=210, width=420, height=320)

    label_quantity_regis = Label(register_selectmenubg, highlightthickness=0,bd=0,font=("Times", 14) ) #ปรับขนาดปุ่ม
    label_quantity_regis.place(x=650, y=20, width=200, height=40)

    label_text_regis = Label(register_selectmenubg,text="กรอกจำนวน :" ,bg="white", highlightthickness=0,bd=0,font=("Times", 14) ) #ปรับขนาดปุ่ม
    label_text_regis.place(x=650, y=130, width=130, height=40)

    entry_quantity_regis = Entry(register_selectmenubg,highlightthickness=0,bd=0,font=("Times", 14) )
    entry_quantity_regis.place(x=800, y=130, width=200, height=40)

    def show_cart_register():
        register_buy_listbox.delete(0,tk.END)
        c.execute("SELECT  id_order ,name, Price,quantity FROM myOrder ")
        donuts_inbasket = c.fetchall()

        for x in donuts_inbasket:
            id_order,name_order, price_order,quantity_order = x
            donuts_basket.append(id_order)
            item_text = f"{name_order} ราคา: {price_order} บาท จำนวน: {quantity_order}"
            register_buy_listbox.insert(tk.END, item_text) #tk.END เพื่อให้ข้อมูลถูกเพิ่มไปด้านล่างของ Listbox.        
                 


    def on_mousewheel(event):      
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas = tk.Canvas(register_selectmenubg, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0, scrollregion=(0, 0, 400, 5000))  #กล่องตรงกลาง
    canvas.place(x=60,y=100, width=490, height=470)
    product = tk.Frame(canvas, highlightbackground="#FFFFFF",bg="#FFFFFF",highlightthickness=0) 
    canvas.create_window((0, 0), window=product, anchor='nw')
    
    register_selectmenubg.bind("<MouseWheel>", on_mousewheel) 
    
    def show_menu_register():
        c.execute("SELECT id_stock, name, price, picture FROM stock ")
        conn.commit()  
        pictures = c.fetchall()     

        def pickedup_cart(item):
            def pickedup():
                def show_quantity():
                    c.execute("SELECT quantity FROM stock WHERE name=? ",(item[1],))
                    result = c.fetchall()  
                    label_quantity_regis.configure(text="คงเหลือ : {}".format (result[0][0],))
        
                def add_to_order():
                    name = item[1]
                    quantity = int(entry_quantity_regis.get())
                    c.execute("SELECT quantity FROM stock WHERE name=? ",(item[1],))
                    result = c.fetchall() 

                    if quantity<result[0][0]:
                        c.execute("INSERT INTO myOrder (name,Price,quantity) VALUES (?,?,?)", (item[1], (item[2]),entry_quantity_regis.get()))
                        conn.commit() 
                        c.execute("UPDATE stock SET quantity=quantity - ? WHERE name =? ",(quantity,name))
                        conn.commit()
                        show_quantity()
                        entry_quantity_regis.delete(0,tk.END)
                        show_menu_register()
                        show_cart_register()

                    else :
                        messagebox.showerror("error","สินค้าไม่เพียงพอ")
                        entry_quantity_regis.delete(0,tk.END)
                show_quantity()

                button_quantity = tk.Button(register_selectmenubg,image=bttn_done, command=add_to_order,bg='#DC416D',bd=0).place(x=700,y=575,width=145,height=46)

            return pickedup


        for i, x in enumerate(pictures):    #แปลงภาพ
            image = Image.open(BytesIO(x[3]))
            target_width, target_height = 117, 166  #ปรับความกว้างและความยาวของ product
            image = image.resize((target_width, target_height))   #ปรับขนาดรูปภาพให้ตรงกับขนาดเป้าหมาย
            image = ImageTk.PhotoImage(image)    #แปลงรูปภาพ Pillow เป็น ImageTk.PhotoImage

            label = Button(product, image=image,command=pickedup_cart(x), width=117, height=166)  #ปรับขนาดปุ่ม
            label.configure(bd=0,borderwidth=0)
            label.image = image
            label.grid(row=i // 4, column=i % 4, padx=2, pady=2)

    def delete_cart():  #ลบของในตะกร้า
            idd_order = register_buy_listbox.curselection()

            if not idd_order:
                messagebox.showinfo(title=None,message="โปรดเลือกสินค้าก่อนลบ")
                return
            
            for index in idd_order:     
                id_order = donuts_basket[index]  
                c.execute("DELETE FROM myOrder WHERE id_order=?", (id_order,))
                conn.commit()
                
                # ลบรายการที่เลือกจาก Listbox
                register_buy_listbox.delete(index) 
                donuts_basket.clear()
            
                show_cart_register()
    def register_backselectmenubg():
        register_menu()
        register_selectmenubg.withdraw()

    show_menu_register()
    Button(register_selectmenubg, image=bttn_back, command=register_backselectmenubg,bg='#DC416D',bd=0).place(x=75,y=585,width=145,height=46)
    Button(register_selectmenubg, image= bttn_pay, command=register_buy_bill,bg='#DC416D',bd=0).place(x=973,y=575,width=145,height=46)
    Button(register_selectmenubg, image=bttn_editorder, command=delete_cart,bg='#DC416D',bd=0).place(x=360,y=585)


def register_buy_bill():
    global register_buy_billbg,photo
    register_selectmenubg.withdraw()
    register_buy_billbg = Toplevel(registermain)
    register_buy_billbg.title("BILL")
    register_buy_billbg.geometry("1200x675+180+50")
    register_buy_billbg.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\bill.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(register_buy_billbg, image=photo)
    lbl.pack()

    def register_total_bill():
        date = time.strftime("%d/%m/%Y",)
        month = time.strftime("%m/%Y",)
        c.execute("SELECT name,Price,quantity FROM myOrder ")
        result=c.fetchall()
        total_login_price = 0

        receipt_login =f"รายการ         จำนวน                   ราคา"

        for donut,price,quantity  in result:
            total=price*quantity 
            receipt_login += f"\n{str(donut).ljust(25)}{str(quantity).ljust(10)}           {total:.2f} บาท"     
            total_login_price = total_login_price + total

        receipt_login+= f"\nยอดรวม                              {total_login_price:.2f} บาท"
        receipt_login += f"\nวันที่                                 {date} "

        receipt_label_login = Label(register_buy_billbg, text=receipt_login, font=("Time", 16),bg="#FFFFFF",anchor='n')
        receipt_label_login.place(x=370,y=170,width=470,height=400)

        def clear_register():  #เคลียร์ ตาราง
                c.execute("SELECT name FROM myOrder")
                result = c.fetchall()
                x=0

                for x in range(len(result)):
                    c.execute("SELECT quantity FROM myOrder WHERE name=?",(result[x][0],))
                    results = c.fetchone()
                    name=(result[x][0])
                    quantity=(results[0])
                    c.execute("UPDATE stock SET quantity=quantity + ? WHERE name =? ",(quantity,name))
                    conn.commit()
                    x+=1
                    row = str(x)
                    c.execute("DELETE FROM myOrder WHERE rowid = ?",row )
                    conn.commit()

                c.execute("UPDATE stock SET quantity=quantity + ? WHERE name =? ",(quantity,name))
                conn.commit()
                c.execute("DELETE FROM myOrder" )
                conn.commit()
                register_buy()
                register_buy_billbg.withdraw()



        def submit_register():
                    c.execute("INSERT INTO bill (order_total,price,date,month,customer_name) VALUES (?,?,?,?,?)", (receipt_login,total_login_price,date,month,regist_Tel))
                    conn.commit() 
                    c.execute("DELETE FROM myOrder")
                    conn.commit()
                    print_receipt_register()



        def print_receipt_register():
                    receipt_buy_register=tk.Toplevel(register_buy_billbg)
                    receipt_buy_register.title("RECEIPT")
                    receipt_buy_register.geometry("470x400+370+170")
                    c.execute("SELECT order_total,customer_name FROM bill ")
                    results = c.fetchall()

                    for order,customer_name in results:
                    
                        receipt_login_for_customer =f"Receipt\n"
                        receipt_login_for_customer+=f"\n"
                        receipt_login_for_customer+=f"user : {customer_name}\n"
                        receipt_login_for_customer+=f"\n"
                        receipt_login_for_customer +=f"{order}"


                    receipt_label = Label(receipt_buy_register, text=receipt_login_for_customer, font=("Time", 16),bg="#FFFFFF",anchor='n')
                    receipt_label.place(x=0,y=0,width=470,height=400)

                    def back_register_receipt():
                        receipt_buy_register.withdraw()
                        register_menu()

                    Button(receipt_buy_register, text="Back", bg="#FFFFFF", command=back_register_receipt, fg='#DC416D', bd=0).place(x=30,y=350,width=80,height=50)

                    register_buy_billbg.withdraw()
                    receipt_buy_register.mainloop()


        Button(register_buy_billbg, image= bttn_back, command=clear_register,bg='#DC416D',bd=0).place(x=75,y=585,width=145,height=46)
        Button(register_buy_billbg, image=bttn_paid, command=submit_register,bg='#DC416D',bd=0).place(x=990,y=585,width=145,height=46)
    register_total_bill()



def register_bill():
    global register_billbg,photo
    registermain.withdraw()
    register_billbg = Toplevel(registermain)
    register_billbg.title("RECEIPT")
    register_billbg.geometry("470x400+180+50")
    register_billbg.resizable(False, False)


    def last_bill():
        c.execute("SELECT order_total FROM bill WHERE customer_name=? ORDER BY id_bill DESC LIMIT 1",(regist_Tel,))
        last_result_register=c.fetchall()
    
        if last_result_register:
            last_receipt_label_register = Label(register_billbg, text=last_result_register[0][0], font=("Time", 16),bg="#FFFFFF",anchor='n')
            last_receipt_label_register.place(x=0,y=0,width=470,height=400)

        else:
            messagebox.showerror("แจ้งเตือน","กรุณาซื้อของก่อน")
            register_buy()
            register_billbg.withdraw()    


    def register_backbillbg():
        register_menu()
        register_billbg.withdraw()

    last_bill()


    Button(register_billbg, text="Back", bg="#FFFFFF", command=register_backbillbg, fg='#DC416D', bd=0).place(x=30,y=350,width=80,height=50)


def paid1():
    global paid,photo
    register_billbg.withdraw()
    paid = Toplevel(register_billbg)
    paid.title("THANK YOU")
    paid.geometry("1200x675+180+50")
    paid.resizable(False, False)
    img = Image.open(r"C:\Users\pitch\Videos\Captures\projectchubby\home22home.png")
    photo = ImageTk.PhotoImage(img)
    lbl = Label(paid, image=photo)
    lbl.pack()  



#Buttons in first page

Button(root ,text="Developer", font=("Arial", 12), command=developer, bg='#DC416D', fg='#FFFFFF', bd=0).place(x=50, y=30, width=80, height=40)

regis = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\regisbttn.png")
Button(root,image=regis,bd=0,command=register).place(x=930,y=545,width=190,height=80)

staff = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\staffbttn.png")
Button(root,image=staff,bd=0,command=staff1).place(x=95,y=545,width=190,height=80)

login2 = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\loginbttn.png")
Button(root,image=login2,bd=0,command=login).place(x=636,y=548,width=189,height=78)

quit1 = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttnquit.png")
Button(root,image=quit1,bd=0,command=quit).place(x=1020,y=45,width=130,height=52)
    

#Import all pic
bttn_back = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_back.png")
bttn_done = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_done.png")
bttn_next = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_next.png")
bttn_menu = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_menu.png")
bttn_editbill = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_editbill.png")
bttn_historybill = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_historybill.png")
bttn_buy = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_buy.png")
bttn_bill = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_bill.png")
bttn_orderhistory = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttnorderhistory.png")
bttn_addstock = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_addstock.png")
bttn_pay = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_pay.png")
bttn_editorder =PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_editorder.png")
bttn_paid  =PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_paid.png")
bttn_check =PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_check.png")
bttn_add= PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_add.png")
bttn_delete = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_delete.png")
bttn_editcus = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_editcus.png")
bttn_edit = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_edit.png")
bttn_seles = PhotoImage(file=r"C:\Users\pitch\Videos\Captures\projectchubby\bttn_sales.png")


root.mainloop()