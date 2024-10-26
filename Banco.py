class Conta:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f'Saque: R$ {valor:.2f}')
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor de saque inválido ou saldo insuficiente.')

    def mostrar_extrato(self):
        print('=== Extrato ===')
        for transacao in self.extrato:
            print(transacao)
        print(f'Saldo atual: R$ {self.saldo:.2f}')


def main():
    conta = Conta()
    
    while True:
        print('\n=== Sistema Bancário ===')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Extrato')
        print('4. Sair')

        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            valor = float(input('Informe o valor a ser depositado: '))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input('Informe o valor a ser sacado: '))
            conta.sacar(valor)
        elif opcao == '3':
            conta.mostrar_extrato()
        elif opcao == '4':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida! Tente novamente.')


if __name__ == "__main__":
    main()
