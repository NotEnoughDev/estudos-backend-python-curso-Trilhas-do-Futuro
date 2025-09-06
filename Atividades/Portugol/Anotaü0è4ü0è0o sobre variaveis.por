//Essas são anotações das atividades
//Se....Senão: São variaveis condicionais onde possui uma estrutura de decisão. Exemplo:

programa {
  funcao inicio () {
    inteiro idade
    escreva ("Digite sua idade: ")
    leia(idade)
    se (idade >= 18) {escreva("\nVocê já esta velho :D")
    } senao {
      escreva("\nVocê é jovem ainda, sortudo! >:C")
    }
  }
}

//Enquanto: Enquanto é uma variavel condicional para estruturas de escolhas. Ela executa uma lista de comandos onde uma opção é verdadeira. Exemplo:

programa 
{
  funcao inicio()
   {
    caracter parar 
    parar = 'N' 

    enquanto (parar != 'S')
    {
    escreva ("deseja parar o laço? (S/N)")
    leia (parar)
    }
  }
}

//Faça.... enquanto: São variaveis condicionais onde se encontram em estruturas de repetição pós teste, ou seja, o codigo faça sera executado uma vez antes da condição da variavel enquanto seja verificada. Exemplo:

programa {
  funcao inicio() {
    real aresta, area 
    faca{ 
      escreva("Informe o valor da aresta: ")
      leia (aresta)
    } enquanto (aresta<= 0)
    area=aresta*aresta
    escreva("A area é: ", area)
  }
}

//Para: É uma variavel de controle onde pode ter um laço de repetição, ou seja, repete um bloco de comando "n" vezes

programa {
  funcao inicio() {
    inteiro tab
    para (inteiro c=1; c<=10; c++)
    {
      tab=c*3
      escreva("3 x", c, " = ", tab, "\n")
    }
  }
}

