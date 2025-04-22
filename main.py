import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from tools.port_scanner import port_scanner
from tools.ping_tool import ping_tool

# إعداد قاعدة البيانات
def create_db():
    if not os.path.exists('users.db'):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                     (username TEXT, password TEXT)''')
        c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
        conn.commit()
        conn.close()

# واجهة تسجيل الدخول
def login_window():
    def authenticate():
        username = entry_username.get()
        password = entry_password.get()

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Success", "تم تسجيل الدخول بنجاح!")
            open_dashboard()
        else:
            messagebox.showerror("Error", "اسم المستخدم أو كلمة المرور غير صحيحة!")

    login = tk.Tk()
    login.title("تسجيل الدخول")

    tk.Label(login, text="اسم المستخدم:").grid(row=0, column=0)
    entry_username = tk.Entry(login)
    entry_username.grid(row=0, column=1)

    tk.Label(login, text="كلمة المرور:").grid(row=1, column=0)
    entry_password = tk.Entry(login, show="*")
    entry_password.grid(row=1, column=1)

    login_button = tk.Button(login, text="دخول", command=authenticate)
    login_button.grid(row=2, column=1)

    login.mainloop()

# واجهة لوحة تحكم الأدمن
def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("لوحة تحكم الأدمن")

    tk.Button(dashboard, text="فحص البورتات", command=port_scanner).pack()
    tk.Button(dashboard, text="أداة Ping", command=ping_tool).pack()

    dashboard.mainloop()

# بداية تشغيل البرنامج
if __name__ == "__main__":
    create_db()  # إنشاء قاعدة البيانات إذا لم تكن موجودة
    login_window()  # فتح نافذة تسجيل الدخول
