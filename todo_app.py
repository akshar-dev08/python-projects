todos = []

while True:
    print("1.Add task")
    print("2.Show all tasks")
    print("3. delete task")
    print("4.exit")
    
    choice = input("enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        todos.append(task)
        print("Task Added!")
        
    elif choice == "2":
        for i in range(len(todos)):
            print(str(i+1) + "." + todos[i])
            
    elif choice == "3":
        print("1.delete a task")
        print("2.delete all the tasks")
        delete_choice = input("Enter your choice:")
        if delete_choice == "1":
            task = input("enter the task to delete:")
            todos.remove(task)
            print("task removed")
        elif delete_choice == "2":
            todos.clear()
            print("all the task are clear")
            
    elif choice == "4" :
        print("good bye!")
        break
