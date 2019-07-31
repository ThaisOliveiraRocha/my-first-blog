#coding:utf-8
class Pessoa(object):
    nome = ""
    endereco = ""
    ano_nascimento = 0

    def obter_idade(self):
        return 2019 - self.ano_nascimento

class Funcionario(Pessoa):
    cargo = ""

funcionario = Funcionario()
funcionario.nome = 'Thais Rocha'
funcionario.ano_nascimento = 2000
funcionario.endereco = 'Campinas'
funcionario.salario = 3000

print('*****************************************')
print('Bem vindo ao sistema')

print("\n Nome do funcionario: ", funcionario.nome, "\n Idade: ", funcionario.obter_idade())
print("\n Salário: ", funcionario.salario)

print('*****************************************')
