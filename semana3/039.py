class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'


if __name__ == '__main__':
    c1 = Carro('Hyundai', 'HB20', 2023)
    print(c1)
    
