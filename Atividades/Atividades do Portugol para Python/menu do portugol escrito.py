print("---------------------------------------")
print("Ol√° Mundo")
print("---------------------------------------")
print("Menu de Atividades do Portugol")
print("---------------------------------------")
print("Observa√ß√µes:")
print("\n\nClaro que o original est√° guardado na nuvem por√©m, quero avisar que os simbolos tipo \ n est√£o separados porque fica ilegivel para o Python, ele entende como comando. Quaisquer erro digitado, por favor depois corrigir. Enfim, fiquem com o script: ")

print("\n\nprograma {")
print("  funcao inicio() {")

print("\n		inteiro opcao")
print("		escreva(""Ol√° Mundo"")")
print("		escreva(""\ nBem vindo a minha atividade ''Fa√ßa voc√™ mesmo!'', onde resolvo alguns desafios!\n\n"")")
print("          escreva (""1) Autonomia de um carro\ n"')'"")
print("          escreva (""2) Parcelamento de Compras\ n"')'"")
print("          escreva (""3) Calculadora de Bonus por venda\ n"')'"")
print("          escreva (""4) Calculadora Simples\ n"')'"")
print("          escreva (""5) Calculadora de IMC\ n"')'"")
print("          escreva (""6) Conversor de Temperatura\ n"')'"")
print("          escreva (""7) Locadora de Carro\ n"')'"")
print("          escreva (""0) Sair\ n\ n"')'"")
print("          escreva (""Selecione uma op√ß√£o: "')'"")
print("          leia (opcao)")
print("          limpa ()")

print("\n          escolha (opcao){")

print("\n           caso 1:")
print("            real km, lt, autonomia")
print("            escreva (""1) Autonomia de um carro\ n\ n"')'"")
print("            escreva (""Quantos Kilometros for√£o percorridos?: "")")
print("            leia (km)")
print("            limpa()")
print("            escreva (""Quantos litros foram consumidos?" ")")
print("            leia (lt)")
print("            limpa ()")
print("            se (lt !=0){")
print("            	autonomia = km / lt")
print("            	escreva (""A autonomia do carro √©: "", autonomia," "km/litros"")")
print("            } senao {")
print("            	escreva (""Erro: A quantidade de litros ou de kilomentros consumidos n√£o pode ser zero"')'"")
print("            } pare")
            
print("\n           caso 2:")
print("            inteiro num, prestacao")
print("            escreva (""2) Parcelamento de Compras\ n\ n"')'"")
print("            escreva (""Qual foi o valor da compra?:" ")")
print("            leia (num)")
print("            limpa()")
print("            prestacao = num / 5")
print("            escreva (""O valor da compra foi de: R$ "", num," "\ n"')'"")
print("            escreva (""O valor total da presta√ß√£o foi de: R$ "", prestacao," "\ n"')'"")
print("            escreva (""O valor de cada presta√ß√£o: ," "\ n\ n"')'"")
print("            para (inteiro c = 1; c <= 5; c++){")
print("            escreva (""Presta√ß√£o"", c," ": R$ "", prestacao," "\ n"')'	"")
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
print("               escreva (""Meta: Alcan√ßada!\ n\ n"')'"")
print("               escreva (""Nome: "", nm," "\ n"')'"")
print("               escreva (""Salario Fixo: R$ "", salarioFixo," "\ n"')'"")
print("               escreva (""Quantidade de Vendas: "", vendas," "\ n"')'"") 	
print("               escreva (""Total do Salario: R$ "", salarioFinal," "\ n"')'"")
print("               escreva (""Bon√ªs: R$ "", bonus," "\ n"')'"")
print("            } senao {")
print("            	escreva (""Meta: N√£o Atingida!\ n\ n"')'"")
print("            	escreva (""Nome: "", nm," "\ n"')'"")
print("            	escreva (""Salario fixo: R$ "", salarioFixo," "'\ n"')'"")
print("            	escreva (""Quantidade de Vendas: "", vendas," "\ n"')'"")
print("            	escreva (""Total do Salario: R$ "", salarioFixo," "\ n"')'"")
print("            	escreva (""Bon√ªs: Nulo\ n"')'"")
print("            } pare")
            
print("\n           caso 4:")
print("		       escreva(""4)Calculadora Simples\ n\ n"')'"")
print("		       escreva(""\ n--- Calculadora ---\ n"')'"")
print("		       escreva(""1- Somar\ n"')'"")
print("		       escreva(""2- Substra√ß√£o\ n"')'"")
print("		       escreva(""3- Multiplica√ß√£o\ n"')'"")
print("		       escreva(""4- Divis√£o\ n"')'"")
print("		       escreva(""0- Sair\ n\ n"')'"")
print("		       escreva(""Escolha seu calculo:" ")")
print("		       leia (opcao)"    )
print("           limpa()")

print("\n           escolha (opcao){")
print("           	caso 1:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1¬∫ n√∫mero:" ")")
print("           	leia (num1)")
print("           	escreva(""Digite 2¬∫ n√∫mero:" ")")
print("           	leia (num2)")
print("           	resultado = num1 + num2")
print("           	escreva("'", num1, "+", num2, "' '="' ", resultado)")
print("           	pare")

print("\n          	caso 2:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1¬∫ n√∫mero:" ")")
print("           	leia (num1)")
print("           	escreva(""Digite 2¬∫ n√∫mero:" ")")
print("           	leia (num2)")
print("           	resultado = num1 - num2")
print("           	escreva("'", num1, "-", num2, "' '="' ", resultado)")
print("           	pare")

print("\n           	caso 3:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1¬∫ n√∫mero:" ")")
print("           	leia (num1)")
print("           	escreva(""Digite 2¬∫ n√∫mero:" ")")
print("           	leia (num2)")
print("           	resultado = num1 + num2")
print("           	escreva("'", num1, "+", num2, "' '="' ", resultado)")
print("           	pare")

print("\n           	caso 4:")
print("           	inteiro num1, num2, resultado")
print("           	escreva(""Digite 1¬∫ n√∫mero: "")")
print("           	leia (num1)")
print("           	escreva(""Digite 2¬∫ n√∫mero: "")")
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
print("           escreva(""Qual √© o seu nome?:" ")")
print("           leia (nome)")
print("           limpa()")
print("           escreva(""Qual √© a sua idade?:" ")")
print("           leia (idade)")
print("           limpa()")
print("           escreva(""Qual √© o seu peso?:" ")")
print("           leia (peso)")
print("           limpa()")
print("           escreva(""Qual √© a sua altura?:" ")")
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
print("        ‡   }w!lcO Ce …mc 4- ≤5){ +	
pranl™∞ 4 ††&( "   %QC“evq0*"\0ÍCla3sIaicwdo8!SocupecÌ""')ri2i~v8" `hb      0ub2%,qo c jm∞} 319 {")
0ry.t "         Ñ  ! erÈpd6a)"‚‹$vQ|ArÛmÙysq$:$Kg'Ykfade"")2)U
xfin\*' " !  $!¢0!})pave"(
prmn\("  l   '†b,)g1co>:&ÈÕ
q∞i,u(   5&  1·g{crmva (*&6i3Co^vecsg˙(`d$Tmmqa3tb!\ |X l"%)')M
ri(t * `∞(  † !e3'Úeva`!j"[,√Çl$Oqfo)L ~ßI')
psind("t ` *"*")† ÌssÚmva 8c:Por$faqop. selUcife(a(gR√%√¶g&ba`vlÃ–erct’va†qqE(dtsM
e0q{d` a comvUr3√£O>\ n] n`&'"B©	L0rHnt( # (h®$ 1 §ËuscreVÈ5)f*7-&K≈lcau-†xara Fi``%njtit\ l¢'kßhç
rktà¢      ( 0† %s¶r'v° $¶b,!V`h2EÆHiia rar·0CelSium}($'™%)áp2ÈÓT(" ∞ ``$$ )#eSbrewÂ`)Ëb04[aËv\ ~\ f*')$Ø
p≤)nt("  J( 4≤b Ä$Ûc#stva ,&"DioiTe cµ· o`ÂßG+k:""*©≤°ér≤)mt("  `" £§† !°lei! 8o`ceO+"/ü
∞ri.t™"( 0†   † 0!lÈmpk(9")ÆI
pzymt(6|6 a    b †É¡ÛkÔlhÈF(ov#A©s#-≠
lpinw,´‡
 b "18  `'aa;o 1:`iç
qpmÓt,  !     ê!  v5el®ldm2Knyk´c~l G·jreniwi~"-çZ`sÈ~vH !$  !0  `$$}Û#reva©#:—uEnd√≠!y!uempePatury8em"AelrI}m?8" -")hvan)"¢!†$ah`( "2iÂi° (4ÂL0Iiac©mn!"(
pÚIL~*"     (§e"$"Ï	opq(90)ç
pryNu("%   `   `   fahn*eit } (eeepIniC`al`  9 - 5)%;$3#¢hprilt)
$`!!`  6 b E1rrewa(Rbi0tÂy`usgtwzqe-`FÈh“evheit ´©!Dm6 b, dAlPU~jeaÙ- †"¬j¢b-( rkdd*‰ 0$2  ·q pbÂ#-

pÍIod(0\J0°0§  $ †asso†≤:"-ù
xzin4(*†`  ("$"††`r%Îl(tul0InÌfiah(!celsÈuk 9*tvknu0  `  !( $  esbrev!h:"QıCl†√©ha,de|eÂÚq∂}r‡ f]0Fih2enlgÈt?: r≤)/9MHprinÅf $ 0p h  "8!l$Ca§∏temp	fibkil©"+ç+Úint®"·!   9 $`& "¯impa()')m
qÚhnu,&a *!  )$"#!aelkiıI!ø ÙgmxLnicial ) 273j5¢)J0viwv  † "(h  ((a "es#reva("£  vAm@eaapuÚe`dm(elsaum!S©`dz$#,!„ansyum,*2⁄∫b+©`1Mxpqov)∞  `$0"1 d}!xarD2©Mé0riNlF J$ ‡2! †  #a{Ô ª2≤)Ö$!  i`d·:  ÖJ∞s…nd("\n|n	 00 y#iHlpi~s(2( |"+
v~int*¢˝¢)