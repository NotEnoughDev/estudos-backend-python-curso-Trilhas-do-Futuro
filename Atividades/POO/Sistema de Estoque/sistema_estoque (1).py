import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime
import hashlib

class SistemaEstoque:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Estoque - Purple & White")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Cores do tema roxo e branco
        self.colors = {
            'primary': '#6a1b9a',      # Roxo principal
            'secondary': '#9c27b0',    # Roxo claro
            'accent': '#e1bee7',       # Roxo muito claro
            'background': '#ffffff',   # Branco
            'text': '#2e2e2e',         # Cinza escuro
            'light_bg': '#f8f8f8'      # Cinza muito claro
        }
        
        # Dados
        self.usuarios = self.carregar_dados('usuarios.json')
        self.produtos = self.carregar_dados('produtos.json')
        self.vendas = self.carregar_dados('vendas.json')
        self.usuario_atual = None
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Iniciar com tela de login
        self.mostrar_tela_login()
        
    def configurar_estilo(self):
        """Configura o estilo visual do sistema"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar cores dos botões
        style.configure('Purple.TButton',
                       background=self.colors['primary'],
                       foreground='white',
                       font=('Arial', 10, 'bold'),
                       padding=10)
        
        style.map('Purple.TButton',
                 background=[('active', self.colors['secondary'])])
        
        # Configurar cores dos frames
        style.configure('Purple.TFrame',
                       background=self.colors['background'])
        
        # Configurar cores das labels
        style.configure('Purple.TLabel',
                       background=self.colors['background'],
                       foreground=self.colors['text'],
                       font=('Arial', 10))
        
        # Configurar cores dos entry
        style.configure('Purple.TEntry',
                       fieldbackground=self.colors['light_bg'],
                       foreground=self.colors['text'],
                       font=('Arial', 10))
        
        # Configurar Treeview
        style.configure('Purple.Treeview',
                       background=self.colors['background'],
                       foreground=self.colors['text'],
                       fieldbackground=self.colors['light_bg'])
        
        style.configure('Purple.Treeview.Heading',
                       background=self.colors['primary'],
                       foreground='white',
                       font=('Arial', 10, 'bold'))
    
    def carregar_dados(self, arquivo):
        """Carrega dados de um arquivo JSON"""
        try:
            if os.path.exists(arquivo):
                with open(arquivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except:
            return []
    
    def salvar_dados(self, dados, arquivo):
        """Salva dados em um arquivo JSON"""
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
    
    def hash_senha(self, senha):
        """Cria hash da senha"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def mostrar_tela_login(self):
        """Mostra a tela de login"""
        self.limpar_tela()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.colors['background'], padx=50, pady=50)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        title_label = tk.Label(main_frame, 
                              text="Sistema de Estoque", 
                              font=('Arial', 24, 'bold'),
                              fg=self.colors['primary'],
                              bg=self.colors['background'])
        title_label.pack(pady=(0, 30))
        
        # Frame do formulário
        form_frame = tk.Frame(main_frame, bg=self.colors['background'])
        form_frame.pack()
        
        # Usuário
        tk.Label(form_frame, text="Usuário:", 
                font=('Arial', 12, 'bold'),
                fg=self.colors['text'],
                bg=self.colors['background']).grid(row=0, column=0, sticky='w', pady=5)
        
        self.entry_usuario = tk.Entry(form_frame, 
                                    font=('Arial', 12),
                                    width=30,
                                    bg=self.colors['light_bg'],
                                    fg=self.colors['text'])
        self.entry_usuario.grid(row=0, column=1, pady=5, padx=(10, 0))
        
        # Senha
        tk.Label(form_frame, text="Senha:", 
                font=('Arial', 12, 'bold'),
                fg=self.colors['text'],
                bg=self.colors['background']).grid(row=1, column=0, sticky='w', pady=5)
        
        self.entry_senha = tk.Entry(form_frame, 
                                   font=('Arial', 12),
                                   width=30,
                                   show='*',
                                   bg=self.colors['light_bg'],
                                   fg=self.colors['text'])
        self.entry_senha.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # Botões
        button_frame = tk.Frame(main_frame, bg=self.colors['background'])
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, 
                 text="Login", 
                 command=self.fazer_login,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['primary'],
                 fg='white',
                 padx=20,
                 pady=10,
                 cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(button_frame, 
                 text="Cadastrar", 
                 command=self.mostrar_tela_cadastro,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['secondary'],
                 fg='white',
                 padx=20,
                 pady=10,
                 cursor='hand2').pack(side='left', padx=10)
        
        # Bind Enter para login
        self.entry_senha.bind('<Return>', lambda e: self.fazer_login())
    
    def mostrar_tela_cadastro(self):
        """Mostra a tela de cadastro de usuário"""
        self.limpar_tela()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.colors['background'], padx=50, pady=50)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        title_label = tk.Label(main_frame, 
                              text="Cadastro de Usuário", 
                              font=('Arial', 24, 'bold'),
                              fg=self.colors['primary'],
                              bg=self.colors['background'])
        title_label.pack(pady=(0, 30))
        
        # Frame do formulário
        form_frame = tk.Frame(main_frame, bg=self.colors['background'])
        form_frame.pack()
        
        # Campos do formulário
        campos = [
            ("Nome:", "entry_nome"),
            ("Usuário:", "entry_usuario"),
            ("Email:", "entry_email"),
            ("Senha:", "entry_senha"),
            ("Confirmar Senha:", "entry_confirmar_senha")
        ]
        
        for i, (label_text, entry_name) in enumerate(campos):
            tk.Label(form_frame, text=label_text, 
                    font=('Arial', 12, 'bold'),
                    fg=self.colors['text'],
                    bg=self.colors['background']).grid(row=i, column=0, sticky='w', pady=5)
            
            entry = tk.Entry(form_frame, 
                           font=('Arial', 12),
                           width=30,
                           bg=self.colors['light_bg'],
                           fg=self.colors['text'])
            entry.grid(row=i, column=1, pady=5, padx=(10, 0))
            
            if "senha" in entry_name:
                entry.config(show='*')
            
            setattr(self, entry_name, entry)
        
        # Botões
        button_frame = tk.Frame(main_frame, bg=self.colors['background'])
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, 
                 text="Cadastrar", 
                 command=self.cadastrar_usuario,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['primary'],
                 fg='white',
                 padx=20,
                 pady=10,
                 cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(button_frame, 
                 text="Voltar", 
                 command=self.mostrar_tela_login,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['secondary'],
                 fg='white',
                 padx=20,
                 pady=10,
                 cursor='hand2').pack(side='left', padx=10)
    
    def cadastrar_usuario(self):
        """Cadastra um novo usuário"""
        nome = self.entry_nome.get().strip()
        usuario = self.entry_usuario.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()
        
        # Validações
        if not all([nome, usuario, email, senha, confirmar_senha]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return
        
        if len(senha) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres!")
            return
        
        # Verificar se usuário já existe
        for user in self.usuarios:
            if user['usuario'] == usuario:
                messagebox.showerror("Erro", "Usuário já existe!")
                return
        
        # Criar novo usuário
        novo_usuario = {
            'id': len(self.usuarios) + 1,
            'nome': nome,
            'usuario': usuario,
            'email': email,
            'senha': self.hash_senha(senha),
            'data_cadastro': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
        
        self.usuarios.append(novo_usuario)
        self.salvar_dados(self.usuarios, 'usuarios.json')
        
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.mostrar_tela_login()
    
    def fazer_login(self):
        """Realiza o login do usuário"""
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get()
        
        if not usuario or not senha:
            messagebox.showerror("Erro", "Usuário e senha são obrigatórios!")
            return
        
        senha_hash = self.hash_senha(senha)
        
        for user in self.usuarios:
            if user['usuario'] == usuario and user['senha'] == senha_hash:
                self.usuario_atual = user
                self.mostrar_menu_principal()
                return
        
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")
    
    def mostrar_menu_principal(self):
        """Mostra o menu principal do sistema"""
        self.limpar_tela()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.colors['background'])
        main_frame.pack(fill='both', expand=True)
        
        # Cabeçalho
        header_frame = tk.Frame(main_frame, bg=self.colors['primary'], height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Título e usuário
        title_frame = tk.Frame(header_frame, bg=self.colors['primary'])
        title_frame.pack(side='left', padx=20, pady=20)
        
        tk.Label(title_frame, 
                text="Sistema de Estoque", 
                font=('Arial', 20, 'bold'),
                fg='white',
                bg=self.colors['primary']).pack(side='left')
        
        user_frame = tk.Frame(header_frame, bg=self.colors['primary'])
        user_frame.pack(side='right', padx=20, pady=20)
        
        tk.Label(user_frame, 
                text=f"Bem-vindo, {self.usuario_atual['nome']}", 
                font=('Arial', 12),
                fg='white',
                bg=self.colors['primary']).pack(side='right')
        
        tk.Button(user_frame, 
                 text="Sair", 
                 command=self.sair,
                 font=('Arial', 10),
                 bg=self.colors['secondary'],
                 fg='white',
                 padx=10,
                 pady=5,
                 cursor='hand2').pack(side='right', padx=(10, 0))
        
        # Menu de navegação
        nav_frame = tk.Frame(main_frame, bg=self.colors['accent'], height=60)
        nav_frame.pack(fill='x')
        nav_frame.pack_propagate(False)
        
        buttons = [
            ("Produtos", self.mostrar_produtos),
            ("Vendas", self.mostrar_vendas),
            ("Relatórios", self.mostrar_relatorios),
            ("Usuários", self.mostrar_usuarios)
        ]
        
        for text, command in buttons:
            tk.Button(nav_frame, 
                     text=text, 
                     command=command,
                     font=('Arial', 12, 'bold'),
                     bg=self.colors['primary'],
                     fg='white',
                     padx=20,
                     pady=15,
                     cursor='hand2').pack(side='left', padx=5, pady=10)
        
        # Área de conteúdo
        self.content_frame = tk.Frame(main_frame, bg=self.colors['background'])
        self.content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Mostrar dashboard por padrão
        self.mostrar_dashboard()
    
    def mostrar_dashboard(self):
        """Mostra o dashboard principal"""
        self.limpar_content()
        
        # Título
        tk.Label(self.content_frame, 
                text="Dashboard", 
                font=('Arial', 18, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['background']).pack(pady=(0, 20))
        
        # Cards de estatísticas
        stats_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        stats_frame.pack(fill='x', pady=10)
        
        # Calcular estatísticas
        total_produtos = len(self.produtos)
        total_usuarios = len(self.usuarios)
        total_vendas = len(self.vendas)
        valor_total_vendas = sum(venda.get('total', 0) for venda in self.vendas)
        
        stats = [
            ("Total de Produtos", total_produtos, self.colors['primary']),
            ("Total de Usuários", total_usuarios, self.colors['secondary']),
            ("Total de Vendas", total_vendas, self.colors['accent']),
            ("Faturamento Total", f"R$ {valor_total_vendas:.2f}", self.colors['primary'])
        ]
        
        for i, (titulo, valor, cor) in enumerate(stats):
            card = tk.Frame(stats_frame, bg=cor, relief='raised', bd=2)
            card.grid(row=0, column=i, padx=10, pady=10, sticky='ew')
            stats_frame.grid_columnconfigure(i, weight=1)
            
            tk.Label(card, 
                    text=titulo, 
                    font=('Arial', 12, 'bold'),
                    fg='white',
                    bg=cor).pack(pady=5)
            
            tk.Label(card, 
                    text=str(valor), 
                    font=('Arial', 20, 'bold'),
                    fg='white',
                    bg=cor).pack(pady=5)
    
    def mostrar_produtos(self):
        """Mostra a tela de gestão de produtos"""
        self.limpar_content()
        
        # Título e botão adicionar
        title_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(title_frame, 
                text="Gestão de Produtos", 
                font=('Arial', 18, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['background']).pack(side='left')
        
        tk.Button(title_frame, 
                 text="+ Adicionar Produto", 
                 command=self.adicionar_produto,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['primary'],
                 fg='white',
                 padx=15,
                 pady=8,
                 cursor='hand2').pack(side='right')
        
        # Tabela de produtos
        columns = ('ID', 'Nome', 'Preço', 'Estoque', 'Categoria', 'Data Cadastro')
        tree = ttk.Treeview(self.content_frame, columns=columns, show='headings', style='Purple.Treeview')
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor='center')
        
        # Adicionar produtos à tabela
        for produto in self.produtos:
            tree.insert('', 'end', values=(
                produto['id'],
                produto['nome'],
                f"R$ {produto['preco']:.2f}",
                produto['estoque'],
                produto['categoria'],
                produto['data_cadastro']
            ))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.content_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind duplo clique para editar
        tree.bind('<Double-1>', lambda e: self.editar_produto(tree))
    
    def adicionar_produto(self):
        """Mostra formulário para adicionar produto"""
        self.mostrar_formulario_produto()
    
    def editar_produto(self, tree):
        """Edita produto selecionado"""
        item = tree.selection()[0]
        produto_id = tree.item(item)['values'][0]
        
        produto = next((p for p in self.produtos if p['id'] == produto_id), None)
        if produto:
            self.mostrar_formulario_produto(produto)
    
    def mostrar_formulario_produto(self, produto=None):
        """Mostra formulário de produto"""
        # Janela modal
        form_window = tk.Toplevel(self.root)
        form_window.title("Adicionar Produto" if not produto else "Editar Produto")
        form_window.geometry("400x500")
        form_window.configure(bg=self.colors['background'])
        form_window.grab_set()
        
        # Centralizar janela
        form_window.transient(self.root)
        form_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        # Título
        tk.Label(form_window, 
                text="Adicionar Produto" if not produto else "Editar Produto", 
                font=('Arial', 16, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['background']).pack(pady=20)
        
        # Frame do formulário
        form_frame = tk.Frame(form_window, bg=self.colors['background'])
        form_frame.pack(padx=30, pady=20)
        
        # Campos
        campos = [
            ("Nome:", "entry_nome"),
            ("Preço:", "entry_preco"),
            ("Estoque:", "entry_estoque"),
            ("Categoria:", "entry_categoria"),
            ("Descrição:", "entry_descricao")
        ]
        
        entries = {}
        for i, (label_text, entry_name) in enumerate(campos):
            tk.Label(form_frame, text=label_text, 
                    font=('Arial', 12, 'bold'),
                    fg=self.colors['text'],
                    bg=self.colors['background']).grid(row=i, column=0, sticky='w', pady=10)
            
            if entry_name == "entry_descricao":
                entry = tk.Text(form_frame, 
                              font=('Arial', 10),
                              width=30,
                              height=3,
                              bg=self.colors['light_bg'],
                              fg=self.colors['text'])
            else:
                entry = tk.Entry(form_frame, 
                               font=('Arial', 10),
                               width=30,
                               bg=self.colors['light_bg'],
                               fg=self.colors['text'])
            
            entry.grid(row=i, column=1, pady=10, padx=(10, 0))
            entries[entry_name] = entry
        
        # Preencher campos se editando
        if produto:
            entries['entry_nome'].insert(0, produto['nome'])
            entries['entry_preco'].insert(0, str(produto['preco']))
            entries['entry_estoque'].insert(0, str(produto['estoque']))
            entries['entry_categoria'].insert(0, produto['categoria'])
            entries['entry_descricao'].insert(1.0, produto.get('descricao', ''))
        
        # Botões
        button_frame = tk.Frame(form_window, bg=self.colors['background'])
        button_frame.pack(pady=20)
        
        def salvar_produto():
            # Validar campos
            nome = entries['entry_nome'].get().strip()
            preco = entries['entry_preco'].get().strip()
            estoque = entries['entry_estoque'].get().strip()
            categoria = entries['entry_categoria'].get().strip()
            descricao = entries['entry_descricao'].get(1.0, tk.END).strip()
            
            if not all([nome, preco, estoque, categoria]):
                messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
                return
            
            try:
                preco = float(preco)
                estoque = int(estoque)
            except ValueError:
                messagebox.showerror("Erro", "Preço deve ser um número decimal e estoque um número inteiro!")
                return
            
            if produto:
                # Editar produto existente
                produto['nome'] = nome
                produto['preco'] = preco
                produto['estoque'] = estoque
                produto['categoria'] = categoria
                produto['descricao'] = descricao
                messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
            else:
                # Adicionar novo produto
                novo_produto = {
                    'id': len(self.produtos) + 1,
                    'nome': nome,
                    'preco': preco,
                    'estoque': estoque,
                    'categoria': categoria,
                    'descricao': descricao,
                    'data_cadastro': datetime.now().strftime('%d/%m/%Y %H:%M')
                }
                self.produtos.append(novo_produto)
                messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            
            self.salvar_dados(self.produtos, 'produtos.json')
            form_window.destroy()
            self.mostrar_produtos()
        
        tk.Button(button_frame, 
                 text="Salvar", 
                 command=salvar_produto,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['primary'],
                 fg='white',
                 padx=20,
                 pady=8,
                 cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(button_frame, 
                 text="Cancelar", 
                 command=form_window.destroy,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['secondary'],
                 fg='white',
                 padx=20,
                 pady=8,
                 cursor='hand2').pack(side='left', padx=10)
    
    def mostrar_vendas(self):
        """Mostra a tela de vendas"""
        self.limpar_content()
        
        # Título e botão nova venda
        title_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(title_frame, 
                text="Gestão de Vendas", 
                font=('Arial', 18, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['background']).pack(side='left')
        
        tk.Button(title_frame, 
                 text="+ Nova Venda", 
                 command=self.nova_venda,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['primary'],
                 fg='white',
                 padx=15,
                 pady=8,
                 cursor='hand2').pack(side='right')
        
        # Tabela de vendas
        columns = ('ID', 'Cliente', 'Produto', 'Quantidade', 'Total', 'Data')
        tree = ttk.Treeview(self.content_frame, columns=columns, show='headings', style='Purple.Treeview')
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor='center')
        
        # Adicionar vendas à tabela
        for venda in self.vendas:
            tree.insert('', 'end', values=(
                venda['id'],
                venda['cliente'],
                venda['produto'],
                venda['quantidade'],
                f"R$ {venda['total']:.2f}",
                venda['data']
            ))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.content_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    def nova_venda(self):
        """Mostra formulário para nova venda"""
        # Janela modal
        venda_window = tk.Toplevel(self.root)
        venda_window.title("Nova Venda")
        venda_window.geometry("600x500")
        venda_window.configure(bg=self.colors['background'])
        venda_window.grab_set()
        
        # Centralizar janela
        venda_window.transient(self.root)
        venda_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        # Título
        tk.Label(venda_window, 
                text="Nova Venda", 
                font=('Arial', 16, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['background']).pack(pady=20)
        
        # Frame do formulário
        form_frame = tk.Frame(venda_window, bg=self.colors['background'])
        form_frame.pack(padx=30, pady=20)
        
        # Cliente
        tk.Label(form_frame, text="Cliente:", 
                font=('Arial', 12, 'bold'),
                fg=self.colors['text'],
                bg=self.colors['background']).grid(row=0, column=0, sticky='w', pady=10)
        
        entry_cliente = tk.Entry(form_frame, 
                               font=('Arial', 10),
                               width=30,
                               bg=self.colors['light_bg'],
                               fg=self.colors['text'])
        entry_cliente.grid(row=0, column=1, pady=10, padx=(10, 0))
        
        # Produto
        tk.Label(form_frame, text="Produto:", 
                font=('Arial', 12, 'bold'),
                fg=self.colors['text'],
                bg=self.colors['background']).grid(row=1, column=0, sticky='w', pady=10)
        
        # ComboBox para produtos
        produto_var = tk.StringVar()
        produto_combo = ttk.Combobox(form_frame, 
                                   textvariable=produto_var,
                                   font=('Arial', 10),
                                   width=27,
                                   state='readonly')
        produto_combo.grid(row=1, column=1, pady=10, padx=(10, 0))
        
        # Preencher produtos
        produtos_list = [f"{p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['estoque']})" for p in self.produtos if p['estoque'] > 0]
        produto_combo['values'] = produtos_list
        
        # Quantidade
        tk.Label(form_frame, text="Quantidade:", 
                font=('Arial', 12, 'bold'),
                fg=self.colors['text'],
                bg=self.colors['background']).grid(row=2, column=0, sticky='w', pady=10)
        
        entry_quantidade = tk.Entry(form_frame, 
                                  font=('Arial', 10),
                                  width=30,
                                  bg=self.colors['light_bg'],
                                  fg=self.colors['text'])
        entry_quantidade.grid(row=2, column=1, pady=10, padx=(10, 0))
        
        # Total
        tk.Label(form_frame, text="Total:", 
                font=('Arial', 12, 'bold'),
                fg=self.colors['text'],
                bg=self.colors['background']).grid(row=3, column=0, sticky='w', pady=10)
        
        label_total = tk.Label(form_frame, 
                              text="R$ 0,00", 
                              font=('Arial', 12, 'bold'),
                              fg=self.colors['primary'],
                              bg=self.colors['background'])
        label_total.grid(row=3, column=1, sticky='w', pady=10, padx=(10, 0))
        
        def calcular_total():
            try:
                produto_selecionado = produto_var.get()
                if produto_selecionado:
                    # Extrair preço do produto selecionado
                    preco_str = produto_selecionado.split('R$ ')[1].split(' ')[0]
                    preco = float(preco_str.replace(',', '.'))
                    quantidade = int(entry_quantidade.get() or 0)
                    total = preco * quantidade
                    label_total.config(text=f"R$ {total:.2f}")
            except:
                label_total.config(text="R$ 0,00")
        
        # Bind eventos
        produto_combo.bind('<<ComboboxSelected>>', lambda e: calcular_total())
        entry_quantidade.bind('<KeyRelease>', lambda e: calcular_total())
        
        # Botões
        button_frame = tk.Frame(venda_window, bg=self.colors['background'])
        button_frame.pack(pady=20)
        
        def finalizar_venda():
            cliente = entry_cliente.get().strip()
            produto_selecionado = produto_var.get()
            quantidade = entry_quantidade.get().strip()
            
            if not all([cliente, produto_selecionado, quantidade]):
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
            
            try:
                quantidade = int(quantidade)
                if quantidade <= 0:
                    messagebox.showerror("Erro", "Quantidade deve ser maior que zero!")
                    return
            except ValueError:
                messagebox.showerror("Erro", "Quantidade deve ser um número inteiro!")
                return
            
            # Encontrar produto
            produto_nome = produto_selecionado.split(' - ')[0]
            produto = next((p for p in self.produtos if p['nome'] == produto_nome), None)
            
            if not produto:
                messagebox.showerror("Erro", "Produto não encontrado!")
                return
            
            if produto['estoque'] < quantidade:
                messagebox.showerror("Erro", "Estoque insuficiente!")
                return
            
            # Criar venda
            total = produto['preco'] * quantidade
            nova_venda = {
                'id': len(self.vendas) + 1,
                'cliente': cliente,
                'produto': produto_nome,
                'quantidade': quantidade,
                'total': total,
                'data': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'vendedor': self.usuario_atual['nome']
            }
            
            # Atualizar estoque
            produto['estoque'] -= quantidade
            
            # Salvar dados
            self.vendas.append(nova_venda)
            self.salvar_dados(self.vendas, 'vendas.json')
            self.salvar_dados(self.produtos, 'produtos.json')
            
            messagebox.showinfo("Sucesso", f"Venda realizada com sucesso!\nTotal: R$ {total:.2f}")
            venda_window.destroy()
            self.mostrar_vendas()
        
        tk.Button(button_frame, 
                 text="Finalizar Venda", 
                 command=finalizar_venda,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['primary'],
                 fg='white',
                 padx=20,
                 pady=8,
                 cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(button_frame, 
                 text="Cancelar", 
                 command=venda_window.destroy,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['secondary'],
                 fg='white',
                 padx=20,
                 pady=8,
                 cursor='hand2').pack(side='left', padx=10)
    
    def mostrar_relatorios(self):
        """Mostra a tela de relatórios"""
        self.limpar_content()
        
        # Título
        tk.Label(self.content_frame, 
                text="Relatórios", 
                font=('Arial', 18, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['background']).pack(pady=(0, 20))
        
        # Frame de relatórios
        reports_frame = tk.Frame(self.content_frame, bg=self.colors['background'])
        reports_frame.pack(fill='both', expand=True)
        
        # Relatório de vendas
        vendas_frame = tk.LabelFrame(reports_frame, 
                                   text="Relatório de Vendas", 
                                   font=('Arial', 12, 'bold'),
                                   fg=self.colors['primary'],
                                   bg=self.colors['background'])
        vendas_frame.pack(fill='x', pady=10)
        
        # Calcular totais
        total_vendas = len(self.vendas)
        valor_total = sum(venda['total'] for venda in self.vendas)
        venda_media = valor_total / total_vendas if total_vendas > 0 else 0
        
        tk.Label(vendas_frame, 
                text=f"Total de Vendas: {total_vendas}", 
                font=('Arial', 11),
                fg=self.colors['text'],
                bg=self.colors['background']).pack(anchor='w', padx=10, pady=5)
        
        tk.Label(vendas_frame, 
                text=f"Faturamento Total: R$ {valor_total:.2f}", 
                font=('Arial', 11),
                fg=self.colors['text'],
                bg=self.colors['background']).pack(anchor='w', padx=10, pady=5)
        
        tk.Label(vendas_frame, 
                text=f"Ticket Médio: R$ {venda_media:.2f}", 
                font=('Arial', 11),
                fg=self.colors['text'],
                bg=self.colors['background']).pack(anchor='w', padx=10, pady=5)
        
        # Relatório de produtos
        produtos_frame = tk.LabelFrame(reports_frame, 
                                     text="Relatório de Produtos", 
                                     font=('Arial', 12, 'bold'),
                                     fg=self.colors['primary'],
                                     bg=self.colors['background'])
        produtos_frame.pack(fill='x', pady=10)
        
        total_produtos = len(self.produtos)
        produtos_estoque_baixo = len([p for p in self.produtos if p['estoque'] < 10])
        valor_estoque = sum(p['preco'] * p['estoque'] for p in self.produtos)
        
        tk.Label(produtos_frame, 
                text=f"Total de Produtos: {total_produtos}", 
                font=('Arial', 11),
                fg=self.colors['text'],
                bg=self.colors['background']).pack(anchor='w', padx=10, pady=5)
        
        tk.Label(produtos_frame, 
                text=f"Produtos com Estoque Baixo: {produtos_estoque_baixo}", 
                font=('Arial', 11),
                fg=self.colors['text'],
                bg=self.colors['background']).pack(anchor='w', padx=10, pady=5)
        
        tk.Label(produtos_frame, 
                text=f"Valor Total do Estoque: R$ {valor_estoque:.2f}", 
                font=('Arial', 11),
                fg=self.colors['text'],
                bg=self.colors['background']).pack(anchor='w', padx=10, pady=5)
        
        # Top produtos
        if self.vendas:
            top_frame = tk.LabelFrame(reports_frame, 
                                    text="Produtos Mais Vendidos", 
                                    font=('Arial', 12, 'bold'),
                                    fg=self.colors['primary'],
                                    bg=self.colors['background'])
            top_frame.pack(fill='x', pady=10)
            
            # Contar vendas por produto
            vendas_por_produto = {}
            for venda in self.vendas:
                produto = venda['produto']
                if produto in vendas_por_produto:
                    vendas_por_produto[produto] += venda['quantidade']
                else:
                    vendas_por_produto[produto] = venda['quantidade']
            
            # Ordenar por quantidade vendida
            top_produtos = sorted(vendas_por_produto.items(), key=lambda x: x[1], reverse=True)[:5]
            
            for i, (produto, quantidade) in enumerate(top_produtos, 1):
                tk.Label(top_frame, 
                        text=f"{i}. {produto}: {quantidade} unidades", 
                        font=('Arial', 11),
                        fg=self.colors['text'],
                        bg=self.colors['background']).pack(anchor='w', padx=10, pady=2)
    
    def mostrar_usuarios(self):
        """Mostra a tela de gestão de usuários"""
        self.limpar_content()
        
        # Título
        tk.Label(self.content_frame, 
                text="Gestão de Usuários", 
                font=('Arial', 18, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['background']).pack(pady=(0, 20))
        
        # Tabela de usuários
        columns = ('ID', 'Nome', 'Usuário', 'Email', 'Data Cadastro')
        tree = ttk.Treeview(self.content_frame, columns=columns, show='headings', style='Purple.Treeview')
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor='center')
        
        # Adicionar usuários à tabela
        for usuario in self.usuarios:
            tree.insert('', 'end', values=(
                usuario['id'],
                usuario['nome'],
                usuario['usuario'],
                usuario['email'],
                usuario['data_cadastro']
            ))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.content_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    def limpar_tela(self):
        """Limpa toda a tela"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def limpar_content(self):
        """Limpa apenas a área de conteúdo"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def sair(self):
        """Sai do sistema"""
        self.root.quit()
    
    def executar(self):
        """Executa o sistema"""
        self.root.mainloop()

if __name__ == "__main__":
    sistema = SistemaEstoque()
    sistema.executar()
