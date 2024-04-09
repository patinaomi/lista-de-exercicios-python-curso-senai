class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self):
        valor = float(input('Digite o valor que deseja depositar: '))
        if valor < 0 :
            print('Valor não pode ser negativo')
        else:
            self.saldo += valor

        print(f"Saldo atualizado: R${round(self.saldo,2)}")

    
    def sacar(self):
        valor = float(input('Digite o valor que deseja sacar: '))
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            print(f'Saque efetuado!')
            self.saldo -= valor
        
        print(f"Saldo atualizado: R${round(self.saldo,2)}")
    
    
if __name__ == "__main__":
    c1 = ContaBancaria(50.3, 1)
    c1.sacar()
    c1.depositar()
