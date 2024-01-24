user_prompt = "Enter a ToDo"
todo = ""
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todos)
