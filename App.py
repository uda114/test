
import datetime
import time
from colorama import init, Fore, Style
from tabulate import tabulate

init()

class TaskWork:
    def __init__(self, title, priority, category, due_date):
        self.title = title
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.completed = False
        
class WorkManager:
    def __init__(self):
        self.tasks = []
        
    def addTask(self, title, priority, category, due_date):
        
        
        
        # if priority == 1: priority == "High"
        # elif priority == 2: priority == "Medium"
        # elif priority == 3: priority == "Low"
        
        newTask = TaskWork(title, priority, category, due_date)
        self.tasks.append(newTask)
        
    def viewTask(self):
        tabledata = []
        for i, task in enumerate(self.tasks, start=1):
            # print("Task ID\tPrioroty\tName\t\t\t Category\t Date\t Status")
            # print(f"{i}.\tv{task.priority}\t\t{task.title}\t{task.category}\t{task.due_date}\t{'Completed' if task.completed else 'Pending'}")
            
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))
     
    def priorotyFilter(self, priority):
        filterPriority = []
        tabledata = []
        for task in self.tasks:
            if task.priority == priority:
                filterPriority.append(task)
               
        for i, task in enumerate(filterPriority, start=1):
            # print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))
            
    def CategoryFilter(self, category):
        categoryFilter = []
        tabledata = []
        for task in self.tasks:
            if task.category == category:
                categoryFilter.append(task)
                
        for i, task in enumerate(categoryFilter, start=1):
            #print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))
            
    def DateFilter(self):
        
        tabledata = [] 
        sortDateTask = sorted(self.tasks, key=lambda x: x.due_date )
        for i, task in enumerate(sortDateTask, start=1):
            #print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))

    def markComplete(self, index_number):
        try:
            task = self.tasks[int(index_number) - 1]
            task.completed = True
            print(Fore.GREEN + f"Task '{task.title}' is completed!" +Style.RESET_ALL)
        except:
            print(Fore.RED +"Enter a valid task ID"+ Style.RESET_ALL)
        
    def deleteTask(self, index_number):
        try:
            del self.tasks[int(index_number) - 1]
            print(Fore.GREEN + "Task removed successfully." +Style.RESET_ALL)
        except:
            print(Fore.RED +"Enter a valid task ID"+Style.RESET_ALL)

def validatePriority(priority):
    
    # priorities = ["1", "2", "3"]
    priorities = ["High", "Medium", "Low"]
    if priority.capitalize() in priorities:
        return True
    else:
        print(Fore.RED + "Invalid priority. Please enter High, Medium, or Low." +Style.RESET_ALL)
        return False

def validateCatagory(catagory):
    # catagories = ["1", "2"]
    catagories = ["Personal", "Business"]
    if catagory.capitalize() in catagories:
        return True 
    else:
        print(Fore.RED + "Invalid catagory. Please enter Personal, or Business." + Style.RESET_ALL)
        return False

def validateNumber(number):
    if number.isdigit():
        return True
    else:
        print(Fore.RED + "Invalid input. Enter only numbers" + Style.RESET_ALL)
        return False
    
def setPriority(priority):
    
    if priority == "1": 
        priority = "High" 
        return priority
    elif priority == "2": 
        priority = "Medium" 
        return priority
    elif priority == "3": 
        priority = "Low"
        return priority
    
def setCatagory(category):
    if category == "1": 
        category = "Personal" 
        return category
    elif category =="2": 
        category = "Business" 
        return category
        

  
def taskInput():
    
    title = input("\nEnter task name: \n > ")
    
    
    priority = input("\nEnter task priority (High, Medium, or Low): \n > ")
    
    while not validatePriority(priority):
        priority = input("\nEnter task priority (High, Medium, or Low): \n > ")
    
    # priority = setPriority(priority)
    
    
    category = input("\nEnter task category (Personal, or Business): \n > ")
    
    while not validateCatagory(category):
        category = input("\nEnter task category (Personal, or Business): \n > ")
    
    # category = setCatagory(category)
    
    
    dategiven = input("\nEnter due date (YYYY-MM-DD): \n > ")
    while (True) :
        try: 
            due_date = datetime.datetime.strptime(dategiven, "%Y-%m-%d").date()
            if due_date >= datetime.date.today():
                break
            else:
                dategiven = input("\nEnter a date in "+Fore.RED+"future"+Style.RESET_ALL+" (YYYY-MM-DD): \n > ")
        except: 
            dategiven = input("\nEnter "+Fore.RED+"a valid"+Style.RESET_ALL+" due date (YYYY-MM-DD): \n > ")
        
    
    return title, priority, category, due_date


if __name__ == "__main__":
    
    Work_Manager = WorkManager()
    
    print("Welcome to Task Manager CLI!")
    # print("\n" +Fore.RED +"Type " +Fore.GREEN +"'help'"+ Style.RESET_ALL+" to see available commands.")
    
    while True:
        
        print("\n" +Fore.RED +"Type " +Fore.GREEN +"'help'"+ Style.RESET_ALL+" to see available commands.")
        choice = input("\n > ")

        if (choice == "add"):
            title, priority, category, deadline = taskInput()
            Work_Manager.addTask(title, priority, category, deadline)
            print(Fore.GREEN +"\n Task added successfully." + Style.RESET_ALL)
            
        elif (choice == "list"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            
        elif (choice == "priority"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            priority = input("\nEnter priority to filter by (High, Medium, Low): ")
            while not validatePriority(priority):
                priority = input("\nEnter task priority High, Medium, Low: ")
            # priority = setPriority(priority)
            Work_Manager.priorotyFilter(priority)
            
        elif (choice == "category"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            category = input("\nEnter task category (Personal, Business): ")
            while not validateCatagory(category):
                category = input("\nEnter task category (Personal, Business): ")
            # category = setCatagory(category)
            Work_Manager.CategoryFilter(category)
            
        elif (choice == "date"):
            print("\n\nView All Sorted Tasks:")
            Work_Manager.DateFilter()
            
        elif (choice == "complete"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            taskNumber = input("\nEnter the index of the task to mark as complete: ")
            while not validateNumber(taskNumber):
                taskNumber = input("\nEnter the index of the task to mark as complete: ")
            Work_Manager.markComplete(taskNumber)
            
        elif (choice == "delete"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            delTaskNumber = input("\nEnter the index of the task to remove: ")
            while not validateNumber(delTaskNumber):
                delTaskNumber = input("\nEnter the index of the task to remove: ")
            Work_Manager.deleteTask(delTaskNumber)
        
        elif (choice.title() == "Help"):
            
            print("\nAvailable commands:")
            print("\n -"+Fore.BLUE+" add"+Style.RESET_ALL+": Add a new task")
            print(" -"+Fore.BLUE+" list"+Style.RESET_ALL+": List all tasks")
            print(" -"+Fore.BLUE+" priority"+Style.RESET_ALL+": View taks by priority")
            print(" -"+Fore.BLUE+" category"+Style.RESET_ALL+": View task by category")
            print(" -"+Fore.BLUE+" date"+Style.RESET_ALL+": Sort task by due date")
            print(" -"+Fore.BLUE+" complete"+Style.RESET_ALL+": Mark a task as complete")
            print(" -"+Fore.BLUE+" delete"+Style.RESET_ALL+": Remove a task")
            print(" -"+Fore.BLUE+" exit"+Style.RESET_ALL+": Exit application")
        
        elif choice == 'exit':
            print(Fore.RED + "Exiting..." +Style.RESET_ALL)
            print(Fore.RED + "..Thank you for using Task manager.." +Style.RESET_ALL)
            time.sleep(3)
            break
        else:
            print("Invalid choice. Please try again.")
            
            
            
            