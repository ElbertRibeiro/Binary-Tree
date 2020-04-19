import modules.createArvore


raiz = modules.createArvore.NodoArvore(40)

raiz.esquerda = modules.createArvore.NodoArvore(20)
raiz.direita = modules.createArvore.NodoArvore(60)
raiz.direita.esquerda = modules.createArvore.NodoArvore(50)
raiz.direita.direita = modules.createArvore.NodoArvore(70)
raiz.esquerda.esquerda = modules.createArvore.NodoArvore(10)
raiz.esquerda.direita = modules.createArvore.NodoArvore(30)


#raiz = modules.createArvore.NodoArvore(3)
#aiz.esquerda = modules.createArvore.NodoArvore(5)
#raiz.direita  = modules.createArvore.NodoArvore(1)
print("Árvore: ", raiz)
