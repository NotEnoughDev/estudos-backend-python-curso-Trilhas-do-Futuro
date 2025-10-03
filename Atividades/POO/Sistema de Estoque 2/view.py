import tkinter as tk
from tkinter import ttk, messagebox

class EstoqueView:
    """View - Interface gráfica do sistema"""
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Estoque - MVC")
        self.root.geometry("980x680")
        self.root.configure(bg="#2c3e50")
        
        # Configurar para não redimensionar
        self.root.resizable(False, False)
        
        self.criar_interface()
        
        # Centralizar janela depois de criar a interface
        self.root.update_idletasks()
        self.centralizar_janela()
    
    def centralizar_janela(self):
        """Centraliza a janela na tela"""
        largura = 980
        altura = 680
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f'{largura}x{altura}+{x}+{y}')
    
    def criar_interface(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Cabeçalho
        header_frame = tk.Frame(main_frame, bg="#2c3e50")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        titulo = tk.Label(header_frame, text="Sistema de Controle de Estoque",
                         font=("Arial", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
        titulo.pack()
        
        subtitulo = tk.Label(header_frame, text="Arquitetura MVC em 3 Camadas",
                            font=("Arial", 11, "italic"), bg="#2c3e50", fg="#95a5a6")
        subtitulo.pack()
        
        # Frame de estatísticas
        stats_frame = tk.Frame(main_frame, bg="#34495e", relief=tk.RAISED, bd=2)
        stats_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.label_total_produtos = tk.Label(stats_frame, text="Total de Produtos: 0",
                                            font=("Arial", 10, "bold"), bg="#34495e", fg="#ecf0f1",
                                            padx=10, pady=5)
        self.label_total_produtos.pack(side=tk.LEFT, padx=10)
        
        self.label_valor_estoque = tk.Label(stats_frame, text="Valor em Estoque: R$ 0.00",
                                           font=("Arial", 10, "bold"), bg="#34495e", fg="#ecf0f1",
                                           padx=10, pady=5)
        self.label_valor_estoque.pack(side=tk.LEFT, padx=10)
        
        # Frame de cadastro
        frame_cadastro = tk.LabelFrame(main_frame, text="📦 Cadastro de Produtos",
                                       font=("Arial", 12, "bold"), bg="#34495e",
                                       fg="#ecf0f1", padx=15, pady=15)
        frame_cadastro.pack(fill=tk.X, pady=(0, 20))
        
        # Grid para os campos
        campos_frame = tk.Frame(frame_cadastro, bg="#34495e")
        campos_frame.pack()
        
        # Linha 1: ID e Nome
        tk.Label(campos_frame, text="ID:", bg="#34495e", fg="#ecf0f1",
                font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_id = tk.Entry(campos_frame, width=15, font=("Arial", 10))
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(campos_frame, text="Nome:", bg="#34495e", fg="#ecf0f1",
                font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", pady=5, padx=(15, 0))
        self.entry_nome = tk.Entry(campos_frame, width=30, font=("Arial", 10))
        self.entry_nome.grid(row=0, column=3, padx=5, pady=5)
        
        # Linha 2: Categoria e Quantidade
        tk.Label(campos_frame, text="Categoria:", bg="#34495e", fg="#ecf0f1",
                font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_categoria = tk.Entry(campos_frame, width=15, font=("Arial", 10))
        self.entry_categoria.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(campos_frame, text="Quantidade:", bg="#34495e", fg="#ecf0f1",
                font=("Arial", 10, "bold")).grid(row=1, column=2, sticky="w", pady=5, padx=(15, 0))
        self.entry_quantidade = tk.Entry(campos_frame, width=30, font=("Arial", 10))
        self.entry_quantidade.grid(row=1, column=3, padx=5, pady=5)
        
        # Linha 3: Preços
        tk.Label(campos_frame, text="Preço Compra (R$):", bg="#34495e", fg="#ecf0f1",
                font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_preco_compra = tk.Entry(campos_frame, width=15, font=("Arial", 10))
        self.entry_preco_compra.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(campos_frame, text="Preço Venda (R$):", bg="#34495e", fg="#ecf0f1",
                font=("Arial", 10, "bold")).grid(row=2, column=2, sticky="w", pady=5, padx=(15, 0))
        self.entry_preco_venda = tk.Entry(campos_frame, width=30, font=("Arial", 10))
        self.entry_preco_venda.grid(row=2, column=3, padx=5, pady=5)
        
        # Linha 4: Fornecedor
        tk.Label(campos_frame, text="Fornecedor:", bg="#34495e", fg="#ecf0f1",
                font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
        self.entry_fornecedor = tk.Entry(campos_frame, width=53, font=("Arial", 10))
        self.entry_fornecedor.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
        
        # Frame de botões de ação
        frame_botoes = tk.Frame(frame_cadastro, bg="#34495e")
        frame_botoes.pack(pady=(15, 0))
        
        self.btn_cadastrar = tk.Button(frame_botoes, text="✓ Cadastrar Produto",
                                       bg="#27ae60", fg="white",
                                       font=("Arial", 10, "bold"),
                                       cursor="hand2", padx=20, pady=8,
                                       relief=tk.RAISED, bd=3)
        self.btn_cadastrar.grid(row=0, column=0, padx=5)
        
        self.btn_limpar = tk.Button(frame_botoes, text="✗ Limpar Campos",
                                    bg="#95a5a6", fg="white",
                                    font=("Arial", 10, "bold"),
                                    cursor="hand2", padx=20, pady=8,
                                    relief=tk.RAISED, bd=3)
        self.btn_limpar.grid(row=0, column=1, padx=5)
        
        # Frame da lista
        frame_lista = tk.LabelFrame(main_frame, text="📋 Produtos Cadastrados",
                                   font=("Arial", 12, "bold"), bg="#34495e",
                                   fg="#ecf0f1", padx=15, pady=15)
        frame_lista.pack(fill=tk.BOTH, expand=True)
        
        # Treeview
        tree_frame = tk.Frame(frame_lista, bg="#34495e")
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar_y = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        scrollbar_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        
        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Nome", "Categoria",
                                                       "Quantidade", "Preço Compra",
                                                       "Preço Venda", "Fornecedor"),
                                show="headings", yscrollcommand=scrollbar_y.set,
                                xscrollcommand=scrollbar_x.set, height=12)
        
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Preço Compra", text="Preço Compra")
        self.tree.heading("Preço Venda", text="Preço Venda")
        self.tree.heading("Fornecedor", text="Fornecedor")
        
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Nome", width=150, anchor="w")
        self.tree.column("Categoria", width=100, anchor="w")
        self.tree.column("Quantidade", width=90, anchor="center")
        self.tree.column("Preço Compra", width=110, anchor="center")
        self.tree.column("Preço Venda", width=110, anchor="center")
        self.tree.column("Fornecedor", width=150, anchor="w")
        
        # Botão remover
        self.btn_remover = tk.Button(frame_lista, text="🗑 Remover Produto Selecionado",
                                     bg="#e74c3c", fg="white",
                                     font=("Arial", 10, "bold"),
                                     cursor="hand2", padx=20, pady=8,
                                     relief=tk.RAISED, bd=3)
        self.btn_remover.pack(pady=(10, 0))
    
    def obter_dados_formulario(self):
        """Obtém os dados do formulário"""
        return {
            'id': self.entry_id.get().strip(),
            'nome': self.entry_nome.get().strip(),
            'categoria': self.entry_categoria.get().strip(),
            'quantidade': self.entry_quantidade.get().strip(),
            'preco_compra': self.entry_preco_compra.get().strip(),
            'preco_venda': self.entry_preco_venda.get().strip(),
            'fornecedor': self.entry_fornecedor.get().strip()
        }
    
    def limpar_formulario(self):
        """Limpa todos os campos do formulário"""
        self.entry_id.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco_compra.delete(0, tk.END)
        self.entry_preco_venda.delete(0, tk.END)
        self.entry_fornecedor.delete(0, tk.END)
        self.entry_id.focus()
    
    def atualizar_tabela(self, produtos):
        """Atualiza a tabela com a lista de produtos"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adicionar produtos
        for produto in produtos:
            self.tree.insert("", tk.END, values=(
                produto.id,
                produto.nome,
                produto.categoria,
                produto.quantidade,
                f"R$ {produto.preco_compra:.2f}",
                f"R$ {produto.preco_venda:.2f}",
                produto.fornecedor
            ))
    
    def atualizar_estatisticas(self, total_produtos, valor_estoque):
        """Atualiza as estatísticas exibidas"""
        self.label_total_produtos.config(text=f"Total de Produtos: {total_produtos}")
        self.label_valor_estoque.config(text=f"Valor em Estoque: R$ {valor_estoque:.2f}")
    
    def obter_produto_selecionado(self):
        """Obtém o ID do produto selecionado na tabela"""
        selecionado = self.tree.selection()
        if not selecionado:
            return None
        item = self.tree.item(selecionado[0])
        # Retorna o ID que está na primeira coluna
        return str(item['values'][0])
    
    def mostrar_mensagem_sucesso(self, mensagem):
        """Exibe mensagem de sucesso"""
        messagebox.showinfo("✓ Sucesso", mensagem)
    
    def mostrar_mensagem_erro(self, mensagem):
        """Exibe mensagem de erro"""
        messagebox.showerror("✗ Erro", mensagem)
    
    def mostrar_mensagem_aviso(self, mensagem):
        """Exibe mensagem de aviso"""
        messagebox.showwarning("⚠ Atenção", mensagem)
    
    def confirmar_acao(self, mensagem):
        """Pede confirmação do usuário"""
        return messagebox.askyesno("❓ Confirmar", mensagem)