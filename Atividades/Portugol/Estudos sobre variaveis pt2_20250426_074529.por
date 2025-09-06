//Hoje na aula do dia 23/04/25, fiquei 30m depois do recreio tentando descobrir como poderia colocar
//opcões de multipla escolha. Então por isso decidir fazer um jogo de multipla escolha, como
//roleplays ou rpgs. No caso, há outras maneiras de fazer isso mas primeiramente fiz como os casos de se... senão se


programa {
  funcao inicio() {
    inteiro opcao //Esta variavel pelo o que eu entendi atribui opções 
    escreva ("Aventura em Texto")
    escreva ("\n1 - Começar")
    escreva ("\nEscreva sua opção: ")
    leia (opcao)
    se (opcao==1){ //A opção 1 seria "1 - Começar"
     limpa ()
     escreva ("Você acorda no seu quarto, deitado em sua cama. O que você quer fazer?")
     escreva ("\n 1 - Levantar da cama")
     escreva ("\n 2 - Continuar a dormir")
     escreva ("\n 3 - Procurar seu telefone")
     escreva ("\n Qual é a sua opção?:")
       leia (opcao)
       se (opcao==1){
        limpa ()
        escreva ("Voce levantou de sua cama e observou seu quato. Sua cama estava desarrumada, livros bagunçados na mesa e roupas no chão o que você faz?")
        escreva ("\n 1 - Arrumar sua bagunça")
        escreva ("\n 2 - Tomar um banho e se prepara para a faxina")
        escreva ("\n 3 - Toma um banho e se prepara para sair de casa")
        escreva ("\n Qual é a sua opção?:")
        leia (opcao)
         se (opcao==1){
         	limpa ()
         	escreva ("\nVocê arrumou a bagunça")
          } senao se (opcao==2){
            limpa ()
            escreva ("\nVocê tomou um banho e se preparou para fazer a faxina")
         } senao se (opcao==3) {
         	 limpa ()
         	 escreva ("\nVocê tomou um banho e deu um role")
         }
       } senao se (opcao==2){
         escreva ("Voce continuou a dormir")
       } senao se (opcao==3){
         escreva ("Voce usou seu telefone")
       }
    } senao {
    	 limpa ()
      escreva ("Sacanagem :<")
    }

    
    
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1860; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */