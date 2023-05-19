class Grafo:


    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1
        self.grafo[v-1][u-1] = 1

    def numero_vertice(self):
        print("A - O número de vértices é ")
        print(len(self.grafo))

    def numero_aresta(self):
        soma = 0
        for i in range(len(self.grafo)):
            soma += sum(self.grafo[i])
        print("B - O número de arestas é ")
        print(int(soma/2))

    def grau_minimo(self):
        minimo = 0
        for i in range(len(self.grafo)):
            if minimo == 0 or sum(self.grafo[i]) < minimo:
                minimo = sum(self.grafo[i])
        print("C - O grau mínimo é ") 
        print(minimo)
        
    def grau_maximo(self):
        maximo = 0
        for i in range(len(self.grafo)):
            if sum(self.grafo[i]) > maximo:
                maximo = sum(self.grafo[i])
        print("D - O grau máximo é ")
        print(maximo)
    
    def mostra_matriz(self):
        print("E - A matriz de adjacências é:")
        for i in range(self.vertices):
            print(self.grafo[i])
            
    def busca_em_largura(self, v):
        visitado = [[False]*len(self.grafo) for i in range(len(self.grafo))]
        busca = []
        filaAux = []
        filaAux.append(v)
        for j in range(len(self.grafo)):
            if filaAux:
                v = filaAux[0]
                busca.append(filaAux.pop(0))
            
            for i in range(len(self.grafo)):
                if self.grafo[v-1][i] == 1 and visitado[v-1][i] == False:
                    visitado[v-1][i] = True
                    visitado[i][v-1] = True
                    if not checaLista((i+1), filaAux):
                        filaAux.append(i+1)
        print("F - busca em largura")
        print(busca)
                
def checaLista (n, v):
    for i in range(len(v)):
        if v[i] == n:
            return True
            

arquivo = open('entrada.txt')

g = Grafo(int(arquivo.readline()))

for i in arquivo:
    aresta = i
    g.adiciona_aresta(int(aresta[0]),int(aresta[2]))
    
print("Aluno: Nathan Farias Dias\nRGM: 12832997-0")

g.numero_vertice()
g.numero_aresta()
g.grau_minimo()
g.grau_maximo()
g.mostra_matriz()
vertice_inicial = int(input("Qual o vertice inicial ?"))
g.busca_em_largura(vertice_inicial)