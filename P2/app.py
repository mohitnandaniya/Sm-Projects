# > Create Simple Tasks Manage Program Using datetime and file io

import datetime as dt
get_dt = dt.datetime.now()
date = get_dt.strftime("%d/%m/%y")
time = get_dt.strftime("%H:%M:%S")
tasks = {}

def create_db(tasks):
    task_file = open("./P2/task_manage.txt","w")
    task_file.write(str(tasks))
    task_file.write('\n')
    task_file.close()

def create_tasks(tasks):
    task_no = int(input("How Many Task You Add : "))
    for i in range(task_no):
        task = input("Enter Your Task : ")
        tasks[i+1] = [task,date,time]
    return create_db(tasks)

def read_tasks():
    try:
        read_tasks = open("./P2/task_manage.txt","r")
        tasks = read_tasks.readline()
        return tasks
    except:
        pass

def delete_tasks():
    try:
        delete_task = input("Enter Task For Delete: ")
        tasks.pop(int(delete_task))
        return create_db(tasks)
    except:
        pass

def update_tasks():
    try:
        update_task = input("Enter Task For Update: ")
        new_task = input("Enter New Task: ")
        tasks[int(update_task)] = [new_task, date, time]
        return create_db(tasks)
    except:
        pass

print(create_tasks(tasks))
print(read_tasks())
delete_tasks()
update_tasks()
print(read_tasks())