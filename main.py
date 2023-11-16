def list_todos(todos):
    """
        List todos
    """
    
  
def add_todo(todos):
    """
        Add todos
    """
    todos.append()

def edit_todo(todos):
    """
        Edit todos
    """

def delete_todo(todos):
    """
        Edit todos
    """
  
      
def menu(todos):
    print("What would you like to do?")
    print("1. List todos")
    print("2. Add a todo")
    print("3. Edit a todo")
    print("4. Delete a todo")
    print("5. Quit")
    choice = input("> ")
    if choice == "1":
      list_todos(1)
    elif choice == "2":
      list_todos(2)
    elif choice == "3":
      list_todos(3)
    elif choice == "4":
      list_todos(4)
    elif choice == "5":
      list_todos(5)
      
def main():
    print("Welcome to your todo list!")
    todos = []
    menu(todos)

main()
