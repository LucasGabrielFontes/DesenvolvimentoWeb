class TimeFutebol:
    def __init__(self, nome, pais):
        self._nome = nome
        self._pais = pais
        self._vitorias = 0
        self._derrotas = 0

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def pais(self, pais):
        self.pais = pais

    @property
    def vitorias(self):
        return self._vitorias
    
    @vitorias.setter
    def vitorias(self, vitorias):
        if (vitorias < 0):
            print("Quantidade de vitórias inválida")
        else:
            self._vitorias = vitorias

    @property
    def derrotas(self):
        return self._derrotas
    
    @derrotas.setter
    def derrotas(self, derrotas):
        if (derrotas < 0):
            print("Quantidade de derrotas inválida")
        else:
            self._derrotas = derrotas

    def ganhar(self):
        self.vitorias += 1

    def perder(self):
        self.derrotas += 1

    @staticmethod
    def analisaSituacao(vitorias, derrotas):
        if (vitorias > derrotas):
            return "Situação boa"
        elif (derrotas > vitorias):
            return "Situação ruim"
        else:
            return "Situação razoável"
        
    def toString(self):
        return ("Time: ", self.nome, "País: ", self.pais, "Vitórias: ", self.vitorias, "Derrotas", self.derrotas)
