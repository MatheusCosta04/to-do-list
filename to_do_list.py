tasks = []

def addTask():
    task = input("Please Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks(): 
    if not tasks:
        print("There are no tasks currently.") 
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete:"))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task{taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")

    except:
        print("Invalid input.")

if __name__== "__main__":
    print("Welcome to the to do list app!")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")
    
    print("Goodbye")

# Hoje desenvolvi um pequeno projeto de lista de tarefas (To-Do List) no terminal, utilizando apenas Python puro.

# Com ele, é possível: ✅ Adicionar novas tarefas
# 🗑️ Deletar tarefas específicas
# 📋 Listar todas as tarefas

# Tudo isso rodando em loop no terminal, com interações simples e práticas — ideal para quem está começando ou quer reforçar a lógica de programação e estruturas básicas como listas, funções e controle de fluxo.

# 🔧 Ferramentas utilizadas:

# Python 3

# Terminal (CLI)

# Esse tipo de projeto, mesmo sendo simples, é um ótimo exercício para desenvolver raciocínio lógico e habilidades com entrada e saída de dados!
