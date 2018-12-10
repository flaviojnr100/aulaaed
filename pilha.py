
class Pilha:
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
    def push(self,chave):
        novo = self.No(chave)
        if self.__primeiro is None:
            self.__primeiro = self.__ultimo = novo
        else:
            self.__primeiro.anterior = novo
            novo.proximo = self.__primeiro
            self.__primeiro = novo
        self.__iterando = None
        self.__tamanho+=1
    def pop(self):
        if self.__primeiro is None:
            raise TypeError("Não há elementos para ser removidos!!")
        elif self.__tamanho == 1:
            self.__primeiro = self.__ultimo = None
        else:
            proximo = self.__primeiro.proximo
            proximo.anterior = None
            self.__primeiro.proximo = None
            self.__primeiro = proximo
        self.__tamanho-=1
        self.__iterando = None







