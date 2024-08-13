def task():
    tasks =[]
    print("--welcome to the TASK MANAGER APP--")
    total_task=int(input("enter the number of task"))
    for i in range (1,total_task+1):
        task_name=input(f"enter the name of the task{i}=")
        tasks.append(task_name)
    print(f"Todays tasks are\n{tasks}")
    while True:
       try:
        operation=int(input("Enter \n1.ADD\n2.UPDATE\n3.VIEW\n4.DELETE\n5.EXIT"))
        if operation==1:
            add=input("enter the new task")
            tasks.append(add)
            print(f"new task {add}, have been added")
        elif operation==2:
            update_val=input("enter the updating task=" )
            if update_val in tasks:
                ind=tasks.index(update_val)
                up=input("enter the updated task")
                tasks[ind]=up
                print(f"the task has been updated to {up} ")
            else:
                print('this task does not exist')
        elif operation==3:
            print("the current tasks are",tasks)
        elif operation==4:
            del_val=input("enter the task to delete")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print("the task have been deleted")
            else:
                print('the task does not exist')
        elif operation==5:
            break
        else:
            print("inavid option,Enter an option with in 1 to 5")
       except ValueError:
           print("Invalid input. please input a valid option")

task()


