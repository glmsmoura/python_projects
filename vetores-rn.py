class Vetor:
    #Inicia uma lista para a classe Vetor
    def __init__(self):
        self.coordenadas=tuple([])

    #Define a função len para objeto da Classe Vetor
    def __len__(self):
        return len(self.coordenadas)

    #Define a iteração para objeto da Classe Vetor (Subscriptable)
    def __getitem__(self, item):
        return self.coordenadas[item]

    #Define print para objeto da Classe Vetor
    def __repr__(self):
        return str(self.coordenadas)

    #Define coordenadas para objeto da Classe Vetor
    def entraCoordenadas(self):
        entrada = input("Insira as coordenadas do seu vetor, separadas por espaço\n")
        vetor = entrada.strip().split(" ")
        self.coordenadas = tuple(int(vetor[i]) for i in range(len(vetor)))


#Define produto interno entre vetores
def produtoInterno(vetor1: Vetor, vetor2: Vetor): 
    #definir vetor1 como vetor1: Vetor é chamado de tipagem estática, o que invocaria um erro caso vetor1 nao fosse objeto Vetor
    #no interpretador padrao do python, ele so ignora, mas tem alguns que implicariam com isso, como o interpretador mypy

    #esse try é chamado de tratamento de erros
    try:
        return(sum([vetor1.coordenadas[i]*vetor2.coordenadas[i] for i in range(len(vetor1))]))
    except IndexError: 
        print("Produto interno entre vetores de dimensões diferentes não está definido. ") #Printando essa mensagem e nao retornando nada, aparece None no terminal. 
        #Poderia retornar a string, mas isso é um pouco estranho.

#Define soma entre vetores
def soma(vetor1: Vetor, vetor2: Vetor):
    try:
        return(tuple([vetor1.coordenadas[i]+vetor2.coordenadas[i] for i in range(len(vetor1))]))
    except IndexError: 
        print("Soma de vetores de dimensões diferentes não está definido. ")

def multiplicar(escalar: int, vetor: Vetor):
    return(tuple([escalar*vetor.coordenadas[i] for i in range(len(vetor))]))


v1 = Vetor()
v1.entraCoordenadas()
v2 = Vetor()
v2.entraCoordenadas()
v3 = Vetor()
v3.entraCoordenadas()

print(v1, len(v1))

print(type(v1), type(v2), type(v3))

print(produtoInterno(v1, v2))
print(soma(v1, v2))
print(multiplicar(3, v1))
