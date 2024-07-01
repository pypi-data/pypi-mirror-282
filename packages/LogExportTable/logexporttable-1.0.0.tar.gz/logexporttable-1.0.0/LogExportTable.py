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
import pyodbc
import os.path
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
import sys

server = '192.168.1.233'
db = 'demo_wibe'
usname = 'admin'
uspsw = '123456'
app = Tk()

#dbstring = f'DRIVER={{ODBC Driver 17 for SQL Server}};#             SERVER={server};DATABASE={db};#             UID={usname};PWD={uspsw}'

try:
    dbstring = ('DRIVER={SQL Server};SERVER=SIN2T\SQLEXPRESS;DATABASE=DemoPy2;Trusted_Connection=yes;')
except Exception:
    showerror(title='Ошибка11', message='Нет соединения с базой данных. Работа приложения будет завершена.')
    sys.exit(1)

where = ''
orderby = 'ORDER BY name'
query = f'SELECT Product.id, Product.art, Product.name, Unit.name AS unit_name, Product.price, Product.price*(100-Product.discount)/100 AS NewPrice, Product.max_discount, Prod.name AS prod_name, Provider.name AS provider_name, Category.name AS category_name, Product.discount, Product.amount, Product.description, Product.image FROM Product INNER JOIN Unit ON Product.unit_id = Unit.unit_id INNER JOIN Prod ON Product.prod_id = Prod.prod_id INNER JOIN Provider ON Product.provider_id = Provider.provider_id INNER JOIN Category ON Product.category_id = Category.category_id'
new_query = f'{query} {where} {orderby}'
record = []
lbl_find_val = ['Найдено товаров', '', 'из', '']
try:
    conn = pyodbc.connect(dbstring)
except Exception:
    showerror('Ошибка подключения 1', 'Не удалось подключиться к базе данных, проверьте соединение')

def data():
    global record
    record = []
    try:
        cursor = conn.cursor()
        cursor.execute(new_query)
        for row in cursor.fetchall():
            image = row.image if row.image else 'picture.png'
            if not os.path.exists(row.image):
                image = 'picture.png'
            img1 = Image.open(image).resize((45, 45))
            img = ImageTk.PhotoImage(img1)
            tag = 'sale' if row.max_discount > 15 else 'blank'
            
            # Округляем цену со скидкой до 2 знаков после запятой
            new_price = f"{row.NewPrice:.2f}"
            
            # Если есть скидка, зачеркиваем оригинальную цену
            if row.discount > 0:
                price = ''.join([u'обр слеш u0335{}'.format(c) for c in str(row.price)])
            else:
                price = row.price
            
            line = [img, (row.id, row.art, row.name, row.unit_name,
                          price, new_price, row.max_discount,
                          row.prod_name, row.provider_name, row.category_name,
                          row.discount, row.amount, row.description), tag]
            record.append(line)
    except Exception as e:
        showerror('Сбой подключения 2', 'Отсутствует подключение к базе данных, проверьте соединение\n\n' + str(e))
    return record


def get_units():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT unit_id, name FROM Unit")
        return cursor.fetchall()
    except Exception as e:
        showerror('Ошибка', 'Не удалось загрузить данные единиц измерения\n\n' + str(e))
        return []

def get_prods():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT prod_id, name FROM Prod")
        return cursor.fetchall()
    except Exception as e:
        showerror('Ошибка', 'Не удалось загрузить данные производителей\n\n' + str(e))
        return []

def get_providers():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT provider_id, name FROM Provider")
        return cursor.fetchall()
    except Exception as e:
        showerror('Ошибка', 'Не удалось загрузить данные поставщиков\n\n' + str(e))
        return []

def get_categories():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT category_id, name FROM Category")
        return cursor.fetchall()
    except Exception as e:
        showerror('Ошибка', 'Не удалось загрузить данные категорий\n\n' + str(e))
        return []


def tree_fill():
    for i in data_tree.get_children():
        data_tree.delete(i)
    for row in data():
        data_tree.insert('', END, open=True, text='',
                         image=row[0], values=row[1], tag=row[2])

def go_status():
    global where
    global lbl_find_val
    global lbl_find
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT COUNT(*) FROM Product {where}')
        lbl_find_val[1] = str(cursor.fetchone()[0])
        if lbl_find_val[1] == '0':
            showinfo(title='Информация', message='Товаров не найдено')
        cursor.execute('SELECT COUNT(*) FROM Product ')
        lbl_find_val[3] = str(cursor.fetchone()[0])
        lbl_find.config(text=' '.join(lbl_find_val))
    except Exception:
        showerror(title='Ошибка 3', message='Нет соединения с базой данных')

def go_sort(event):
    global orderby
    global new_query
    select = cb_sort.get()
    if select == 'По возрастанию':
        orderby = 'ORDER BY price'
    elif select == 'По убыванию':
        orderby = 'ORDER BY price DESC'
    else:
        orderby = 'ORDER BY name'
    new_query = f'{query} {where} {orderby}'
    tree_fill()

def go_filtr(event):
    global orderby
    global where
    global query
    global new_query
    select = cb_filtr.get()
    if select == 'Менее 10%':
        where = 'WHERE discount<10'
    elif select == 'От 10 до 15%':
        where = 'WHERE discount>=10 and discount<15'
    elif select == '15% и более':
        where = 'WHERE discount>=15'
    else:
        where = ''
    new_query = f'{query} {where} {orderby}'
    tree_fill()
    go_status()

def register_user():
    global reg_window
    # Открываем окно регистрации
    reg_window = Toplevel(app)
    reg_window.title('Регистрация')
    reg_window.geometry('400x300')

    # Создаем поля ввода
    username_label = Label(reg_window, text='Имя пользователя:')
    username_entry = Entry(reg_window)
    password_label = Label(reg_window, text='Пароль:')
    password_entry = Entry(reg_window, show='*')
    email_label = Label(reg_window, text='Электронная почта:')
    email_entry = Entry(reg_window)

    # Размещаем поля ввода на окне
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    email_label.pack()
    email_entry.pack()

    # Создаем кнопку регистрации
    reg_button = Button(reg_window, text='Зарегистрироваться', command=lambda: register(username_entry.get(), password_entry.get(), email_entry.get()))
    reg_button.pack()

def register(username, password, email):
    # Проверяем, что все поля заполнены
    if not username or not password or not email:
        showerror(title='Ошибка', message='Все поля должны быть заполнены')
        return

    # Проверяем, что пользователь с таким именем еще не существует
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result:
        showerror(title='Ошибка', message='Пользователь с таким именем уже существует')
        return

    # Добавляем нового пользователя в базу данных
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, password, email, role_id) VALUES (?, ?, ?, ?)", (username, password, email, 2))
    conn.commit()

    # Выводим сообщение об успешной регистрации
    showinfo(title='Успех', message='Вы успешно зарегистрировались!')
    reg_window.withdraw()
    reg_window.deiconify()

def login():
    # Открываем окно входа
    global login_window
    login_window = Toplevel()
    login_window.title('Вход')
    login_window.geometry('300x200')

    # Создаем поля ввода
    username_label = Label(login_window, text='Имя пользователя:')
    username_entry = Entry(login_window)
    password_label = Label(login_window, text='Пароль:')
    password_entry = Entry(login_window, show='*')

    # Размещаем поля ввода на окне
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()

    # Создаем кнопку входа
    login_button = Button(login_window, text='Войти', command=lambda: check_password(username_entry.get(), password_entry.get()))
    register_button = Button(login_window, text='Регистрация', command=lambda: register_user())
    login_button.pack()
    register_button.pack()

    app.withdraw()
    login_window.mainloop()

def check_password(username, password):
    global app
    # Получаем пароль и роль пользователя из базы данных
    cursor = conn.cursor()
    cursor.execute(f' SELECT u.password, r.name AS role FROM Users u INNER JOIN Roles r ON u.role_id = r.id WHERE u.username = ?', (username,))
    result = cursor.fetchone()

    # Проверяем пароль и роль пользователя
    if result and password == result[0]:
        global user_role
        user_role = result[1]
        showinfo(title='Успех', message='Вы вошли в систему!')
        # Настраиваем основное окно приложения
        app.title('Магазин')
        app.geometry('1200x600')
        # Обновляем текст виджета Label в главном окне
        welcome_label.config(text=f'Вы вошли как {username} ({user_role})')
        # Скрываем окно входа
        login_window.withdraw()
        # Обновляем меню в основном окне
        update_menu()
        # Отображаем основное окно приложения
        app.deiconify()
        # Запускаем главный цикл приложения
        app.mainloop()
    else:
        showerror(title='Ошибка', message='Неверное имя пользователя или пароль')

def add_product():
    if user_role == 'Admin':
        add_window = Toplevel(app)
        add_window.title('Добавление товара')
        add_window.geometry('400x600')

        # Создаем поля ввода
        art_label = Label(add_window, text='Артикул:')
        art_entry = Entry(add_window)
        name_label = Label(add_window, text='Наименование:')
        name_entry = Entry(add_window)

        # Выпадающий список для единицы измерения
        unit_label = Label(add_window, text='Единица измерения:')
        units = get_units()
        unit_values = [f"{unit_id} - {unit_name}" for unit_id, unit_name in units]
        unit_combobox = ttk.Combobox(add_window, values=unit_values, state='readonly')

        # Выпадающий список для производителя
        prod_label = Label(add_window, text='Производитель:')
        prods = get_prods()
        prod_values = [f"{prod_id} - {prod_name}" for prod_id, prod_name in prods]
        prod_combobox = ttk.Combobox(add_window, values=prod_values, state='readonly')

        # Выпадающий список для поставщика
        provider_label = Label(add_window, text='Поставщик:')
        providers = get_providers()
        provider_values = [f"{provider_id} - {provider_name}" for provider_id, provider_name in providers]
        provider_combobox = ttk.Combobox(add_window, values=provider_values, state='readonly')

        # Выпадающий список для категории
        category_label = Label(add_window, text='Категория:')
        categories = get_categories()
        category_values = [f"{category_id} - {category_name}" for category_id, category_name in categories]
        category_combobox = ttk.Combobox(add_window, values=category_values, state='readonly')

        price_label = Label(add_window, text='Цена:')
        price_entry = Entry(add_window)
        max_discount_label = Label(add_window, text='Максимальная скидка:')
        max_discount_entry = Entry(add_window)
        discount_label = Label(add_window, text='Скидка:')
        discount_entry = Entry(add_window)
        amount_label = Label(add_window, text='Количество:')
        amount_entry = Entry(add_window)
        description_label = Label(add_window, text='Описание:')
        description_entry = Entry(add_window)
        image_label = Label(add_window, text='Изображение:')
        image_entry = Entry(add_window)

        # Размещаем поля ввода на окне
        art_label.pack()
        art_entry.pack()
        name_label.pack()
        name_entry.pack()
        unit_label.pack()
        unit_combobox.pack()
        prod_label.pack()
        prod_combobox.pack()
        provider_label.pack()
        provider_combobox.pack()
        category_label.pack()
        category_combobox.pack()
        price_label.pack()
        price_entry.pack()
        max_discount_label.pack()
        max_discount_entry.pack()
        discount_label.pack()
        discount_entry.pack()
        amount_label.pack()
        amount_entry.pack()
        description_label.pack()
        description_entry.pack()
        image_label.pack()
        image_entry.pack()

        # Создаем кнопку добавления товара
        add_button = Button(add_window, text='Добавить товар', command=lambda: add(art_entry.get(), name_entry.get(), unit_combobox.get(), price_entry.get(), max_discount_entry.get(), prod_combobox.get(), provider_combobox.get(), category_combobox.get(), discount_entry.get(), amount_entry.get(), description_entry.get(), image_entry.get()))
        add_button.pack()

def add(art, name, unit, price, max_discount, prod, provider, category, discount, amount, description, image):
    if user_role == 'Admin':
        # Извлекаем ID из выбранных значений в выпадающих списках
        unit_id = int(unit.split(' - ')[0])
        prod_id = int(prod.split(' - ')[0])
        provider_id = int(provider.split(' - ')[0])
        category_id = int(category.split(' - ')[0])

        try:
            cursor = conn.cursor()
            cursor.execute(f'INSERT INTO Product (art, name, unit_id, price, max_discount, prod_id, provider_id, category_id, discount, amount, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            , (art, name, unit_id, price, max_discount, prod_id, provider_id, category_id, discount, amount, description, image))
            conn.commit()

            # Выводим сообщение об успешном добавлении товара
            showinfo(title='Успех', message='Товар успешно добавлен!')
            # Обновляем таблицу товаров
            tree_fill()
        except Exception as e:
            showerror('Ошибка', 'Не удалось добавить товар\n\n' + str(e))
    else:
        showerror(title='Ошибка', message='У вас нет прав для добавления товаров')


def delete_product():
    # Проверяем роль пользователя
    if user_role == 'Admin':
        # Получаем выбранную строку из таблицы товаров
        selected_item = data_tree.selection()
        if not selected_item:
            showerror(title='Ошибка', message='Не выбрана строка для удаления')
            return
        selected_id = data_tree.item(selected_item)['values'][0]  # Теперь здесь будет использоваться первый элемент кортежа

        # Проверяем, что выбранный идентификатор является целым числом
        selected_id = int(selected_id)

        # Проверяем, что выбранный элемент существует в таблице товаров
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product WHERE id=?", (selected_id,))
        row = cursor.fetchone()
        if not row:
            showerror(title='Ошибка', message='Не существует товара с таким идентификатором')
            return

        # Подтверждение удаления
        confirm = askyesno(title='Подтверждение удаления', message='Вы уверены, что хотите удалить этот товар?')
        if not confirm:
            return

        # Удаляем товар из базы данных
        cursor.execute("DELETE FROM Product WHERE id=?", (selected_id,))
        conn.commit()

        # Обновляем таблицу товаров
        tree_fill()
    else:
        showerror(title='Ошибка', message='У вас нет прав для удаления товаров')



# Создаем меню
menu = Menu(app)
app.config(menu=menu)

# Создаем пункты меню
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="Выход", command=app.quit)
menu.add_cascade(label="Файл", menu=file_menu)

edit_menu = Menu(menu, tearoff=0)
edit_menu.add_command(label="Добавить товар", command=add_product)
edit_menu.add_command(label="Удалить товар", command=delete_product)
menu.add_cascade(label="Правка", menu=edit_menu)

user_menu = Menu(menu, tearoff=0)
user_menu.add_command(label="Сменить пользователя", command=login)
menu.add_cascade(label="Пользователь", menu=user_menu)

# Создаем фреймы для комбобоксов, лэйбла и дерева
cb_frame = Frame(app)
lbl_frame = Frame(app)
tree_frame = Frame(app)

# Добавляем комбобоксы
lbl_sort = Label(cb_frame, text='Сортировать ')
cb_sort_val = ['Без сортировки', 'По возрастанию',
               'По убыванию']
cb_sort = ttk.Combobox(cb_frame, values=cb_sort_val,
                       state='readonly')
lbl_filtr = Label(cb_frame, text='Фильтровать ')
cb_filtr_val = ['Без фильтрации', 'Менее 10%',
               'От 10 до 15%', '15% и более']
cb_filtr = ttk.Combobox(cb_frame, values=cb_filtr_val,
                       state='readonly')

# Привязка комбобоксов к функциям
cb_sort.bind("<<ComboboxSelected>>", go_sort)
cb_filtr.bind("<<ComboboxSelected>>", go_filtr)

# Публикуем комбобоксы таблицей
lbl_sort.grid(column=0, row=0)
cb_sort.grid(column=1, row=0)
lbl_filtr.grid(column=2, row=0)
cb_filtr.grid(column=3, row=0)

# Добавляем лэйбл найдено товаров и сразу публикуем
lbl_find = Label(lbl_frame, text=' '.join(lbl_find_val))
lbl_find.pack()

# Добавляем дерево
tree = [
    ['#0', 'Картинка', 'center', 50, 0],
    ['#1', 'ID', 'center', 50, 1],  # Новый элемент для столбца 'ID'
    ['#2', 'Артикул', 'center', 60, 2],
    ['#3', 'Наименование', 'center', 150, 3],
    ['#4', 'Ед.изм.', 'center', 50, 4],
    ['#5', 'Цена', 'center', 70, 5],
    ['#6', 'Со скидкой', 'center', 70, 6],
    ['#7', 'Макс.скидка', 'center', 70, 7],
    ['#8', 'Производитель', 'center', 80, 8],
    ['#9', 'Поставщик', 'center', 120, 9],
    ['#10', 'Категория', 'center', 120, 10],
    ['#11', 'Скидка', 'center', 50, 11],
    ['#12', 'Кол-во', 'center', 50, 12],
    ['#13', 'Описание', 'center', 200, 13]
]
columns = [k[0] for k in tree]  # Теперь здесь будет включен столбец 'ID'
style = ttk.Style()
style.configure('data.Treeview', rowheight=50)
data_tree = ttk.Treeview(tree_frame, columns=columns[1:],
                         style='data.Treeview')
data_tree.tag_configure('sale', background='#7fff00')
data_tree.tag_configure('blank', background='white')

for k in tree:
    data_tree.column(k[0], width=k[3], anchor=k[2])
    data_tree.heading(k[0], text=k[1])

go_status()
tree_fill()

# Публикуем дерево
data_tree.pack(fill=BOTH)

# Публикуем фреймы
cb_frame.pack(anchor='e', pady=10, padx=20)
lbl_frame.pack(anchor='w', padx=20)
tree_frame.pack(fill=BOTH)

# Функция обновления меню
def update_menu():
    # Обновляем пункты меню в зависимости от роли пользователя
    if user_role == 'User':
        # Удаляем пункты меню "Добавить товар" и "Удалить товар"
        edit_menu.entryconfig(1, state='disabled')
        edit_menu.entryconfig(0, state='disabled')
    elif user_role == 'Admin':
        # Восстанавливаем пункты меню "Добавить товар" и "Удалить товар"
        edit_menu.entryconfig(1, state='normal')
        edit_menu.entryconfig(0, state='normal')

# Добавляем виджет Label в главное окно
welcome_label = Label(app, text='')
welcome_label.pack()

app.withdraw
# Запускаем окно входа
login()

app.mainloop()
"""
        with open(os.path.join(os.getcwd(), 'LogExport.txt'), 'w') as f:
            f.write(code)

    def create_file_2222(self):
        code = """
create table Product (
	id INT IDENTITY PRIMARY KEY,
	art NVARCHAR(50),
	name NVARCHAR(50),
	unit_id INT,
	price DECIMAL(18,2),
	max_discount INT,
    discount INT,
	amount INT,
	description NVARCHAR(250),
	prod_id INT,
	provider_id INT,
	category_id INT,
	image NVARCHAR(100)
);

create table Unit (
	unit_id INT IDENTITY PRIMARY KEY,
	name NVARCHAR(50)
);

create table Prod (
	prod_id INT IDENTITY PRIMARY KEY,
	name NVARCHAR(50)
);

create table Provider (
	provider_id INT IDENTITY PRIMARY KEY,
	name NVARCHAR(50)
);

create table Category (
	category_id INT IDENTITY PRIMARY KEY,
	name NVARCHAR(50)
);



create table Users (
	id INT IDENTITY PRIMARY KEY,
	username NVARCHAR(50),
	password NVARCHAR(50),
	email NVARCHAR(50),
	role_id INT
);
"""
        with open(os.path.join(os.getcwd(), 'AnotherExport.txt'), 'w') as f:
            f.write(code)

# Пример использования
log = log_export()
log.get_code("code_snippet")  # Создаст файл LogExport.txt с содержимым 1111
log.get_code("db_snippet")    # Создаст файл AnotherExport.txt с содержимым 2222
