
class Fila:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__iterando = None
    class No:
        def __init__(self,chave):
            self.proximo = None
            self.anterior = None
            self.chave = chave
    def __len__(self):
        return self.__tamanho
    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self
    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.__primeiro
        else:
            self.__iterando = self.__iterando.proximo
        if not self.__iterando is None:
            return self.__iterando.chave
        raise StopIteration

    def __str__(self):
        formato = "["
        atual = self.__primeiro
        i=0
        while i <self.__tamanho:
            formato+=atual.chave.__repr__()
            if i<self.__tamanho -1:
                formato+=", "

            atual = atual.proximo
            i+=1
        formato+="]"
        return formato
    def enfileirar(self,chave):
        novo = self.No(chave)
        if self.__tamanho == 0:
            self.__primeiro = self.__ultimo = novo

        else:
            self.__ultimo.proximo = novo
            novo.anterior = self.__primeiro
            self.__ultimo = novo
        self.__tamanho+=1
        self.__iterando = None

    def desenfileirar(self):
        if self.__tamanho == 0:
            raise TypeError("Não há elementos para ser removido!!")
        elif self.__tamanho == 1:
            self.__primeiro = self.__ultimo = None
        elif self.__tamanho>1:
            proximo = self.__primeiro.proximo
            self.__primeiro.proximo = None
            proximo.anterior = None
            self.__primeiro = proximo
        self.__tamanho-=1
        self.__iterando = None



