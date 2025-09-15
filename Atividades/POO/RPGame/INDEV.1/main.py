import os
import time
import base64

def print_dragao():
    print("""\t\t\t\t
                                                                      
                        ,===:'.,            `-._                           
                               `:.`---.__         `-._                     
                                 `:.     `--.         `.                   
                                 \.        `.         `.                  
                         (,,(,    \.         `.   ____,-`.,               
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                   
                     \;'   /  ,' /  _  \  /  _  \   ,'/                   
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'      
    """)

def clear():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

class Criptografia:
    @staticmethod
    def criptografar(texto):
        """Criptografia simples usando Base64 e Caesar Cipher"""
        # Converte para bytes, aplica Caesar cipher e depois Base64
        resultado = ""
        for char in texto:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                resultado += chr((ord(char) - ascii_offset + 3) % 26 + ascii_offset)
            else:
                resultado += char
        return base64.b64encode(resultado.encode()).decode()
    
    @staticmethod
    def descriptografar(texto_criptografado):
        """Descriptografa o texto"""
        try:
            # Decodifica Base64 primeiro
            texto_decodificado = base64.b64decode(texto_criptografado.encode()).decode()
            # Aplica Caesar cipher reverso
            resultado = ""
            for char in texto_decodificado:
                if char.isalpha():
                    ascii_offset = ord('a') if char.islower() else ord('A')
                    resultado += chr((ord(char) - ascii_offset - 3) % 26 + ascii_offset)
                else:
                    resultado += char
            return resultado
        except:
            return "Erro ao descriptografar"

class Kogami:
    def __init__(self):
        self._data_file = ".config_cache.dat"
    
    def _save_entry(self, entry):
        """Salva entrada no arquivo oculto"""
        with open(self._data_file, "a", encoding="utf-8") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            full_entry = f"[{timestamp}] {entry}"
            encrypted_entry = Criptografia.criptografar(full_entry)
            f.write(f"{encrypted_entry}\n")
    
    def _load_entries(self):
        """Carrega entradas do arquivo oculto"""
        if os.path.exists(self._data_file):
            with open(self._data_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if lines:
                    clear()
                    print("\n" + "="*50)
                    print("           ARQUIVO DE CONFIGURAÇÃO")
                    print("="*50)
                    for i, line in enumerate(lines, 1):
                        decrypted_line = Criptografia.descriptografar(line.strip())
                        print(f"{i}. {decrypted_line}")
                    print("="*50)
                else:
                    clear()
                    print("\n Nenhum registro encontrado.")
        else:
            clear()
            print("\n Arquivo de configuração não encontrado.")
    
    def _interface(self):
        """Interface do sistema oculto"""
        clear()
        print("\n" + "🔧"*21)
        print("   PAINEL DE CONFIGURAÇÃO AVANÇADA")
        print("🔧"*21)
        print("\n1 - Adicionar entrada de log")
        print("2 - Visualizar logs do sistema")
        print("3 - Retornar")
        print("🔧"*21)
    
    def activate(self):
        """Ativa o sistema Kogami"""
        while True:
            self._interface()
            choice = input(">>  ")
            
            if choice == "1":
                clear()
                print("\n📝 Digite a entrada de log:")
                entry = input(">> ")
                if entry.strip():
                    self._save_entry(entry)
                    print("✅ Entrada registrada no sistema!\n")
                else:
                    print("❌ Entrada não pode estar vazia!\n")
                input("Pressione Enter para continuar...")
                    
            elif choice == "2":
                self._load_entries()
                input("\nPressione qualquer tecla...")
                
            elif choice == "3":
                clear()
                print("🔧 Fechando painel de configuração...")
                time.sleep(1)
                break
                
            else:
                clear()
                print("❌ Opção inválida.\n")
                input("Pressione Enter para continuar...")

class Jogo:
    def __init__(self):
        self.run = True
        self.menu = True
        self.playing = False
        self.rules = False
        self._secret_sequence = ['W', 'W', 'S', 'S', 'A', 'D', 'A', 'D', 'B', 'A']
        self._input_buffer = []
        self._kogami = Kogami()
        
    def _check_sequence(self, key):
        """Verifica sequência especial"""
        self._input_buffer.append(key.upper())
        
        # Mantém buffer limitado
        if len(self._input_buffer) > 10:
            self._input_buffer.pop(0)
        
        # Verifica sequência
        if self._input_buffer == self._secret_sequence:
            clear()
            print("\n🎉 MODO DESENVOLVEDOR ATIVADO! 🎉")
            time.sleep(2)
            self._input_buffer = []
            return True
        return False
        
    def exit_game(self):
        """Encerra aplicação"""
        clear()
        print("\nObrigado por jogar!")
        time.sleep(1)
        self.run = False
        self.main_menu = False
        self.playing = False
        self.rules = False

    def main_menu(self):
        clear()
        print_dragao()

        
        while self.main_menu:
            clear()
            print_dragao()
            print("="*100)
            print("\t\t\t         MENU PRINCIPAL")
            print("="*100)
            print("1. INICIAR JOGO")
            print("2. CARREGAR JOGO")
            print("3. REGRAS")
            print("4. SAIR")
            print("="*100)

            
            try:
                choice = input(">> ").strip()
                
                # Processa entrada para sequência especial
                for char in choice:
                    if self._check_sequence(char):
                        self._kogami.activate()
                        clear()
                        print("Retornando ao menu principal...")
                        time.sleep(1)
                        break
                else:
                    # Menu padrão
                    if choice == "1":
                        clear()
                        print("Iniciando jogo...")
                        self.play()
                    elif choice == "2":
                        clear()
                        print("Carregando jogo...")
                        self.load_game()
                    elif choice == "3":
                        clear()
                        print("Mostrando regras...")
                        self.show_rules()
                    elif choice == "4":
                        self.exit_game()
                    else:
                        clear()
                        print("Opção inválida")
                        time.sleep(1)
                        
            except KeyboardInterrupt:
                clear()
                print("\n\nEncerrando aplicação...")
                time.sleep(1)
                self.exit_game()
                break
    
    def play(self):
        """Modo jogo"""
        print("\nFuncionalidade em desenvolvimento!")
        input("Pressione Enter para continuar...")
        clear()
        print("Retornando ao menu principal...")
        time.sleep(1)
    
    def load_game(self):
        """Carrega save"""
        print("\nSistema de save em desenvolvimento!")
        input("Pressione Enter para continuar...")
        clear()
        print("Retornando ao menu principal...")
        time.sleep(1)
    
    def show_rules(self):
        """Exibe informações do jogo"""
        print("\n" + "="*40)
        print("                SOBRE")
        print("="*40)
        print("Sistema em desenvolvimento!")
        print("Nota de Desenvolvedor: Preciso terminar isso aqui ksks")
        print("="*40)
        input("Pressione Enter para continuar...")
        clear()
        print("Retornando ao menu principal...")
        time.sleep(1)

if __name__ == "__main__":
    jogo = Jogo()
    jogo.main_menu()