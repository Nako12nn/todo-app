tasks = ['sss', 'ccc', 'ggg', '4444', '6666']
def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print(f"Task: {new_task} added")

def show_tasks():
    if not tasks:
        print("No tasks yet")
        return
    else:
        for i, task in enumerate(tasks, start =1):
            print(f"{i} {task} ")

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

show_tasks()

add_task()

show_tasks()

delete_task()

show_tasks()