import os

class log_export:
    def __init__(self):
        self.words = {
            "code_snippet": self.create_file_1111,
            "db_snippet": self.create_file_2222,
        }

    def get_code(self, word):
        func = self.words.get(word, None)
        if func:
            func()

    def create_file_1111(self):
        code = """
import tkinter as tk
from tkinter import messagebox, ttk
import pyodbc
import hashlib
import sys
from tkinter.messagebox import showerror


server = '192.168.1.233'
db = 'demo_wibe'
usname = 'admin'
uspsw = '123456'

#dbstring = f'DRIVER={{ODBC Driver 17 for SQL Server}};#             SERVER={server};DATABASE={db};#             UID={usname};PWD={uspsw}'

try:
    dbstring = ('DRIVER={SQL Server};SERVER=SIN2T\\SQLEXPRESS;DATABASE=DemoKino2;Trusted_Connection=yes;')
except Exception:
    showerror(title='Ошибка11', message='Нет соединения с базой данных. Работа приложения будет завершена.')
    sys.exit(1)

# Подключение к базе данных
def connect_db():
    conn = pyodbc.connect(
        dbstring)
    return conn

# Функция для хеширования пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Функция для выполнения SQL запросов
def execute_query(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Окно авторизации
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("200x200")
        
        self.label_login = tk.Label(root, text="Логин")
        self.label_login.pack()
        self.entry_login = tk.Entry(root)
        self.entry_login.pack()
        
        self.label_password = tk.Label(root, text="Пароль")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()
        
        self.login_button = tk.Button(root, text="Войти", command=self.login)
        self.login_button.pack()
        
        self.register_button = tk.Button(root, text="Зарегистрироваться", command=self.register)
        self.register_button.pack()
        
    def login(self):
        login = self.entry_login.get()
        password = hash_password(self.entry_password.get())
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, role_id FROM Users WHERE login=? AND password=?", (login, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            user_id, first_name, last_name, role_id = user
            self.root.destroy()
            main_window = tk.Tk()
            MainWindow(main_window, user_id, first_name, last_name, role_id)
        else:
            messagebox.showerror("Ошибка", "Неправильный логин или пароль")
    
    def register(self):
        self.root.destroy()
        register_window = tk.Tk()
        RegisterWindow(register_window)

# Окно регистрации
class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрация")
        self.root.geometry("200x300")
        
        self.label_first_name = tk.Label(root, text="Имя")
        self.label_first_name.pack()
        self.entry_first_name = tk.Entry(root)
        self.entry_first_name.pack()
        
        self.label_last_name = tk.Label(root, text="Фамилия")
        self.label_last_name.pack()
        self.entry_last_name = tk.Entry(root)
        self.entry_last_name.pack()
        
        self.label_phone = tk.Label(root, text="Телефон")
        self.label_phone.pack()
        self.entry_phone = tk.Entry(root)
        self.entry_phone.pack()
        
        self.label_login = tk.Label(root, text="Логин")
        self.label_login.pack()
        self.entry_login = tk.Entry(root)
        self.entry_login.pack()
        
        self.label_password = tk.Label(root, text="Пароль")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()
        
        self.register_button = tk.Button(root, text="Зарегистрироваться", command=self.register)
        self.register_button.pack()
    
    def register(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        phone = self.entry_phone.get()
        login = self.entry_login.get()
        password = hash_password(self.entry_password.get())
        
        execute_query(
            "INSERT INTO Users (login, first_name, last_name, phone_number, role_id, password) VALUES (?, ?, ?, ?, ?, ?)",
            (login, first_name, last_name, phone, 1, password)
        )
        
        messagebox.showinfo("Успех", "Регистрация прошла успешно")
        self.root.destroy()
        login_window = tk.Tk()
        LoginWindow(login_window)

# Главное окно
class MainWindow:
    def __init__(self, root, user_id, first_name, last_name, role_id):
        self.root = root
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.role_id = role_id
        self.root.title("Главное окно")
        self.root.minsize(300, 200)

        self.create_widgets()

    def create_widgets(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Добавляем меню "Заказ" и команды в зависимости от роли
        self.order_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Заказ", menu=self.order_menu)
        
        if self.role_id == 1:  # User
            self.order_menu.add_command(label="Создать", command=self.create_order)
            self.order_menu.add_command(label="Редактировать", command=self.edit_order)
        elif self.role_id == 2:  # Manager
            self.order_menu.add_command(label="Изменить приоритет", command=self.change_priority)
            self.order_menu.add_command(label="Выполнить", command=self.complete_order)
            self.order_menu.add_command(label="Отменить", command=self.cancel_order)

        # Добавляем меню "Сортировка" и команды
        self.sort_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Сортировка", menu=self.sort_menu)
        if self.role_id == 3:  # Admin
            self.sort_menu.add_command(label="По фамилии (А-Я)", command=self.sort_users_asc)
            self.sort_menu.add_command(label="По фамилии (Я-А)", command=self.sort_users_desc)
        else:
            self.sort_menu.add_command(label="Сначала новое", command=self.sort_orders_by_date_desc)
            self.sort_menu.add_command(label="Сначала старое", command=self.sort_orders_by_date_asc)
            self.sort_menu.add_command(label="Выполненные (сначала новые)", command=self.sort_orders_by_completed_desc)
            self.sort_menu.add_command(label="Отмененные (сначала новые)", command=self.sort_orders_by_cancelled_desc)

        # Теперь добавляем меню "Пользователь" в последнюю очередь
        self.settings_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Пользователь", menu=self.settings_menu)
        self.settings_menu.add_command(label="Сменить пользователя", command=self.change_user)
        self.settings_menu.add_command(label="Выход", command=self.exit)

        # Настраиваем основную часть окна в зависимости от роли пользователя
        if self.role_id == 3:  # Admin
            self.user_list_frame = tk.Frame(self.root)
            self.user_list_frame.pack(expand=True, fill='both')
            self.load_users()
        else:
            self.order_list_frame = tk.Frame(self.root)
            self.order_list_frame.pack(expand=True, fill='both')
            self.initialize_order_tree()
            self.load_orders()

        # Добавляем статусную строку внизу окна
        self.status_label = tk.Label(self.root, text=f"{self.first_name} {self.last_name} ({self.get_role_name(self.role_id)})")
        self.status_label.pack(side=tk.BOTTOM)


    def sort_users_asc(self):
        self.sort_users("ASC")

    def sort_users_desc(self):
        self.sort_users("DESC")

    def sort_users(self, order):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, login, first_name, last_name, phone_number, role_id FROM Users WHERE role_id != 3 ORDER BY last_name {order}")
        users = cursor.fetchall()
        conn.close()

        # Check if self.user_tree already exists
        if hasattr(self, 'user_tree'):
            # Clear the existing items
            for item in self.user_tree.get_children():
                self.user_tree.delete(item)
        else:
            # Create the user_tree only once
            self.user_tree = ttk.Treeview(self.user_list_frame, columns=("id", "login", "first_name", "last_name", "phone_number", "role"), show="headings")
            self.user_tree.heading("id", text="ID", anchor='center')
            self.user_tree.heading("login", text="Логин", anchor='center')
            self.user_tree.heading("first_name", text="Имя", anchor='center')
            self.user_tree.heading("last_name", text="Фамилия", anchor='center')
            self.user_tree.heading("phone_number", text="Телефон", anchor='center')
            self.user_tree.heading("role", text="Роль", anchor='center')

            self.user_tree.column("id", anchor='center')
            self.user_tree.column("login", anchor='center')
            self.user_tree.column("first_name", anchor='center')
            self.user_tree.column("last_name", anchor='center')
            self.user_tree.column("phone_number", anchor='center')
            self.user_tree.column("role", anchor='center')

            self.user_tree.pack(expand=True, fill='both')

            # Bind the double-click event for user selection
            self.user_tree.bind("<Double-1>", self.on_user_click)

        # Insert the new data
        for user in users:
            self.user_tree.insert("", "end", values=(user[0], user[1], user[2], user[3], user[4], self.get_role_name(user[5])))

    def sort_orders_by_date_asc(self):
        self.sort_orders_by_date("ASC")

    def sort_orders_by_date_desc(self):
        self.sort_orders_by_date("DESC")

    def sort_orders_by_date(self, order):
        conn = connect_db()
        cursor = conn.cursor()

        if self.role_id == 1:  # User
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE created_by_id=? AND status='создан' ORDER BY created_at {order}", (self.user_id,))
        elif self.role_id == 2:  # Manager
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE status NOT IN ('выполнен', 'отменен') ORDER BY created_at {order}")
        else:  # Admin
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders ORDER BY created_at {order}")

        orders = cursor.fetchall()
        conn.close()

        # Очищаем Treeview перед добавлением отсортированных заказов
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

        if orders:
            self.order_tree.pack(expand=True, fill='both')
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()

            for order in orders:
                self.order_tree.insert("", "end", values=[str(value).strip("(),'") for value in order])
        else:
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()
            self.no_orders_label = tk.Label(self.order_list_frame, text="Заказов пока нет")
            self.no_orders_label.pack(expand=True, fill='both')
            self.order_tree.pack_forget()  # Hide the empty Treeview


    def sort_orders_by_completed_desc(self):
        self.sort_orders_by_completed_date("DESC")

    def sort_orders_by_completed_date(self, order):
        conn = connect_db()
        cursor = conn.cursor()

        if self.role_id == 1:  # User
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE created_by_id=? AND status='выполнен' ORDER BY completed_at {order}", (self.user_id,))
        elif self.role_id == 2:  # Manager
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE status='выполнен' ORDER BY completed_at {order}")
        else:  # Admin
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE status='выполнен' ORDER BY completed_at {order}")

        orders = cursor.fetchall()
        conn.close()

        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

        if orders:
            self.order_tree.pack(expand=True, fill='both')
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()

            for order in orders:
                self.order_tree.insert("", "end", values=[str(value).strip("(),'") for value in order])
        else:
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()
            self.no_orders_label = tk.Label(self.order_list_frame, text="Заказов пока нет")
            self.no_orders_label.pack(expand=True, fill='both')
            self.order_tree.pack_forget()

    def sort_orders_by_cancelled_desc(self):
        self.sort_orders_by_cancelled_date("DESC")

    def sort_orders_by_cancelled_date(self, order):
        conn = connect_db()
        cursor = conn.cursor()

        if self.role_id == 1:  # User
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE created_by_id=? AND status='отменен' ORDER BY completed_at {order}", (self.user_id,))
        elif self.role_id == 2:  # Manager
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE status='отменен' ORDER BY completed_at {order}")
        else:  # Admin
            cursor.execute(
                f"SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                f"FROM Orders WHERE status='отменен' ORDER BY completed_at {order}")

        orders = cursor.fetchall()
        conn.close()

        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

        if orders:
            self.order_tree.pack(expand=True, fill='both')
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()

            for order in orders:
                self.order_tree.insert("", "end", values=[str(value).strip("(),'") for value in order])
        else:
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()
            self.no_orders_label = tk.Label(self.order_list_frame, text="Заказов пока нет")
            self.no_orders_label.pack(expand=True, fill='both')
            self.order_tree.pack_forget()    
        

    def sort_orders_by_completed_date(self, order):
        conn = connect_db()
        cursor = conn.cursor()

        if self.role_id == 1:  # User
            cursor.execute(
                "SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                "FROM Orders WHERE created_by_id=? AND status='выполнен' ORDER BY completed_at " + order, (self.user_id,))
        elif self.role_id == 2:  # Manager
            cursor.execute(
                "SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                "FROM Orders WHERE status='выполнен' ORDER BY completed_at " + order)
        else:  # Admin
            cursor.execute(
                "SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                "FROM Orders WHERE status='выполнен' ORDER BY completed_at " + order)

        orders = cursor.fetchall()
        conn.close()

        # Clear existing items in the order_tree
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

        if orders:
            self.order_tree.pack(expand=True, fill='both')
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()

            for order in orders:
                self.order_tree.insert("", "end", values=[str(value).strip("(),'") for value in order])
        else:
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()
            self.no_orders_label = tk.Label(self.order_list_frame, text="Заказов пока нет")
            self.no_orders_label.pack(expand=True, fill='both')
            self.order_tree.pack_forget()



    def initialize_order_tree(self):
        columns = ("id", "title", "description", "first_name", "last_name", "phone_number", "status", "created_at", "completed_at", "priority", "report")
        self.order_tree = ttk.Treeview(self.order_list_frame, columns=columns, show="headings")
        
        # Установка заголовков с выравниванием по центру
        self.order_tree.heading("id", text="ID", anchor='center')
        self.order_tree.heading("title", text="Название", anchor='center')
        self.order_tree.heading("description", text="Описание", anchor='center')
        self.order_tree.heading("first_name", text="Имя", anchor='center')
        self.order_tree.heading("last_name", text="Фамилия", anchor='center')
        self.order_tree.heading("phone_number", text="Телефон", anchor='center')
        self.order_tree.heading("status", text="Статус", anchor='center')
        self.order_tree.heading("created_at", text="Дата создания", anchor='center')
        self.order_tree.heading("completed_at", text="Дата выполнения", anchor='center')
        self.order_tree.heading("priority", text="Приоритет", anchor='center')
        self.order_tree.heading("report", text="Отчет", anchor='center')
        
        # Установка ширины столбцов и выравнивание данных по центру
        self.order_tree.column("id", width=50, anchor='center')
        self.order_tree.column("title", width=100, anchor='center')
        self.order_tree.column("description", anchor='center')
        self.order_tree.column("first_name", width=100, anchor='center')
        self.order_tree.column("last_name", width=100, anchor='center')
        self.order_tree.column("phone_number", width=100, anchor='center')
        self.order_tree.column("status",  width=70, anchor='center')
        self.order_tree.column("created_at", anchor='center')
        self.order_tree.column("completed_at", anchor='center')
        self.order_tree.column("priority", width=70, anchor='center')

        self.order_tree.column("report", anchor='center')
        
        self.order_tree.pack(expand=True, fill='both')
    
    def load_users(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, login, first_name, last_name, phone_number, role_id FROM Users WHERE role_id != 3")
        users = cursor.fetchall()
        conn.close()

        # Check if self.user_tree already exists
        if hasattr(self, 'user_tree'):
            # Clear the existing items
            for item in self.user_tree.get_children():
                self.user_tree.delete(item)
        else:
            # Create the user_tree only once
            self.user_tree = ttk.Treeview(self.user_list_frame, columns=("id", "login", "first_name", "last_name", "phone_number", "role"), show="headings")
            self.user_tree.heading("id", text="ID", anchor='center')
            self.user_tree.heading("login", text="Логин", anchor='center')
            self.user_tree.heading("first_name", text="Имя", anchor='center')
            self.user_tree.heading("last_name", text="Фамилия", anchor='center')
            self.user_tree.heading("phone_number", text="Телефон", anchor='center')
            self.user_tree.heading("role", text="Роль", anchor='center')
            
            self.user_tree.column("id", anchor='center')
            self.user_tree.column("login", anchor='center')
            self.user_tree.column("first_name", anchor='center')
            self.user_tree.column("last_name", anchor='center')
            self.user_tree.column("phone_number", anchor='center')
            self.user_tree.column("role", anchor='center')

            self.user_tree.pack(expand=True, fill='both')
            
            # Bind the double-click event for user selection
            self.user_tree.bind("<Double-1>", self.on_user_click)
        
        # Insert the new data
        for user in users:
            self.user_tree.insert("", "end", values=(user[0], user[1], user[2], user[3], user[4], self.get_role_name(user[5])))


    
    def load_orders(self):
        # Clear the old table content
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

        # Load new data
        conn = connect_db()
        cursor = conn.cursor()

        if self.role_id == 1:  # User
            cursor.execute(
                "SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                "FROM Orders WHERE created_by_id=? AND status='создан'", (self.user_id,))
        elif self.role_id == 2:  # Manager
            cursor.execute(
                "SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                "FROM Orders WHERE status NOT IN ('выполнен', 'отменен')")
        else:  # Admin
            cursor.execute(
                "SELECT id, title, description, first_name, last_name, phone_number, status, created_at, completed_at, priority, report "
                "FROM Orders")

        orders = cursor.fetchall()
        conn.close()

        if orders:
            self.order_tree.pack(expand=True, fill='both')
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()

            for order in orders:
                self.order_tree.insert("", "end", values=[str(value).strip("(),'") for value in order])
        else:
            if hasattr(self, 'no_orders_label'):
                self.no_orders_label.pack_forget()
            self.no_orders_label = tk.Label(self.order_list_frame, text="Заказов пока нет")
            self.no_orders_label.pack(expand=True, fill='both')
            self.order_tree.pack_forget()  # Hide the empty Treeview




    def create_order(self):
        CreateOrderWindow(self.root, self.user_id, self)
        self.load_orders()  # Refresh the table after creating an order

    def change_priority(self):
        selected_order = self.get_selected_order()
        if selected_order:
            ChangePriorityWindow(self.root, self, selected_order)
            self.load_orders()  # Refresh the table after changing the priority
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите заказ для изменения приоритета.")
    

    def edit_order(self):
        selected_order = self.get_selected_order()
        if selected_order:
            EditOrderWindow(self.root, self, selected_order)
            self.load_orders() # Refresh the table after editing an order
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите заказ для редактирования.")

    def complete_order(self):
        selected_order = self.get_selected_order()
        if selected_order:
            ReportWindow(self.root, self, selected_order, 'выполнен')
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите заказ для выполнения.")

    def cancel_order(self):
        selected_order = self.get_selected_order()
        if selected_order:
            ReportWindow(self.root, self, selected_order, 'отменен')
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите заказ для отмены.")
    
    def get_selected_order(self):
        selected_item = self.order_tree.selection()
        if selected_item:
            return self.order_tree.item(selected_item, "values")
        return None

    def get_selected_user(self):
        selected_item = self.user_tree.selection()
        if selected_item:
            return self.user_tree.item(selected_item, "values")
        return None
    
    def get_role_name(self, role_id):
        roles = {1: "user", 2: "manager", 3: "admin"}
        return roles.get(role_id, "unknown")

    def change_user(self):
        self.root.destroy()
        login_window = tk.Tk()
        LoginWindow(login_window)
    
    def exit(self):
        self.root.destroy()
    
    def on_user_click(self, event):
        selected_user = self.get_selected_user()
        if selected_user:
            user_id = selected_user[0]
            UserDetailWindow(self.root, self, user_id) 

class ChangePriorityWindow:
    def __init__(self, parent, main_window, selected_order):
        self.top = tk.Toplevel(parent)
        self.top.title("Изменить приоритет")
        self.top.geometry("300x150")

        self.main_window = main_window  # Сохраняем ссылку на MainWindow
        self.selected_order = selected_order

        self.label_priority = tk.Label(self.top, text="Выберите новый приоритет")
        self.label_priority.pack()

        self.priority_var = tk.StringVar()
        self.priority_combobox = ttk.Combobox(self.top, textvariable=self.priority_var)
        self.priority_combobox['values'] = ('обычный', 'средний', 'высокий')
        self.priority_combobox.current(0)
        self.priority_combobox.pack()

        self.submit_button = tk.Button(self.top, text="Изменить", command=self.change_priority)
        self.submit_button.pack()

    def change_priority(self):
        new_priority = self.priority_var.get()
        order_id = self.selected_order[0]

        query = f'UPDATE Orders SET priority = ? WHERE id = ?'

        params = (new_priority, order_id)
        execute_query(query, params)

        messagebox.showinfo("Успех", "Приоритет заказа успешно изменен.")
        self.top.destroy()
        self.main_window.load_orders()  # Обновляем таблицу заказов

        
class ReportWindow:
    def __init__(self, parent, main_window, order, status):
        self.top = tk.Toplevel(parent)
        self.top.title("Отчет по заказу")
        self.top.geometry("300x200")
        self.main_window = main_window  # Ссылка на главное окно
        self.order_id = order[0]
        self.status = status

        self.label = tk.Label(self.top, text="Отчет о проделанной работе:")
        self.label.pack(pady=10)
        
        self.text_report = tk.Text(self.top, height=5, width=40)
        self.text_report.pack(pady=10)
        
        self.submit_button = tk.Button(self.top, text="Сохранить", command=self.save_report)
        self.submit_button.pack(pady=10)

    def save_report(self):
        report = self.text_report.get("1.0", tk.END).strip()

        if report:
            execute_query(
                "UPDATE Orders SET status=?, completed_by_id=?, completed_at=GETDATE(), report=? WHERE id=?", 
                (self.status, self.main_window.user_id, report, self.order_id)
            )
            self.main_window.load_orders()  # Обновить список заказов
            self.top.destroy()
            messagebox.showinfo("Успех", f"Заказ успешно {self.status}")
        else:
            messagebox.showwarning("Предупреждение", "Отчет не может быть пустым.")

class CreateOrderWindow:
    def __init__(self, parent, user_id, main_window):
        self.top = tk.Toplevel(parent)
        self.top.title("Создать заказ")
        self.top.geometry("300x150")
        self.main_window = main_window  # Сохраняем ссылку на MainWindow

        self.label_title = tk.Label(self.top, text="Название")
        self.label_title.pack()
        self.entry_title = tk.Entry(self.top)
        self.entry_title.pack()
        
        self.label_description = tk.Label(self.top, text="Описание")
        self.label_description.pack()
        self.entry_description = tk.Entry(self.top)
        self.entry_description.pack()
        
        self.submit_button = tk.Button(self.top, text="Создать", command=lambda: self.create_order(user_id))
        self.submit_button.pack()
    
    def create_order(self, user_id):
        title = self.entry_title.get()
        description = self.entry_description.get()
        
        # Получаем информацию о пользователе
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, phone_number FROM Users WHERE id=?", (user_id,))
        user = cursor.fetchone()
        conn.close()

        if user:
            first_name, last_name, phone_number = user
            priority = 'обычный'  # Устанавливаем приоритет по умолчанию

            # Вставляем новый заказ с приоритетом
            execute_query(
                "INSERT INTO Orders (title, description, first_name, last_name, phone_number, status, created_by_id, priority) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (title, description, first_name, last_name, phone_number, 'создан', user_id, priority)
            )

            self.top.destroy()  # Закрываем окно создания заказа

            # Удаляем метку "Заказов пока нет", если она существует
            if hasattr(self.main_window, 'no_orders_label'):
                self.main_window.no_orders_label.pack_forget()

            self.main_window.load_orders()  # Обновляем таблицу заказов через ссылку на MainWindow
            messagebox.showinfo("Успех", "Заказ успешно создан")
        else:
            messagebox.showerror("Ошибка", "Пользователь не найден")



class EditOrderWindow:
    def __init__(self, parent, main_window, order):
        self.top = tk.Toplevel(parent)
        self.top.title("Редактировать заказ")
        self.top.geometry("300x150")
        
        self.main_window = main_window  # Store reference to MainWindow instance
        self.order_id = order[0]

        self.label_title = tk.Label(self.top, text="Название")
        self.label_title.pack()
        self.entry_title = tk.Entry(self.top)
        self.entry_title.insert(0, order[1])
        self.entry_title.pack()

        self.label_description = tk.Label(self.top, text="Описание")
        self.label_description.pack()
        self.entry_description = tk.Entry(self.top)
        self.entry_description.insert(0, order[2])
        self.entry_description.pack()

        self.submit_button = tk.Button(self.top, text="Сохранить", command=self.edit_order)
        self.submit_button.pack()

    def edit_order(self):
        title = self.entry_title.get()
        description = self.entry_description.get()

        execute_query(
            "UPDATE Orders SET title=?, description=? WHERE id=?",
            (title, description, self.order_id)
        )

        messagebox.showinfo("Успех", "Заказ успешно обновлен")
        self.top.destroy()
        self.main_window.load_orders()  # Call load_orders() on the main window after editing


class UserDetailWindow:
    def __init__(self, parent, main_window, user_id):
        self.parent = parent
        self.main_window = main_window
        self.user_id = user_id

        self.top = tk.Toplevel(parent)
        self.top.title("Детали пользователя")
        self.top.geometry("300x200")

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, login, first_name, last_name, phone_number, role_id FROM Users WHERE id=?", (user_id,))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.user_id = user[0]
            login, first_name, last_name, phone_number, role_id = user[1:]

            tk.Label(self.top, text=f"ID: {self.user_id}").pack()
            tk.Label(self.top, text=f"Логин: {login}").pack()
            tk.Label(self.top, text=f"Имя: {first_name}").pack()
            tk.Label(self.top, text=f"Фамилия: {last_name}").pack()
            tk.Label(self.top, text=f"Телефон: {phone_number}").pack()

            tk.Label(self.top, text="Роль").pack()
            self.role_var = tk.StringVar(value=self.get_role_name(role_id))
            self.role_combobox = ttk.Combobox(self.top, textvariable=self.role_var, values=["user", "manager"])
            self.role_combobox.pack()

            tk.Button(self.top, text="Сохранить", command=self.update_role).pack()

    def get_role_name(self, role_id):
        roles = {1: "user", 2: "manager", 3: "admin"}
        return roles.get(role_id, "unknown")

    def update_role(self):
        new_role = self.role_var.get()
        role_id = 1 if new_role == "user" else 2 if new_role == "manager" else None

        if role_id:
            execute_query("UPDATE Users SET role_id=? WHERE id=?", (role_id, self.user_id))
            messagebox.showinfo("Успех", "Роль успешно обновлена")
            self.top.destroy()
            self.main_window.load_users()  # Refresh user list in MainWindow
        else:
            messagebox.showerror("Ошибка", "Недопустимая роль")


# Запуск программы
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
"""
        with open(os.path.join(os.getcwd(), 'code_snippet.txt'), 'w') as f:
            f.write(code)

    def create_file_2222(self):
        code = """
-- Создание таблицы Roles
CREATE TABLE Roles (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Создание таблицы Users
CREATE TABLE Users (
    id INT IDENTITY PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50),
    role_id INT NOT NULL,
    password VARCHAR(64) NOT NULL,
    FOREIGN KEY (role_id) REFERENCES Roles(id)
);

-- Создание таблицы Orders
CREATE TABLE Orders (
    id INT IDENTITY PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    description VARCHAR(250),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    priority VARCHAR(50), -- Новое поле "приоритет"
    created_by_id INT NOT NULL,
    created_at DATETIME DEFAULT GETDATE(),
    completed_by_id INT,
    completed_at DATETIME,
    report VARCHAR(250), -- Поле "report(250)"
    FOREIGN KEY (created_by_id) REFERENCES Users(id),
    FOREIGN KEY (completed_by_id) REFERENCES Users(id)
);


-- Заполнение таблицы Roles
INSERT INTO Roles (name)
VALUES 
('user'),
('manager'),
('admin');
"""
        with open(os.path.join(os.getcwd(), 'db_snippet.txt'), 'w') as f:
            f.write(code)

# Пример использования
log = log_export()
log.get_code("code_snippet")  # Создаст файл LogExport.txt с содержимым 1111
log.get_code("db_snippet")    # Создаст файл AnotherExport.txt с содержимым 2222
