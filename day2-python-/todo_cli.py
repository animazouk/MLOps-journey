'''
Project: todo_cli.py
Goal: Build a fully interactive To-Do List CLI from scratch
Time: 30–45 mins
Difficulty: Intermediate (uses lists, loops, input parsing, error handling)
'''
#Feature,Must Do
'''
1. Add Task,add <task name> → adds to list
2. Show Tasks,show → prints numbered list
3. Remove Task,remove <number> → deletes by index
4. Quit,quit → exits program
5. Error Handling,
6. Empty List Check,"show → ""No tasks!"" if empty"
7. Case Insensitive,"ADD, Show, QUIT all work"
8. No Crash,"Invalid input → ""Try again"""
'''

def main():

    todo = []
    while True: 
        cmd = input("Enter Next Command here > ").strip().lower()

#.      Add Task
        if cmd.startswith("add "):
            task = cmd[4:].strip()
            if task:
                todo.append(task)
                print(f"Added: {task}")
            else:
                print("task cannot be empty")
#       Show List
        elif cmd.startswith("show"):
            if todo:
               for i,task in enumerate(todo,1):
                   print(f"{i}. {task} ")
            else:
                print("Todo is Empty")
        elif cmd.startswith("remove "):
            try:
                index = int(cmd.split(maxsplit=1)[1])-1
                if 0 <= index <= len(todo):
                    removed = todo.pop(index)
                    print(f" removed: {removed}")
                else:
                   print("Invalid task number!")
            except (ValueError,IndexError):
                print("Please enter a valid number x as : remove x")
        
        elif cmd.startswith("quit"):
            print("Goodbye! Stay productive.")
            break
        else:
            print("Unknown command. Use: add, show, remove, quit")

        print()

if __name__ == "__main__":
    main()

