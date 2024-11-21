class Task:
    def __init__(self, titulo, descricao, data_entrega="Sem data de entrega", status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.data_entrega = data_entrega
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        print("\n=== Adicionar Nova Tarefa ===")
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        data_entrega = input("Digite a data de entrega (ou pressione Enter para pular): ")
        
        if not data_entrega:
            data_entrega = "Sem data de entrega"
            
        task = Task(titulo, descricao, data_entrega)
        self.tasks.append(task)
        print("Tarefa adicionada com sucesso!")
    
    def view_tasks(self):
        if not self.tasks:
            print("\nNenhuma tarefa encontrada!")
            return
            
        print("\n=== Todas as Tarefas ===")
        for index, task in enumerate(self.tasks, 1):
            print(f"\nTarefa {index}:")
            print(f"Título: {task.titulo}")
            print(f"Descrição: {task.descricao}")
            print(f"Data de Entrega: {task.data_entrega}")
            print(f"Status: {task.status}")
            print("-" * 20)
    
    def mark_completed(self):
        self.view_tasks()
        if not self.tasks:
            return
            
        try:
            task_num = int(input("\nDigite o número da tarefa para marcar como concluída: ")) - 1
            if 0 <= task_num < len(self.tasks):
                self.tasks[task_num].status = "Concluída"
                print("Tarefa marcada como concluída!")
            else:
                print("Número de tarefa inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")
    
    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return
            
        try:
            task_num = int(input("\nDigite o número da tarefa para excluir: ")) - 1
            if 0 <= task_num < len(self.tasks):
                removed_task = self.tasks.pop(task_num)
                print(f"Tarefa '{removed_task.titulo}' excluída com sucesso!")
            else:
                print("Número de tarefa inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")

def main():
    task_manager = TaskManager()
    
    while True:
        print("\n=== Menu do Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair")
        
        choice = input("\nDigite sua escolha (1-5): ")
        
        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.mark_completed()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            print("\nAté logo!")
            break
        else:
            print("\nEscolha inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    main()