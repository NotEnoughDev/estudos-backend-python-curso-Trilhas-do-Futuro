//Se quiser, colocar a estrutura das linhas 11 a 16 nas linhas 5 a 9 que te poupara 6 linhas. 
//Esse script vai ser util para Estacio ou qualquer outra instituição que estudar - Wesley, 2025

programa {
  funcao inicio() {
    cadeia nome
    inteiro idade
    real notaProva , notaTrabalho , media
    caracter turno 
    logico status

    nome = "Wesley"
    idade = 18
    notaProva = 10
    notaTrabalho = 10
    turno = 'N'
    media = (notaProva+notaTrabalho)/2
    status = (media>=7) 

    escreva("\nNome:", nome)
    escreva("\nIdade:", idade)
    escreva("\nNota da Prova:", notaProva)
    escreva("\nNota do Trabalho:", notaTrabalho)
    escreva("\nMedia das Notas:", media)
    escreva("\nTurno:", turno)
    se (status) {
      escreva("\nStatus: Aprovado :D")
    } senao {
      escreva("\nStatus: Reprovado >:C")
    }
  }
}
