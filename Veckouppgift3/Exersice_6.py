#6 Todo list (att göra-lista) Bygg ett program där användaren kan lägga till saker till en todo-lista.
todo_list = []
finished_list = []

print("** Todo list extravaganza **\n1. Se innehållet i din lista\n2. Lägga till nya punkter i din lista\n3. Markera som klar\n4. Lagg tillbaka klart foremal till todo\n5. Avsluta")

while True:
    user_action = input("Välj ett alternativ: ")
    if user_action == '1':
        for i in todo_list:
            print(i)
    elif user_action == '2':
        todo = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        todo_list.append(todo)
    elif user_action == '3':
        for i in todo_list:
            print(i)
        user_to_remove = input("Vilken ar du klar med? > ")
        try:
            # .index to do initial check if item is in the list, then do the actions to it in the next try-block
            todo_list.index(user_to_remove)
            try:
                finished_list.append(user_to_remove)
                todo_list.remove(user_to_remove)
            except ValueError:
                # Because above comment and .index, we should never get here
                print("Should never reach this code")
        except ValueError:
            print("Todo inte i listan, forsok igen")
    elif user_action == '4':
        for i in finished_list:
            print(i)
        user_to_remove = input("Vilken ar du klar med? > ")
        try:
            # .index to do initial check if item is in the list, then do the actions to it in the next try-block
            finished_list.index(user_to_remove)
            try:
                finished_list.append(user_to_remove)
                finished_list.remove(user_to_remove)
            except ValueError:
                # Because above comment and .index, we should never get here
                print("Should never reach this code")
        except ValueError:
            print("Klara uppgiften inte i listan, forsok igen")
    elif user_action == '5':
        break
