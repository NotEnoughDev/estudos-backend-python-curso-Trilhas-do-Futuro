print("---------------------------------------")
print("Olá Mundo")
print("---------------------------------------")
print("Menu de Atividades do Portugol")
print("---------------------------------------")
print("Observações:")
print("\n\nClaro que o original está guardado na nuvem porém, quero avisar que os simbolos tipo \ n estão separados porque fica ilegivel para o Python, ele entende como comando. Quaisquer erro digitado, por favor depois corrigir. Enfim, fiquem com o script: ")

print("\n\nprograma {")
print("  funcao inicio() {")

print("\n		inteiro opcao")
print("		escreva(""Olá Mundo"")")
print("		escreva(""\ nBem vindo a minha atividade ''Faça você mesmo!'', onde resolvo alguns desafios!\n\n"")")
print("          escreva (""1) Autonomia de um carro\ n"')'"")
print("          escreva (""2) Parcelamento de Compras\ n"')'"")
print("          escreva (""3) Calculadora de Bonus por venda\ n"')'"")
print("          escreva (""4) Calculadora Simples\ n"')'"")
print("          escreva (""5) Calculadora de IMC\ n"')'"")
print("          escreva (""6) Conversor de Temperatura\ n"')'"")
print("          escreva (""7) Locadora de Carro\ n"')'"")
print("          escreva (""0) Sair\ n\ n"')'"")
print("          escreva (""Selecione uma opção: "')'"")
print("          leia (opcao)")
print("          limpa ()")

print("\n          escolha (opcao){")

print("\n           caso 1:")
print("            real km, lt, autonomia")
print("            escreva (""1) Autonomia de um carro\ n\ n"')'"")
print("            escreva (""Quantos Kilometros forão percorridos?: "")")
print("            leia (km)")
print("            limpa()")
print("            escreva (""Quantos litros foram consumidos?" ")")
print("            leia (lt)")
print("            limpa ()")
print("            se (lt !=0){")
print("            	autonomia = km / lt")
print("            	escreva (""A autonomia do carro é: "", autonomia," "km/litros"")")
print("            } senao {")
print("            	escreva (""Erro: A quantidade de litros ou de kilomentros consumidos não pode ser zero"')'"")
print("            } pare")
            
print("\n           caso 2:")
print("            inteiro num, prestacao")
print("            escreva (""2) Parcelamento de Compras\ n\ n"')'"")
print("            escreva (""Qual foi o valor da compra?:" ")")
print("            leia (num)")
print("            limpa()")
print("            prestacao = num / 5")
print("            escreva (""O valor da compra foi de: R$ "", num," "\ n"')'"")
print("            escreva (""O valor total da prestação foi de: R$ "", prestacao," "\ n"')'"")
print("            escreva (""O valor de cada prestação: ," "\ n\ n"')'"")
print("            para (inteiro c = 1; c <= 5; c++){")
print("            escreva (""Prestação"", c," ": R$ "", prestacao," "\ n"')'	"")
print("            } pare")
print("           caso 3:")
print("            real salarioFixo, vendas, salarioFinal, bonus")
print("            cadeia nm")
print("            escreva (""3) Calculadora de Bonus por venda\ n\ n"')'"")
print("            escreva (""Digite seu nome: "')'"")
print("            leia (nm)")
print("            limpa()")
print("            escreva (""Digite seu salario fixo: "')'"")
print("            leia (salarioFixo)")
print("            limpa()")
print("            escreva (""Digite a quantidade de vendas: "')'"")
print("            leia (vendas)")
print("            limpa()")
print("            se (vendas>=20){")
print("               bonus = salarioFixo * 0.15")
print("               salarioFinal = salarioFixo + bonus")
print("               escreva (""Meta: Alcançada!\ n\ n"')'"")
print("               escreva (""Nome: "", nm," "\ n"')'"")
print("               escreva (""Salario Fixo: R$ "", salarioFixo," "\ n"')'"")
print("               escreva (""Quantidade de Vendas: "", vendas," "\ n"')'"") 	
print("               escreva (""Total do Salario: R$ "", salarioFinal," "\ n"')'"")
print("               escreva (""Bonûs: R$ "", bonus," "\ n"')'"")
print("            } senao {")
print("            	escreva (""Meta: Não Atingida!\ n\ n"')'"")
print("            	escreva (""Nome: "", nm," "\ n"')'"")
print("            	escreva (""Salario fixo: R$ "", salarioFixo," "'\ n"')'"")
print("            	escreva (""Quantidade de Vendas: "", vendas," "\ n"')'"")
print("            	escreva (""Total do Salario: R$ "", salarioFixo," "\ n"')'"")
print("            	escreva (""Bonûs: Nulo\ n"')'"")
print("            } pare")
            
print("\n           caso 4:")
print("		       escreva(""4)Calculadora Simples\ n\ n"')'"")
print("		       escreva(""\ n--- Calculadora ---\ n"')'"")
print("		       escreva(""1- Somar\ n"')'"")
print("		       escreva(""2- Substração\ n"')'"")
print("		       escreva(""3- Multiplicação\ n"')'"")
print("		       escreva(""4- Divisão\ n"')'"")
print("		       escreva(""0- Sair\ n\ n"')'"")
print("		       escreva(""Escolha seu calculo:" ")")
print("		       leia (opcao)"    )
print("           limpa()")

print("\n           escolha (opcao){")
print("           	caso 1:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1º número:" ")")
print("           	leia (num1)")
print("           	escreva(""Digite 2º número:" ")")
print("           	leia (num2)")
print("           	resultado = num1 + num2")
print("           	escreva("'", num1, "+", num2, "' '="' ", resultado)")
print("           	pare")

print("\n          	caso 2:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1º número:" ")")
print("           	leia (num1)")
print("           	escreva(""Digite 2º número:" ")")
print("           	leia (num2)")
print("           	resultado = num1 - num2")
print("           	escreva("'", num1, "-", num2, "' '="' ", resultado)")
print("           	pare")

print("\n           	caso 3:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1º número:" ")")
print("           	leia (num1)")
print("           	escreva(""Digite 2º número:" ")")
print("           	leia (num2)")
print("           	resultado = num1 + num2")
print("           	escreva("'", num1, "+", num2, "' '="' ", resultado)")
print("           	pare")

print("\n           	caso 4:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1º número: "")")
print("           	leia (num1)")
print("           	escreva(""Digite 2º número: "")")
print("           	leia (num2)")
print("           	resultado = num1 + num2")
print("           	escreva("'", num1, "+", num2, "' '="' ", resultado)")
print("           	pare")
print
print("           	caso 0:")
print("           	escreva'('""Tchau :D!""')'")
print("           	pare")         	
print("            } pare")

print("\n		       caso 5:")
print("           real idade, peso, altura, imc")
print("           cadeia nome")
print("           escreva(""5)Calculo de IMC\ n\ n"')'"")
print("           escreva(""Qual é o seu nome?:" ")")
print("           leia (nome)")
print("           limpa()")
print("           escreva(""Qual é a sua idade?:" ")")
print("           leia (idade)")
print("           limpa()")
print("           escreva(""Qual é o seu peso?:" ")")
print("           leia (peso)")
print("           limpa()")
print("           escreva(""Qual é a sua altura?:" ")")
print("           leia (altura)")
print("           limpa()")
print("           imc = peso / altura*altura")
print("           escreva(""\ nNome: "", nome"')'"")
print("           escreva(""\ nIdade: "", idade""')")
print("           escreva(""\ nPeso: "", peso""')")
print("           escreva(""\ nAltura: "", altura"")""")
print("           escreva(""\ nIMC: "", imc"")""")
print("            se (imc < 18.5){")
print("      	       escreva(""\ nClassificado: Abaixo do Peso""')")
print("            } senao se (imc >= 18.5){")
print("      	       escreva(""\ nClassificado: Peso normal""')")
print("        �   }w!lcO Ce �mc 4- �5){ +	
pranl�� 4 ��&( "   %QC�evq0*"\0�Cla3sIaicwdo8!Socupec�""')ri�2i~v8" `hb      0ub2%,qo c jm�} 319 {")
0ry.t "         �  ! er�pd6a)"��$vQ|Ar�m�ysq$:$Kg'Ykfade"")2)U
xfin\*' " !  $!�0!})pave"(
prmn\("  l   '�b,)g1co>:&��
q�i,u(   5&  1�g{crmva (*&6i3Co^vecsg�(`d$Tmmqa3tb!\ |X l"%)')M
�ri(t * `�(  � !e3'�eva`!j"[,Âl$Oqfo)L ~�I')
psind("t ` *"*")� �ss�mva 8c:Por$faqop. selUcife(a(gR�%æg&ba`vl��erct�va�qqE(dtsM
e0q{d` a comvUr3ãO>\ n] n`&'"B�	L0rHnt( # (h�$ 1 ��uscreV�5)f*7-&K�lcau-�xara Fi``%njtit\ l�'k�h�
�rkt��      ( 0� %s�r'v� $�b,!V`h2E�Hiia rar�0CelSium}($'�%)�p2��T(" � ``$$ )#eSbrew�`)�b04[a�v\ ~\ f*')$�
p�)nt("  J( 4�b �$�c#stva ,&"DioiTe c�� o`�G+k:""*����r�)mt("  `" ��� !�lei! 8o`ceO+"/�
�ri.t�"( 0�   � 0!l�mpk(9")�I
pzymt(6|6 a    b ����k�lh�F(ov#A�s#-�
lpinw,��
 b "18  `'aa;o 1:`i�
qpm�t,  !     �!  v5el�ldm2Knyk�c~l G�jreniwi~"-�Z`s�~vH !$  !0  `$$}�#reva�#:�uEndí!y!uempePatury8em"AelrI}m?8" -")hvan)"�!�$ah`( "2i�i� (4�L0Iiac�mn!"(
p�IL~*"     (�e"$"�	opq(90)�
pryNu("%   `   `   fahn*eit } (eeepIniC`al`  9 - 5)%;$3#�hprilt)
$`!!`  6 b E1rrewa(Rbi0t�y`usgtwzqe-`F�h�evheit ��!Dm6 b, dAlPU~jea�- �"�j�b-( rkdd*� 0$2  �q pb�#-

p�Iod(0\J0�0�  $ �asso��:"-�
xzin4(*�`  ("$"��`r%�l(tul0In�fiah(!cels�uk 9*tvknu0  `  !( $  esbrev!h:"Q�Cl�éha,de|e��q�}r� f]0Fih2enlg�t?: r�)/9MHprin�f $ 0p h  "8!l$Ca��temp	fibkil�"+�+��int�"�!   9 $`& "�impa()')m
q�hnu,&a *!  )$"#!aelki�I!� �gmxLnicial ) 273j5�)J0viwv  � "(h  ((a "es#reva("�  vAm@eaapu�e`dm(elsaum!S�`dz$#,!�ansyum,*2ںb+�`1Mxpqov)�  `$0"1 d}!xarD2�M�0riNlF J$ �2! �  #a{� �2�)�$!  i`d�:  �J�s�nd("\n|n	 00 y#iHlpi~s(2( |"+
v~int*���)