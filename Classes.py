from nova_classe import msg,modelando,todas,valor
from time import sleep


class dinheiro:

    def __init__(self):
        msg()

    def menu(self):
        self.real = input("Valor em R$: ").strip()
        if self.real.isdecimal():
            self.real = float(self.real)
        else:
            while not self.real.isnumeric():
                self.real = input("Valor em R$: ").strip()
                if self.real.isdecimal():
                    self.real = float(self.real)
                    break
                else:
                    continue

        print()
        modelando(todas)
        self.converter = float(input("Escolha a moeda de conversão: "))
        print()
        self.alterar()

    def saida(self):
        sair = input("Sair [S/N]: ")[0].upper().strip()
        if len(sair)<0:
            print('Você precisa digitar algo!')
        while not sair.isalpha() or sair not in 'SsNn':
            sair = input("Por favor digite apenas S ou N: ")[0].upper().strip()
        if sair == "S":
            exit(0)
        elif sair == "N":
            print()
            self.menu()
        elif 'SN' not in sair:
            print("Digite Apenas S ou N !")
        elif len(sair)<0:
            print('Você precisa digitar algo!')

    def alterar(self):

        if self.converter == 1:
            print(f'Aguarde enquanto convertemos...')
            sleep(2)
            print(f'\nO valor R${self.real:.2f} em US$ (Dólares) = US${self.real * valor[0]:.2f}\n'.replace('.',','))

        elif self.converter == 2:
            print(f'Aguarde enquanto convertemos...')
            sleep(2)
            print(f'\nO valor R${self.real:.2f} em £ (libra) = £{self.real * valor[1]:.2f}\n'.replace('.',','))

        elif self.converter == 3:
            print(f'Aguarde enquanto convertemos...')
            sleep(2)
            print(f'\nO valor R${self.real:.2f} em ¥ (Iene) = ¥{self.real * valor[2]:.2f}\n'.replace('.',','))

        elif self.converter == 4:
            print(f'Aguarde enquanto convertemos...')
            sleep(2)
            print(f'\nO valor R${self.real:.2f} em ¥ (Iene) = ¥{self.real * valor[2]:.2f}\n'.replace('.',','))

        self.saida()





