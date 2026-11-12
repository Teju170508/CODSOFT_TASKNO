#TO-DO LIST APPLICATION:
task=[]
def add_task():
    new_task=input("Enter the new task:")
    task.append(new_task)
    print("task added successfully!")
def view_task():
    if len(task)==0:
        print("no task available!")
    else:
        print("\nYour task:")
        for i in range(len(task)):
              print(i+1,".",task[i])
def delete_task():
    view_task()
    if len(task)>0:
        task_number=int(input("Enter the task number to delete:"))
            
    if 1 <= task_number <=len(task):
        removed_task =task.pop(task_number-1)
        print("Deleted task:",removed_task)
    else:
        print("invalid task number!")
                    
while True:
    print("\n====To-Do List Applicaion====")
    print("1.Add Task")
    print("2.view Task")
    print("3.Delete Task")
    print("4.Exit")
    
    choice=input("Enter your choice:")
    
    if choice=="1":
        add_task()
        
    elif choice=="2":
        view_task()
        
    elif choice=="3":
        delete_task()
        
    elif choice=="4":
        print("Thankyou for using To-Do List!")
        break
    
    else:
        print("Invalid choice. please try again!")
        
        
