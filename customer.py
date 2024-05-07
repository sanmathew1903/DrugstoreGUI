# create table customer(id int auto_increment primary key,name varchar(30),phone varchar(10),date date);
# alter table customer add constraint PK_customer primary key(phone);
import mysql.connector as my
from datetime import date
import tkinter as tk
from tkinter import messagebox


class DBinitiate:
    def __init__(self):
        self.mydb = my.connect(host="localhost", user="root",passwd="sanmathew", database="drugstore")
        self.mycursor = self.mydb.cursor()


class authenticate():

    def __init__(self, root):
        self.root = root
        self.root.title("Authentication")

        self.authenticateUI()

    

    def authenticateUI(self):

        def signup():
            tk.Label(self.root, text="SIGNUP", font=("Arial", 14, "bold")).pack(pady=5)
            self.add_customer_frame = tk.LabelFrame(self.root, text="Set Credentials")
            self.add_customer_frame.pack(padx=10, pady=10, fill=tk.BOTH)
            tk.Label(self.add_customer_frame, text="Set Username:").grid(row=0, column=0, padx=5, pady=5)
            self.username = tk.Entry(self.add_customer_frame)
            self.username.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(self.add_customer_frame, text="Set Password:").grid(
                row=1, column=0, padx=5, pady=5)
            self.password = tk.Entry(self.add_customer_frame)
            self.password.grid(row=1, column=1, padx=5, pady=5)

            self.submit_button = tk.Button(self.add_customer_frame, text="Submit", command=(self.setCredentials))
            self.submit_button.grid(row=5, columnspan=5, padx=5, pady=5)
            
            


        def login():
            tk.Label(self.root, text="LOGIN", font=("Arial", 14, "bold")).pack(pady=5)

            self.add_customer_frame = tk.LabelFrame(self.root, text="Enter Credentials")
            self.add_customer_frame.pack(padx=10, pady=10, fill=tk.BOTH)
            tk.Label(self.add_customer_frame, text=" Username:").grid(row=0, column=0, padx=5, pady=5)
            self.username = tk.Entry(self.add_customer_frame)
            self.username.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(self.add_customer_frame, text=" Password:").grid(row=1, column=0, padx=5, pady=5)
            self.password = tk.Entry(self.add_customer_frame)
            self.password.grid(row=1, column=1, padx=5, pady=5)

            self.submit_button = tk.Button(self.add_customer_frame, text="Submit", command=(self.checkCredentials))
            self.submit_button.grid(row=5, columnspan=5, padx=5, pady=5)

        if self.credentials()==False:
            login()

        else:
            signup()
            
            
            
    def credentials(self):
        userfile = open("username.txt", 'r')
        username = userfile.read()
        userfile.close()
        if username == "":
            return True
        return False
        

    def setCredentials(self):

        username = self.username.get()
        password = self.password.get()
        userfile = open("username.txt", 'w')
        passfile = open("password.txt", 'w')
        # Enter the username into the userfile
        print("entered")
        userfile.write(username)

        # Hashing the password
        ciphertxt = ""
        for i in password:
            chng = ord(i)
            chng = chng + 1
            cipher = chr(chng)
            ciphertxt += cipher  # the 2nd alphabet to the respective alphabet is saved in the word file
        password = ciphertxt

        # Enter the hashed password into the File
        passfile.write(password)
        userfile.close()
        passfile.close()
        messagebox.showinfo("Success", "Admin Created.\nRestart to save changes")
            
        root.destroy()
            
        

    def checkCredentials(self):

        username = self.username.get()
        password = self.password.get()
        userfile = open("username.txt", 'r')
        passfile = open("password.txt", 'r')
        checkpassword=passfile.read()
        checkusername=userfile.read()

        str = ""

        # Decrpytiong the password
        for i in checkpassword:
            s = ord(i)
            s = s - 1
            i = chr(s)
            str = str + i
        checkpassword = str

        # checking the credentials
        if (username == checkusername and password == checkpassword):
            
            messagebox.showinfo("Success", "Login Successfull")
            custRoot=tk.Tk()
            CustomerApp(custRoot)
            root.destroy()
            
        else:
            messagebox.showerror("Error", "Incorrect Credentials")
            

    


class CustomerApp(DBinitiate):

    def __init__(self, root):

        DBinitiate.__init__(self)
        self.root = root
        self.root.title("Drug Management System")

        self.customerUI()

    def customerUI(self):

        tk.Label(self.root, text="CUSTOMER", font=("Arial", 14, "bold")).pack(pady=5)

        # Add Company
        self.add_customer_frame = tk.LabelFrame(self.root, text="Add Customer")
        self.add_customer_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        tk.Label(self.add_customer_frame, text="Customer Name:").grid(
            row=0, column=0, padx=5, pady=5)
        self.customerName = tk.Entry(self.add_customer_frame)
        self.customerName.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_customer_frame, text="Phone No:").grid(
            row=1, column=0, padx=5, pady=5)
        self.phone = tk.Entry(self.add_customer_frame)
        self.phone.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_customer_frame, text="Medicine Bought:").grid(
            row=2, column=0, padx=5, pady=5)
        self.medicineBought = tk.Entry(self.add_customer_frame)
        self.medicineBought.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.add_customer_frame, text="No. of Units bought :").grid(
            row=3, column=0, padx=5, pady=5)
        self.units = tk.Entry(self.add_customer_frame)
        self.units.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(
            self.add_customer_frame, text="Add", command=self.addCustomer)
        self.add_button.grid(row=5, columnspan=5, padx=5, pady=5)

        # search customer
        self.search_customer_frame = tk.LabelFrame(
            self.root, text="Search Customer")
        self.search_customer_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        tk.Label(self.search_customer_frame, text="Search Name:").grid(
            row=0, column=0, padx=5, pady=5)
        self.customerNameSearch = tk.Entry(self.search_customer_frame)
        self.customerNameSearch.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(
            self.search_customer_frame, text="Search", command=self.searchCustomer)
        self.search_button.grid(row=3, columnspan=5, padx=5, pady=5)

        self.details_text = tk.Text(
            self.search_customer_frame, height=5, width=50)
        self.details_text.grid(row=4, columnspan=5, padx=5, pady=5)

        # Delete Customer
        self.search_customer_frame = tk.LabelFrame(
            self.root, text="Delete Customer")
        self.search_customer_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        tk.Label(self.search_customer_frame, text="Delete Name:").grid(
            row=0, column=0, padx=5, pady=5)
        self.customerNameDelete = tk.Entry(self.search_customer_frame)
        self.customerNameDelete.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(
            self.search_customer_frame, text="Delete", command=self.deleteCustomer)
        self.delete_button.grid(row=2, columnspan=5, padx=5, pady=5)

        # Show All Data
        self.show_customer_frame = tk.LabelFrame(
            self.root, text="Show All Record")
        self.show_customer_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.search_button = tk.Button(
            self.show_customer_frame, text="Show All Record", command=self.showCustomer)
        self.search_button.grid(row=3, columnspan=2, padx=5, pady=5)

        self.show_details_text = tk.Text(
            self.show_customer_frame, height=10, width=50)
        self.show_details_text.grid(row=4, columnspan=5, padx=5, pady=5)

    def addCustomer(self):
        customerName = self.customerName.get()
        phone = self.phone.get()
        medicineBought = self.medicineBought.get()
        units = self.units.get()
        dates = str(date.today())

        try:
            query = "INSERT INTO customer (CName, date, medicine_sold, QTY, phone) VALUES (%s, %s, %s, %s, %s)"
            values = (customerName, dates, medicineBought, units, phone)
            self.mycursor.execute(query, values)
            self.mydb.commit()
            self.customerName.delete(0, 'end')
            self.medicineBought.delete(0, 'end')
            self.units.delete(0, 'end')
            self.phone.delete(0, 'end')
            messagebox.showinfo("Success", "Company Added Successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def searchCustomer(self):
        searchname = self.customerNameSearch.get()

        try:
            query = "SELECT * FROM customer WHERE CName = %s"
            self.mycursor.execute(query, (searchname,))
            details = self.mycursor.fetchall()
            if details:
                for i in range(0, len(details)):
                    self.details_text.delete("1.0", tk.END)
                    self.details_text.insert(tk.END, f"Customer Name: {details[i][0]}\n")
                    self.details_text.insert(tk.END, f"Date: {details[i][1]}\n")
                    self.details_text.insert(tk.END, f"Medicine Bought: {details[i][2]}\n")
                    self.details_text.insert(tk.END, f"Quantity: {details[i][3]}\n")
                    self.details_text.insert(tk.END, f"Phone Number: {details[i][4]}\n")
                self.customerNameSearch.delete(0, 'end')

            else:
                self.details_text.delete("1.0", tk.END)
                messagebox.showerror("Info", "Customer not found")

        except my.Error as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def deleteCustomer(self):
        deletename = self.customerNameDelete.get()
        try:
            query = "Delete from customer where CName=%s"
            self.mycursor.execute(query, (deletename,))
            self.mydb.commit()
            if (self.mycursor.rowcount == 0):

                messagebox.showerror("Error", "Customer not found")
            else:
                messagebox.showinfo("Info", "Customer deleted")

            self.customerNameDelete.delete(0, 'end')

        except my.Error as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def showCustomer(self):
        try:
            query = "SELECT * FROM customer"
            self.mycursor.execute(query)
            details = self.mycursor.fetchall()
            print(details)
            if details:
                self.show_details_text.delete("1.0", tk.END)
                for i in range(0, len(details)):

                    self.show_details_text.insert(
                        tk.END, f"Customer Name: {details[i][0]}\n")
                    self.show_details_text.insert(
                        tk.END, f"Date: {details[i][1]}\n")
                    self.show_details_text.insert(
                        tk.END, f"Medicine Bought: {details[i][2]}\n")
                    self.show_details_text.insert(
                        tk.END, f"Quantity: {details[i][3]}\n")
                    self.show_details_text.insert(
                        tk.END, f"Phone Number: {details[i][4]}\n\n")

            else:
                self.show_details_text.delete("1.0", tk.END)
                messagebox.showinfo("Info", "No Customer  found")

        except my.Error as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")


root = tk.Tk()
auth = authenticate(root)
# app=CustomerApp(root)

root.mainloop()
