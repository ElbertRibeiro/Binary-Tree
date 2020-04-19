import modules.createArvore

'''
raiz=NodoArvore(40)

raiz.esquerda=NodoArvore(20)
raiz.direita=NodoArvore(60)
raiz.direita.esquerda=NodoArvore(50)
raiz.direita.direita=NodoArvore(70)
raiz.esquerda.esquerda=NodoArvore(10)
raiz.esquerda.direita=NodoArvore(30)
'''

raiz = modules.createArvore.NodoArvore(3)
raiz.esquerda = modules.createArvore.NodoArvore(5)
raiz.direita  = modules.createArvore.NodoArvore(1)
print("Árvore: ", raiz)
