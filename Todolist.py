import psycopg2

# Підключення до бази
conn = psycopg2.connect(
    dbname="todo_app",
    user="maksym.com",     # тут вкажи свій юзер
    password="Ps-q-l34!!",   # пароль від Postgres
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# 1. Створимо таблицю (якщо ще нема)
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
""")

# 2. Додамо завдання
cur.execute("INSERT INTO tasks (description) VALUES (%s)",)

# 3. Отримаємо всі завдання
cur.execute("SELECT * FROM tasks;")
rows = cur.fetchall()
for row in rows:
    print(row)

# 4. Збережемо зміни
conn.commit()

print()

def add_task(description):
    cur.execute("INSERT INTO tasks(description) VALUES (%s)", (description))
    conn.commit()
    print(f"Task {description} was added! ") 

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet")
        return
    else:
        for row, task in enumerate(tasks, start =1):
            print(f"{row} {task} ")

def delete_task():
    if tasks:
        delete = int(input("Wanna delete a task?: enter number "))
        right_index = int(delete) - 1
        if right_index < len(tasks):    
            tasks.pop(int(right_index))
        else:
            input("enter correct number: ")
    else:
        print("no tasks yet")

while True:
    print()
    print()
    print()
    print()
    print()
    print()
    break 
show_tasks()

add_task()

show_tasks()

delete_task()

show_tasks()
# now I got some redults 