import tkinter as tk
from model1 import EstoqueModel
from view import EstoqueView
from controller import EstoqueController

def main():
    """Função principal que inicia o sistema"""
    try:
        # Criar janela principal
        root = tk.Tk()
        
        # Instanciar as camadas MVC
        model = EstoqueModel()
        view = EstoqueView(root)
        controller = EstoqueController(model, view)
        
        # Iniciar loop da interface
        root.mainloop()
        
    except Exception as e:
        print(f"Erro ao iniciar o sistema: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()