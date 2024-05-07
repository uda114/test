import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

from tabulate import tabulate

class Task:
    def __init__(self, id, title, priority, category, due_date, completed):
        self.id = id
        self.title = title
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.completed = completed 

class TaskManager:
    def __init__(self):
        cred = credentials.Certificate("C:/Users/udara/Desktop/my-application-478b6-firebase-adminsdk-lqgxv-050f774779.json")  # Update with your service account key file path
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://my-application-478b6-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Update with your database URL
        })

    def add_task(self, title, priority, category, due_date):
        new_task_ref = db.reference('tasks').push()
        new_task_ref.set({
            'title': title,
            'priority': priority,
            'category': category,
            'due_date': due_date.strftime("%Y-%m-%d"),
            'completed': False
        })

    def get_all_tasks(self):
        tasks_ref = db.reference('tasks').get()
        tasks = []
        for task_id, task_data in tasks_ref.items():
            task = Task(task_id, task_data['title'], task_data['priority'], task_data['category'], datetime.datetime.strptime(task_data['due_date'], "%Y-%m-%d").date(), task_data['completed'])
            tasks.append(task)
        
        tabledata = []
        for i, task in enumerate(tasks, start=1):
            # print("Task ID\tPrioroty\tName\t\t\t Category\t Date\t Status")
            # print(f"{i}.\tv{task.priority}\t\t{task.title}\t{task.category}\t{task.due_date}\t{'Completed' if task.completed else 'Pending'}")
            
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))

    def filter_by_priority(self, priority):
        tasks_ref = db.reference('tasks').order_by_child('priority').equal_to(priority).get()
        tasks = []
        tabledata = []
        
        for task_id, task_data in tasks_ref.items():
            task = Task(task_id, task_data['title'], task_data['priority'], task_data['category'], datetime.datetime.strptime(task_data['due_date'], "%Y-%m-%d").date(), task_data['completed'])
            tasks.append(task)
            
        for i, task in enumerate(tasks, start=1):
            # print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))

    def filter_by_category(self, category):
        tasks_ref = db.reference('tasks').order_by_child('category').equal_to(category).get()
        tasks = []
        tabledata = []
        for task_id, task_data in tasks_ref.items():
            task = Task(task_id, task_data['title'], task_data['priority'], task_data['category'], datetime.datetime.strptime(task_data['due_date'], "%Y-%m-%d").date(), task_data['completed'])
            tasks.append(task)
            
        for i, task in enumerate(tasks, start=1):
            # print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))

    def sort_by_due_date(self):
        tasks_ref = db.reference('tasks').order_by_child('due_date').get()
        tasks = []
        tabledata = []
        for task_id, task_data in tasks_ref.items():
            task = Task(task_id, task_data['title'], task_data['priority'], task_data['category'], datetime.datetime.strptime(task_data['due_date'], "%Y-%m-%d").date(), task_data['completed'])
            tasks.append(task)
        
        for i, task in enumerate(tasks, start=1):
            # print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))

    def mark_as_complete(self, task_id):
        db.reference('tasks').child(task_id).update({'completed': True})

    def remove_task(self, task_id):
        db.reference('tasks').child(task_id).delete()

# Sample usage
if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. View All Tasks")
        print("3. Filter by Priority")
        print("4. Filter by Category")
        print("5. Sort by Due Date")
        print("6. Mark Task as Complete")
        print("7. Remove Task")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            category = input("Enter task category: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            task_manager.add_task(title, priority, category, due_date)
            print("Task added successfully.")
        elif choice == '2':
            print("\nAll tasks:")
            task_manager.get_all_tasks()
            
        elif choice == '3':
            priority = input("Enter priority to filter by: ")
            task_manager.filter_by_priority(priority)
            
        elif choice == '4':
            category = input("Enter category to filter by: ")
            task_manager.filter_by_category(category)
            
        elif choice == '5':
            print("\nTasks sorted by due date:")
            tasks = task_manager.sort_by_due_date()
            
        elif choice == '6':
            task_id = input("Enter the id of the task to mark as complete: ")
            task_manager.mark_as_complete(task_id)
            print("Task marked as complete.")
        elif choice == '7':
            task_id = input("Enter the id of the task to remove: ")
            task_manager.remove_task(task_id)
            print("Task removed successfully.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
