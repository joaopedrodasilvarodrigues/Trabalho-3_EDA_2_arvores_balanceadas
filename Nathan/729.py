class No:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.esquerda = None
        self.direita = None
        self.cor = "VERMELHO"


class MyCalendar:
    def __init__(self):
        self.raiz = None

    def book(self, inicio, fim):
        if not self.raiz:
            self.raiz = No(inicio, fim)
            self.raiz.cor = "PRETO"
            return True
        return self._inserir(self.raiz, inicio, fim)

    def _inserir(self, no, inicio, fim):
        if inicio < no.fim and fim > no.inicio:
            return False
        if inicio < no.inicio:
            if not no.esquerda:
                no.esquerda = No(inicio, fim)
                return True
            return self._inserir(no.esquerda, inicio, fim)
        else:
            if not no.direita:
                no.direita = No(inicio, fim)
                return True
            return self._inserir(no.direita, inicio, fim)
