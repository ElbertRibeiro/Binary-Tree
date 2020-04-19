import modules.createArvore


raiz = modules.createArvore.NodoArvore(50)

raiz.esquerda = modules.createArvore.NodoArvore(17)
raiz.direita = modules.createArvore.NodoArvore(76)

raiz.direita.esquerda = modules.createArvore.NodoArvore(54)

raiz.esquerda.esquerda = modules.createArvore.NodoArvore(9)
raiz.esquerda.direita = modules.createArvore.NodoArvore(23)

print("Árvore: ", raiz)
