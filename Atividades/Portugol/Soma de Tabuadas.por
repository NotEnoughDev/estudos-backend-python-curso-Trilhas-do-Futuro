programa {
  funcao inicio() {
    inteiro numero1, numero2, tabuada1, tabuada2, tabuada3, soma
    escreva ("Qual numero você gostaria a tabuada?: ")
    leia (numero1)
    limpa()
    escreva ("Qual é o 2º numero você gostaria a 2ª tabuada?: ")
    leia (numero2)
    limpa()
    escreva ("Tabuada do ", numero1, ":", "\n")
    para (inteiro c=0; c<=10; c++){
      tabuada1=c*(numero1)
      escreva ("\n", numero1, " x ", c, " = ", tabuada1, "\n")
    }   
    escreva ("\nTabuada do ", numero2, ":", "\n")
    para (inteiro c=0; c<=10; c++){
      tabuada2=c*(numero2)
      escreva ("\n", numero2, " x ", c, " = ", tabuada2, "\n")
    }   
    inteiro opcao
    escreva ("\nVocê deseja somar as tabuadas?: ")
    escreva ("\n1 - Para sim :D")
    escreva ("\n2 - Para não :D")
    escreva ("\n\nDecida: ")
    leia (opcao)
    limpa()
    se (opcao==1){
      tabuada3 = tabuada1+tabuada2
      soma = numero1+numero2
      escreva ("\nTabuada do ", soma, ":", "\n")
      para (inteiro c=0; c<=10; c++){
      tabuada3=c*(soma)
      escreva ("\n", soma, " x ", c, " = ", tabuada3, "\n")
      }
    } senao se (opcao==2){
      escreva ("\nPoxa ;-;")
    }    
  }
}
