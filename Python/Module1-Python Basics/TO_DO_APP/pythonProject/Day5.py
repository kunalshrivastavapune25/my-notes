todos = []
while True:
    user_action = input('enter add show edit or exit')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('enter a todo')
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index+1}---{item}")
        case 'edit':
            number = int(input("Number of todo to be updated"))
            number = number -1
            new_todo = input('enter a new todo')
            todos[number] = new_todo
        case 'exit':
            break
print('bye')


