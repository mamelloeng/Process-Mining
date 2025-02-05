class ListaController:
    def __init__(self):
        self.lista = []

    def adicionar_inicio(self, elemento):
        self.lista.insert(0, elemento)

    def adicionar_fim(self, elemento):
        self.lista.append(elemento)

    def remover_elemento(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            print("Elemento não encontrado na lista.")

    def tamanho(self):
        return len(self.lista)

    def imprimir_lista(self):
        print("Lista:", self.lista)

    def esvaziar_lista(self):
        self.lista.clear()

# Exemplo de uso
def main():
    lista = ListaController()
    lista.adicionar_inicio(10)
    lista.adicionar_fim(20)
    lista.adicionar_inicio(5)
    lista.imprimir_lista()
    lista.remover_elemento(10)
    lista.imprimir_lista()
    print("Tamanho da lista:", lista.tamanho())
    lista.esvaziar_lista()
    lista.imprimir_lista()

if __name__ == "__main__":
    main()