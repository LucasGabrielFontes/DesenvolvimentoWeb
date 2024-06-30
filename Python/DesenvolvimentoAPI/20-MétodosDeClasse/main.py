class Estudante:
    def metodo_instancia(self):
        return "Método de instância" # É chamado a partir de um objeto 
    
    @classmethod
    def metodo_classe(classe):
        return "Método de classe" # É chamado a partir de uma classe
    
    @staticmethod
    def metodo_estatico():
        return "Método estático" # Não tem referência a nenhuma classe ou objeto