import modules.createArvore

raiz = modules.createArvore.NodoArvore(3)
raiz.esquerda = modules.createArvore.NodoArvore(5)
raiz.direita  = modules.createArvore.NodoArvore(1)
print("Árvore: ", raiz)