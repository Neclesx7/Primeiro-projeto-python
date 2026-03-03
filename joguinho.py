print("Apos uma noite de festas você acorda aprisionado em um cativeiro \n"
      "você olha pro lado e ve as seguintes opções:\n"
      "1 - Uma porta \n "
      "2 - Uma janela pequena \n"
      "Escolha uma Opção: ")
escolha1 = input()

if escolha1 == "1":
        print("Esta trancada."
              "FIM DE JOGO!!!")
        exit()

else:
        print("você pulou janela!!")

print("\n Apos você pular a janela voce tem 2 opções novamente"
      "\n 1 - na esquerda tem seguranças armados dormindo"
      "\n 2 - na direita tem cachorros famintos ")
escolha2 = input()

if escolha2 == "1":
        print("Você foi capturado. \n"
              "FIM DE JOGO!!!")
        exit()
else:
        print("Você precisa escolher se vai preferir passar \n"
              "silenciosamente pelos cachorros ou fazer uma distração \n"
              "1 - Fazer uma distração \n"
              "2 - Passar silenciosamente \n"
              "Escolha: ")

escolha3 = input()

if escolha3 == "1":
        print("você jogou um galho longe de voce e os cachorros foram atras\n"
              "e você conseguiu fugir da casa.\n"
              "FIM DE JOGO!!!")
else:
        print("eles sentiram seu cheiro e voce foi capturado."
              "\n FIM DE JOGO!!!")
        exit()