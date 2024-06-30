# Os objetos instaciados a partir de classes criadas sao mutaveis

class Estudante:
    def setNome(self, nome): # Na chamada do metodo, o python passa como primeiro parametro a referencia ao objeto que, aqui, eu chamei de this
        self.nome = nome 

estudante = Estudante()
estudante.nome = "Lucas Gabriel" # Simplesmente cria o atributo nome - apenas para esse objeto
print(estudante.nome)

estudante.setNome("Gabriel Lucas")
print(estudante.nome)
