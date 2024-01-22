# tasks is an empty list for storing user's tasks
tasks = []

def add_task():
    print("Add task")
    new_task = input("Enter your task : ")
    tasks.append(new_task)
    print("New task is successfully added")

def veiw_task():
    print("View tasks")
    if tasks:
        print("Tasks : ")
        for index , task in enumerate(tasks , start=1):
            print(f"{index}.{task}")
        
    else:
        print("No task found")

def complete_task():
    veiw_task()
    if tasks:
        task_index =  int(input("Enter the task number to mark as complete : "))
        if 1<=task_index>=len(tasks):
            done_tasks=tasks.pop(task_index - 1)
            print(f"Task '{done_tasks}' marked as complete.")
        else:
            print("Invalide task number")
    else:
        print("No task found!!")

# the main pae of the program
while True:    
    print("M==== TO-Do-List ====M")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Exit")
    x = input("Enter your choice (1_4) : ")

    if int(x) == 1:
        add_task()

    elif int(x) == 2:
        veiw_task()

    elif int(x) == 3:
        complete_task()

    elif int(x) == 4:
        print("Exiting the program...")
        break

    else:
        print("Wrong input")