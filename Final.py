import random

class Funcionario:
    def __init__(self, nome_atendente):
        nome = ['Clau', 'Tays', 'Samia']
        self.nome_atendente = random.choice(nome)

    def atender(self):
        print(f'Olá {self.nome_cliente} retornaremos seu contato.')
        print(f'Cliente: {self.nome_cliente}')
        print(f'Telefone: {self.telefone_cliente}')
        print(f'Atendente: {self.nome_atendente}')
    
    def tecnicos(self):
        if self.cod_tec == 1:
            print('André:\nTécnico novato, atencioso e disposto.')
            print('Funções:\n- Atendimento\n- Instalações FTTH')
        elif self.cod_tec == 2:
            print('Charllys:\nExperiente.')
            print('Funções:\n- Responsável pela rede FTTx\n- Instalações FTTH')
        elif self.cod_tec == 3:
            print('Marcelo Pinheiro:\nO mais experiente e antigo na empresa.')
            print('Funções:\n- Atendimento\n- Instalações FTTH')

    def tec_infra(self):
        if self.cod_infra == 1:
            print(f'{self.nome_infra}:\nGerente de Infra')
            print('Funções:\n- Genrecia dos Técnicos\n- Genrecia da Rede')
        elif self.cod_infra == 2:
            print(f'{self.nome_infra}:\nResponsável pela Rede FTTx')
            print('Funções:\n- Manutenção, Planejamento e Instalação de redes FTTx\n- Instalações FTTH')

class Atendimento(Funcionario):
    def __init__(self, nome_atendente, nome_cliente, telefone_cliente):
        self.nome_cliente = input('Digite seu nome:')
        self.telefone_cliente = int(input('Digite seu telefone:'))
        Funcionario.__init__(self, None)

class Tecnico(Funcionario):
    def __init__(self, cod_tec):
        self.cod_tec = int(input('Digite o código do técnico:\n1 - André\n2 - Charllys\n3 - Marcelo Pinheiro'))
        Funcionario.__init__(self, None)

class Infra(Funcionario):
    def __init__(self, cod_infra, nome):
        self.cod_infra = int(input('Digite o código da Infra:\n1 - Marcelo Henrique\n2 - Charllys'))
        if self.cod_infra == 1:
            self.nome_infra = str('Marcelo Henrique')
        elif self.cod_infra == 2:
            self.nome_infra = str('Charllys')
        Funcionario.__init__(self, None)


print("Escolha a opção:")
print('1 - Atendimento:')
print('2 - Quadro Técnico:')
print('3 - Técnicos Infra:')
op = int(input('Digite a opção: '))

if op == 1:
    atender = Atendimento(None, None, None)
    atender = atender.atender()
elif op == 2:
    tecnico = Tecnico(None)
    tecnico = tecnico.tecnicos()
elif op == 3:
    tecnico_infra = Infra(None, None)
    tecnico_infra = tecnico_infra.tec_infra()