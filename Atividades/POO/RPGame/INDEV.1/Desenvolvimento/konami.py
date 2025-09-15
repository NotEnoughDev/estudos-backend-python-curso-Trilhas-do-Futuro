"""
Sistema Kogami - Sistema de anotações secretas criptografadas
Arquivo: kogami.py
"""

import os
import time
import base64

class Criptografia:
    """Sistema de criptografia usando Base64 e Caesar Cipher"""
    
    @staticmethod
    def criptografar(texto):
        """
        Criptografa texto usando Caesar Cipher + Base64
        
        Args:
            texto (str): Texto a ser criptografado
            
        Returns:
            str: Texto criptografado
        """
        if not texto:
            return ""
            
        # Aplica Caesar cipher (deslocamento de 3)
        resultado = ""
        for char in texto:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                resultado += chr((ord(char) - ascii_offset + 3) % 26 + ascii_offset)
            else:
                resultado += char
        
        # Codifica em Base64
        return base64.b64encode(resultado.encode('utf-8')).decode('utf-8')
    
    @staticmethod
    def descriptografar(texto_criptografado):
        """
        Descriptografa texto usando Base64 + Caesar Cipher reverso
        
        Args:
            texto_criptografado (str): Texto criptografado
            
        Returns:
            str: Texto descriptografado ou mensagem de erro
        """
        if not texto_criptografado:
            return ""
            
        try:
            # Decodifica Base64
            texto_decodificado = base64.b64decode(texto_criptografado.encode('utf-8')).decode('utf-8')
            
            # Aplica Caesar cipher reverso (deslocamento de -3)
            resultado = ""
            for char in texto_decodificado:
                if char.isalpha():
                    ascii_offset = ord('a') if char.islower() else ord('A')
                    resultado += chr((ord(char) - ascii_offset - 3) % 26 + ascii_offset)
                else:
                    resultado += char
            
            return resultado
        except Exception as e:
            return f"[ERRO] Falha na descriptografia: {str(e)}"

class Kogami:
    """
    Sistema Kogami - Gerenciamento de anotações secretas criptografadas
    
    Funcionalidades:
    - Adicionar anotações criptografadas com timestamp
    - Visualizar anotações descriptografadas
    - Arquivo de dados oculto (.config_cache.dat)
    - Interface de terminal integrada
    """
    
    def __init__(self, arquivo_dados=None):
        """
        Inicializa o sistema Kogami
        
        Args:
            arquivo_dados (str, optional): Nome do arquivo de dados. 
                                         Padrão: '.config_cache.dat'
        """
        self._data_file = arquivo_dados or ".config_cache.dat"
        self.active = False
        self._crypto = Criptografia()
    
    def adicionar_anotacao(self, anotacao):
        """
        Adiciona uma anotação criptografada ao arquivo
        
        Args:
            anotacao (str): Anotação a ser salva
            
        Returns:
            bool: True se salvou com sucesso, False caso contrário
        """
        if not anotacao or not anotacao.strip():
            return False
            
        try:
            with open(self._data_file, "a", encoding="utf-8") as f:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                anotacao_completa = f"[{timestamp}] {anotacao.strip()}"
                anotacao_criptografada = self._crypto.criptografar(anotacao_completa)
                f.write(f"{anotacao_criptografada}\n")
            return True
        except Exception as e:
            print(f"❌ Erro ao salvar: {e}")
            return False
    
    def carregar_anotacoes(self):
        """
        Carrega e descriptografa todas as anotações
        
        Returns:
            list: Lista de anotações descriptografadas
        """
        anotacoes = []
        
        if not os.path.exists(self._data_file):
            return anotacoes
            
        try:
            with open(self._data_file, "r", encoding="utf-8") as f:
                for linha in f:
                    linha = linha.strip()
                    if linha:
                        anotacao_descriptografada = self._crypto.descriptografar(linha)
                        anotacoes.append(anotacao_descriptografada)
        except Exception as e:
            print(f"❌ Erro ao carregar anotações: {e}")
            
        return anotacoes
    
    def visualizar_anotacoes(self):
        """Exibe todas as anotações na interface"""
        anotacoes = self.carregar_anotacoes()
        
        if not anotacoes:
            print("\n📝 Nenhum registro encontrado.")
            return
            
        print("\n" + "="*60)
        print("              ARQUIVO DE CONFIGURAÇÃO")
        print("="*60)
        
        for i, anotacao in enumerate(anotacoes, 1):
            print(f"{i:2d}. {anotacao}")
            
        print("="*60)
        print(f"📊 Total de registros: {len(anotacoes)}")
    
    def limpar_anotacoes(self):
        """
        Remove todas as anotações (arquivo)
        
        Returns:
            bool: True se removeu com sucesso
        """
        try:
            if os.path.exists(self._data_file):
                os.remove(self._data_file)
                return True
            return False
        except Exception as e:
            print(f"❌ Erro ao limpar: {e}")
            return False
    
    def contar_anotacoes(self):
        """
        Conta o número de anotações
        
        Returns:
            int: Número de anotações
        """
        return len(self.carregar_anotacoes())
    
    def _mostrar_interface(self):
        """Exibe a interface do sistema"""
        print("\n" + "🔧"*25)
        print("      PAINEL DE CONFIGURAÇÃO AVANÇADA")
        print("🔧"*25)
        print("1 - Adicionar entrada de log")
        print("2 - Visualizar logs do sistema")
        print("3 - Estatísticas")
        print("4 - Limpar todos os logs")
        print("5 - Retornar")
        print("🔧"*25)
    
    def ativar_interface(self):
        """
        Ativa a interface interativa do sistema Kogami
        
        Returns:
            None
        """
        self.active = True
        print("\n🎉 MODO DESENVOLVEDOR ATIVADO! 🎉")
        print("🔧 Painel de configuração carregado...")
        
        while self.active:
            self._mostrar_interface()
            
            try:
                escolha = input("🔧 Digite uma opção: ").strip()
                
                if escolha == "1":
                    print("\n📝 Digite a entrada de log:")
                    entrada = input(">> ")
                    
                    if self.adicionar_anotacao(entrada):
                        print("✅ Entrada registrada no sistema!\n")
                    else:
                        print("❌ Falha ao registrar entrada!\n")
                        
                elif escolha == "2":
                    self.visualizar_anotacoes()
                    input("\n⏎ Pressione Enter para continuar...")
                    
                elif escolha == "3":
                    total = self.contar_anotacoes()
                    arquivo_existe = "✅ Existe" if os.path.exists(self._data_file) else "❌ Não existe"
                    print(f"\n📊 ESTATÍSTICAS:")
                    print(f"   • Total de registros: {total}")
                    print(f"   • Arquivo: {self._data_file}")
                    print(f"   • Status do arquivo: {arquivo_existe}")
                    input("\n⏎ Pressione Enter para continuar...")
                    
                elif escolha == "4":
                    print(f"\n⚠️  ATENÇÃO: Todos os {self.contar_anotacoes()} registros serão removidos!")
                    confirmacao = input("Digite 'CONFIRMAR' para prosseguir: ")
                    
                    if confirmacao == "CONFIRMAR":
                        if self.limpar_anotacoes():
                            print("✅ Todos os registros foram removidos!")
                        else:
                            print("❌ Nenhum arquivo para remover.")
                    else:
                        print("❌ Operação cancelada.")
                    
                    input("\n⏎ Pressione Enter para continuar...")
                    
                elif escolha == "5":
                    print("🔧 Fechando painel de configuração...")
                    self.active = False
                    break
                    
                else:
                    print("❌ Opção inválida. Tente novamente.\n")
                    
            except KeyboardInterrupt:
                print("\n\n🔧 Fechando painel de configuração...")
                self.active = False
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {e}\n")

# Funções de conveniência para import direto
def criar_sistema_kogami(arquivo=None):
    """
    Cria uma nova instância do sistema Kogami
    
    Args:
        arquivo (str, optional): Nome do arquivo de dados
        
    Returns:
        Kogami: Instância do sistema
    """
    return Kogami(arquivo)

def criptografar_texto(texto):
    """
    Função de conveniência para criptografar texto
    
    Args:
        texto (str): Texto a criptografar
        
    Returns:
        str: Texto criptografado
    """
    return Criptografia.criptografar(texto)

def descriptografar_texto(texto_cripto):
    """
    Função de conveniência para descriptografar texto
    
    Args:
        texto_cripto (str): Texto criptografado
        
    Returns:
        str: Texto descriptografado
    """
    return Criptografia.descriptografar(texto_cripto)

# Exemplo de uso standalone
if __name__ == "__main__":
    print("🔧 Sistema Kogami - Modo Standalone")
    print("=" * 40)
    
    sistema = criar_sistema_kogami()
    sistema.ativar_interface()