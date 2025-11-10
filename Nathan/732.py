class MyCalendarThree:
    def __init__(self):
        self.eventos = {}
        self.maximo = 0

    def book(self, inicio, fim):
        self.eventos[inicio] = self.eventos.get(inicio, 0) + 1
        self.eventos[fim] = self.eventos.get(fim, 0) - 1
        ativo = 0
        maximo_atual = 0
        for k in sorted(self.eventos.keys()):
            ativo += self.eventos[k]
            maximo_atual = max(maximo_atual, ativo)
        self.maximo = max(self.maximo, maximo_atual)
        return self.maximo
