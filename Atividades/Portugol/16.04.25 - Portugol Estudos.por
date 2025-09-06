//Esse arquivo é o primeiro arquivo em Portugol que dedico a estudos onde estou aprendendo no curso do Grau Tecnico pelo Trilhas do Futuro, no dia 16/04/25
  //Entrada: Entra informação; no caso, o usuario coloca a informação.
  //Saida: Sai informação; no caso, essa informação é mostrada.

programa {   
  funcao inicio() { 
    escreva ("Olá, Mundo") //Apenas escrevi para dar sorte na hora de escrever, tradição de programadores :)
    inteiro numero
     escreva ("\nDigite seu numero: ", numero) 
     leia(numero)
     escreva("Seu numero é: ", numero)
     inteiro numero2
       escreva("\n Digite um numero para somar", numero2)
       leia(numero2)
       escreva("\n O resultado é:", numero+numero2)
  }
}

//Comandos:
// "\n" é um comando para tacar um texto para baixo no console/terminal
// "programa" é o comando que criar o programa
// Abre chaves "{" é o simbolo que inicia o programa. 
// "cadeia" é uma variavel string, ou seja, uma variavel que armazena dados como caracteres, numeros, etc. 
   //Observação: Se você fazer duas ou mais cadeias e soma las, você ira apenas agrupar as palavras, ou seja, se na cadeia1 escreveu 2 e na cadeia2 4
   //e na cadeia 3 6, o resultado será: 246 e não 12. Exemplo:

programa {
  funcao inicio() {
    cadeia palavra
     escreva ("\nDigite sua primeira palavra para uma frase:", palavra)
     leia(palavra)
     escreva("\nA primeira palavra é:", palavra)
     cadeia palavra2
      escreva ("\nDigite sua segunda palavra para uma frase:", palavra2)
      leia(palavra2)
      escreva("\nA segunda palavra é:", palavra2)
      cadeia palavra3
       escreva ("\nDigite sua terceira palavra para uma frase:", palavra3)
       leia(palavra3)
       escreva("\nA terceira palavra é:", palavra3)
       cadeia frase
        escreva("\nSua frase é:", palavra ,  palavra2 , palavra3) //Ou "palavra + palavra 2 + palavra3"
        frase 
  }
}

// "inteiro" é uma variavel que reconhece um numero como numero inteiro, ou seja, sem casa decimal.
// "leia" e "escrever" é auto explicatorio
