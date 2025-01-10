class Animal:
    def __init__(self, nome, habitat):
        self.nome = nome  
        self.habitat = habitat  

    def emitir_som(self):
        return "Som de animal"

    def detalhes(self):
        return f"Nome: {self.nome}, Habitat: {self.habitat}"


class Mamifero(Animal):
    def __init__(self, nome, habitat, tem_pelos=True):
        super().__init__(nome, habitat)
        self.tem_pelos = tem_pelos 

    def emitir_som(self):
        return "Som de mamífero"

class Passaro(Animal):
    def __init__(self, nome, habitat, pode_voar=True):
        super().__init__(nome, habitat)
        self.pode_voar = pode_voar 

    def emitir_som(self):
        return "Canto de ave"

    def voar(self):
        return "Estou voando!" if self.pode_voar else "Não consigo voar."

class Peixe(Animal):
    def __init__(self, nome, habitat, tem_escamas=True):
        super().__init__(nome, habitat)
        self.tem_escamas = tem_escamas  

    def emitir_som(self):
        return "Som de bolhas"

def main():

    gato = Mamifero("Gato", "Doméstico")
    pardal= Passaro("Pardal", "Floresta", pode_voar=True)
    atum = Peixe("Atum", "Oceano")

    animais = [gato, pardal, atum]

    print("=== Detalhes dos Animais ===")
    for animal in animais:
        print(animal.detalhes())
        print(f"Som: {animal.emitir_som()}")
        if isinstance(animal, Passaro): 
            print(f"Ação: {animal.voar()}")
        print("-" * 30)


if __name__ == "__main__":
    main()
