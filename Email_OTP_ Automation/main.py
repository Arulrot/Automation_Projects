import tkinter as tk
from tkinter import messagebox
import random
import smtplib
import csv
import webbrowser


root = tk.Tk()
root.title("Registration System")
root.geometry("800x600")  
root.configure(bg="#f0f8ff")  

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
department_var = tk.StringVar()
otp = None

def create_registration_page():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#f0f8ff")

    tk.Label(root, text="Registration Page", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#333333").pack(pady=20)

    tk.Label(root, text="Name :", font=("Arial", 14), bg="#f0f8ff", fg="#333333").pack(pady=5)
    tk.Entry(root, textvariable=name_var, font=("Arial", 14)).pack(pady=5)

    tk.Label(root, text="Email ID:", font=("Arial", 14), bg="#f0f8ff", fg="#333333").pack(pady=5)
    tk.Entry(root, textvariable=email_var, font=("Arial", 14)).pack(pady=5)

    tk.Label(root, text="Phone Number:", font=("Arial", 14), bg="#f0f8ff", fg="#333333").pack(pady=5)
    tk.Entry(root, textvariable=phone_var, font=("Arial", 14)).pack(pady=5)

    tk.Label(root, text="Department:", font=("Arial", 14), bg="#f0f8ff", fg="#333333").pack(pady=5)
    tk.Entry(root, textvariable=department_var, font=("Arial", 14)).pack(pady=5)

    tk.Button(root, text="Submit", font=("Arial", 14), bg="#4caf50", fg="white", command=submit_details).pack(pady=20)

    tk.Label(root, text="Developed by ArulMohan", font=("Arial", 10), bg="#f0f8ff", fg="#333333").place(relx=1.0, rely=1.0, anchor="se")

    tk.Button(root, text="Contact", font=("Arial", 10), bg="#4caf50", fg="white", command=open_linkedin).place(relx=1.0, rely=0.0, anchor="ne")


def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/arulmohanp27/")

def submit_details():
    if not name_var.get() or not email_var.get() or not phone_var.get() or not department_var.get():
        messagebox.showerror("Error", "All fields are required!")
    else:
        global otp
        otp = str(random.randint(1000, 9999))
        print(f"Generated OTP: {otp}")
        send_mail(otp)

def send_mail(otp):
    smtp_server="smtp.gmail.com"
    smtp_port=587
    sender_email="Your Email "
    sender_password="Your Email Password "
    reciver_email=email_var.get()

    subject="OTP VERIFICATION MAIL"
    body=f"The One Time Password For the Signup Is {otp}"
    message=f"subject: {subject}\n\n{body}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print("Connecting to SMTP server...")
        server.login(sender_email, sender_password)
        print("Logged in successfully.")
        server.sendmail(sender_email, reciver_email, message)
        print("Email sent successfully.")
        create_otp_page()

    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", "Email Processing Failed")
    finally:
        if server:
            server.quit()

def create_otp_page():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#fffacd")

    otp_var = tk.StringVar()

    tk.Label(root, text="OTP Verification", font=("Arial", 24, "bold"), bg="#fffacd", fg="#333333").pack(pady=20)
    tk.Label(root, text=f"Enter the OTP sent to your email {email_var.get()}:", font=("Arial", 14), bg="#fffacd", fg="#333333").pack(pady=10)
    tk.Entry(root, textvariable=otp_var, font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Verify", font=("Arial", 14), bg="#4caf50", fg="white", command=lambda: verify_otp(otp_var)).pack(pady=20)
    

def verify_otp(otp_var):
    if otp_var.get() == otp:
        messagebox.showinfo("Success", "OTP Verified Successfully!")
        database()
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")

def database():
    data=[name_var.get(),email_var.get(),phone_var.get(),department_var.get()]
    with open("Customer_data.csv",mode='+a',newline='') as file:
         writer=csv.writer(file)
         writer.writerow(data)
         print("Data stored successfully")
         create_welcome_page()

def create_welcome_page():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#e6ffe6")

    tk.Label(root, text="Welcome!", font=("Arial", 24, "bold"), bg="#e6ffe6", fg="#333333").pack(pady=20)

    tk.Label(root, text="Thank You", font=("Arial", 16), bg="#e6ffe6", fg="#333333").pack(pady=20)

create_registration_page()

root.state("zoomed")
root.mainloop()
