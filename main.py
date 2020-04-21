#import modules.tree
#import modules.searchPreOrdem

import modules.tree

#listar arvore
#print(modules.tree.funTree())


# pre-oredem
# print(modules.searchPreOrdem.funSearch())


arv = modules.tree.Tree()
print("Programa Arvore Binaria")
opcao = 0
while opcao != 5:

     print("Entre com a opcao:")
     print(" --- 1: Inserir")
     print(" --- 2: Excluir")
     print(" --- 3: Pesquisar")
     print(" --- 4: Exibir")
     print(" --- 5: Sair do programa")
     
     opcao = int(input("-> "))
     if opcao == 1:
          x = int(input(" Informe o valor -> "))
          arv.inserir(x)
     elif opcao == 2:
          x = int(input(" Informe o valor -> "))
          if arv.remover(x) == False:
               print(" Valor nao encontrado!")
     elif opcao == 3:
          x = int(input(" Informe o valor -> "))
          if arv.buscar(x) != None:
               print(" Valor Encontrado")
          else:
               print(" Valor nao encontrado!")	 
     elif opcao == 4:
          arv.caminhar()
     elif opcao == 5:
          break