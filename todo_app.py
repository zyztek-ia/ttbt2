import json
import os

class TodoApp:
    def __init__(self, storage_path='todo_storage.json'):
        self.storage_path = storage_path
        self.todos = self.load_todos()

    def load_todos(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return []

    def save_todos(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.todos, f, indent=2)

    def add_todo(self, task):
        todo = {'task': task, 'done': False}
        self.todos.append(todo)
        self.save_todos()
        print(f"Added: {task}")

    def list_todos(self):
        if not self.todos:
            print("No to-do items found.")
            return
        for idx, todo in enumerate(self.todos, 1):
            status = '[x]' if todo['done'] else '[ ]'
            print(f"{idx}. {status} {todo['task']}")

    def complete_todo(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]['done'] = True
            self.save_todos()
            print(f"Marked as done: {self.todos[index]['task']}")
        else:
            print("Invalid index.")

    def delete_todo(self, index):
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            self.save_todos()
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid index.")

if __name__ == "__main__":
    app = TodoApp()
    while True:
        print("\nTo-Do List Application")
        print("1. Add To-Do")
        print("2. List To-Dos")
        print("3. Mark To-Do as Done")
        print("4. Delete To-Do")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter to-do task: ")
            app.add_todo(task)
        elif choice == '2':
            app.list_todos()
        elif choice == '3':
            app.list_todos()
            idx = int(input("Enter task number to mark as done: ")) - 1
            app.complete_todo(idx)
        elif choice == '4':
            app.list_todos()
            idx = int(input("Enter task number to delete: ")) - 1
            app.delete_todo(idx)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")