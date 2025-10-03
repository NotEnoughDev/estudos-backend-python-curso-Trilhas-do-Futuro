from model1 import ProdutoModel

class EstoqueController:
    """Controller - Gerencia a comunicação entre Model e View"""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Conectar eventos dos botões
        self.view.btn_cadastrar.config(command=self.cadastrar_produto)
        self.view.btn_limpar.config(command=self.limpar_formulario)
        self.view.btn_remover.config(command=self.remover_produto)
        
        # Carregar produtos iniciais
        self.atualizar_interface()
    
    def cadastrar_produto(self):
        """Processa o cadastro de um novo produto"""
        try:
            # Obter dados do formulário
            dados = self.view.obter_dados_formulario()
            
            # Validar campos vazios
            if not all(dados.values()):
                self.view.mostrar_mensagem_aviso("Todos os campos devem ser preenchidos!")
                return
            
            # Validar e converter tipos
            try:
                quantidade = int(dados['quantidade'])
                preco_compra = float(dados['preco_compra'].replace(',', '.'))
                preco_venda = float(dados['preco_venda'].replace(',', '.'))
            except ValueError:
                self.view.mostrar_mensagem_erro(
                    "Quantidade deve ser um número inteiro!\n"
                    "Preços devem ser números decimais!"
                )
                return
            
            # Validar valores positivos
            if quantidade < 0:
                self.view.mostrar_mensagem_erro("Quantidade não pode ser negativa!")
                return
            
            if preco_compra < 0 or preco_venda < 0:
                self.view.mostrar_mensagem_erro("Preços não podem ser negativos!")
                return
            
            # Validar lógica de negócio
            if preco_venda < preco_compra:
                resposta = self.view.confirmar_acao(
                    "O preço de venda é menor que o preço de compra.\n"
                    "Isso resultará em prejuízo. Deseja continuar?"
                )
                if not resposta:
                    return
            
            # Criar produto
            produto = ProdutoModel(
                dados['id'],
                dados['nome'],
                dados['categoria'],
                quantidade,
                preco_compra,
                preco_venda,
                dados['fornecedor']
            )
            
            # Adicionar ao modelo
            self.model.adicionar_produto(produto)
            
            # Atualizar interface
            self.atualizar_interface()
            self.view.limpar_formulario()
            self.view.mostrar_mensagem_sucesso(
                f"Produto '{dados['nome']}' cadastrado com sucesso!"
            )
            
        except ValueError as e:
            self.view.mostrar_mensagem_erro(str(e))
        except Exception as e:
            self.view.mostrar_mensagem_erro(f"Erro ao cadastrar produto:\n{str(e)}")
    
    def remover_produto(self):
        """Remove o produto selecionado"""
        try:
            # Obter ID do produto selecionado
            id_produto = self.view.obter_produto_selecionado()
            
            if not id_produto:
                self.view.mostrar_mensagem_aviso("Selecione um produto na tabela para remover!")
                return
            
            # Buscar informações do produto
            produto = self.model.buscar_produto_por_id(id_produto)
            if not produto:
                self.view.mostrar_mensagem_erro("Produto não encontrado!")
                return
            
            # Confirmar remoção
            confirmar = self.view.confirmar_acao(
                f"Deseja realmente remover o produto?\n\n"
                f"ID: {produto.id}\n"
                f"Nome: {produto.nome}\n"
                f"Categoria: {produto.categoria}"
            )
            
            if confirmar:
                # Remover produto
                self.model.remover_produto(id_produto)
                
                # Atualizar interface
                self.atualizar_interface()
                
                # Mostrar mensagem de sucesso
                self.view.mostrar_mensagem_sucesso(
                    f"Produto '{produto.nome}' removido com sucesso!"
                )
                
        except ValueError as e:
            self.view.mostrar_mensagem_erro(str(e))
        except Exception as e:
            self.view.mostrar_mensagem_erro(f"Erro ao remover produto:\n{str(e)}")
    
    def limpar_formulario(self):
        """Limpa o formulário"""
        self.view.limpar_formulario()
    
    def atualizar_interface(self):
        """Atualiza toda a interface com os dados do modelo"""
        try:
            # Atualizar tabela
            produtos = self.model.obter_todos_produtos()
            self.view.atualizar_tabela(produtos)
            
            # Atualizar estatísticas
            total_produtos = self.model.obter_total_produtos()
            valor_estoque = self.model.obter_valor_total_estoque()
            self.view.atualizar_estatisticas(total_produtos, valor_estoque)
        except Exception as e:
            print(f"Erro ao atualizar interface: {e}")
