class Estudante:
    def __init__(self, nome, idade, matricula): # Método construtor ou método especial
        self._nome = nome # O underline indica que os atributos só devem ser modificados através dos métodos devidos
        self._idade = idade
        self._matricula = matricula

    @property # Define o método get que é chamado como se estivesse acessando o atributo diretamente (antes do setter)
    def nome(self):
        return self._nome

    @nome.setter # Define o método set que é chamado como se estivesse modificando o atributo diretamente
    def nome(self, nome):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if (idade < 0):
            print("Idade inválida")
        else:
            self._idade = idade

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter 
    def matricula(self, matricula):
        self._matricula = matricula
    
estudante = Estudante("Lucas Gabriel", 19, "20230015665")

estudante.idade = -8 # Não modifica o atributo diretamente. Utiliza os métodos próprios para isso
print(estudante.idade)