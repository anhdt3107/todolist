# Set up the basic structure of the program
tasks = []
completed_tasks = []

def add_task(task):
  tasks.append(task)

def complete_task(index):
  completed_tasks.append(tasks.pop(index))

def display_tasks():
  if not tasks:
    print("No pending tasks")
  else:
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")

def display_completed_tasks():
  if not completed_tasks:
    print("No completed tasks")
  else:
    for i, task in enumerate(completed_tasks):
      print(f"{i+1}. {task}")

while True:
  print("1. Add a task")
  print("2. Mark a task as complete")
  print("3. Display pending tasks")
  print("4. Display completed tasks")
  print("5. Clear completed tasks")
  print("6. Exit")
  choice = int(input("Enter a choice: "))

  # Add a task
  if choice == 1:
    task = input("Enter a task: ")
    add_task(task)
    print("Task added")

  # Mark a task as complete
  elif choice == 2:
    display_tasks()
    index = int(input("Enter the index of the task to mark as complete: ")) - 1
    complete_task(index)
    print("Task marked as complete")

  # Display pending tasks
  elif choice == 3:
    display_tasks()

  # Display completed tasks
  elif choice == 4:
    display_completed_tasks()

  # Clear completed tasks
  elif choice == 5:
    completed_tasks.clear()
    print("Completed tasks cleared")

  # Exit
  elif choice == 6:
    break
