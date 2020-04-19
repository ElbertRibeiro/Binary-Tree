import modules.createArvore


raiz = modules.createArvore.NodoArvore(40)

raiz.esquerda = modules.createArvore.NodoArvore(20)
raiz.direita = modules.createArvore.NodoArvore(60)
raiz.direita.esquerda = modules.createArvore.NodoArvore(50)
raiz.direita.direita = modules.createArvore.NodoArvore(70)
raiz.esquerda.esquerda = modules.createArvore.NodoArvore(10)
raiz.esquerda.direita = modules.createArvore.NodoArvore(30)

print("Árvore: ", raiz)
