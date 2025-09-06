//Se quiser, colocar a estrutura das linhas 11 a 16 nas linhas 5 a 9 que te poupara 6 linhas. 
//Esse script vai ser util para Estacio ou qualquer outra instituição que estudar - Wesley, 2025

programa {
  funcao inicio() {
    cadeia nome
    inteiro idade
    real notaProva , notaTrabalho , media
    caracter turno 
    logico status

    escreva("\nQual é o seu nome?: ")
    leia(nome)
    escreva("\nQual é a sua idade?: ")
    leia(idade)
    escreva("\nQual é o seu turno?(M para manha, T para Tarde, N para noite) ")
    leia(turno)
    escreva("\nQual foi a sua nota da trabalho?: ")
    leia(notaTrabalho)
    escreva("\nQual foi a sua nota do prova?: ")
    leia(notaProva)

    escreva("\nNome:", nome)
    escreva("\nIdade:", idade)
    escreva("\nTurno:", turno)
    escreva("\nNota do Trabalho:", notaTrabalho)
    escreva("\nNota do Prova:", notaProva)
    media = (notaProva+notaTrabalho)/2
    escreva("\nMedia: ", media)

    se (media>=7) {
      escreva("\nStatus: Aprovado :D")
    } senao {
      escreva("\nStatus: Reprovado >:C")
     }
   }
}