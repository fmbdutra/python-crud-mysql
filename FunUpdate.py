'''
Fabiano Matheus B. Dutra
Faculdade SENAI de Tecnologia Porto Alegre
Análise e Desenvolvimento de Sistema
Python CRUD and MYSQL
'''

from PHPBanco.FuncionarioTO import FuncionarioTO
from PHPBanco.FuncionarioDAO import FuncionarioDAO


class FunUpdate:

    def getUp(self):
        id = input("Digite ID: ")

        print("Digite os valores a atualizar. Caso não queria atualizar o que pede, pressione ENTER.")
        print()

        nome = input("Digite o nome: ")
        nasc = input("Digite a data de nascimento (ano(4)-mês-dia): ")
        salario = input("Digite o salario: ")
        foto = input("Digite arquivo da foto: ")

        f = FuncionarioTO(nome, nasc, salario, foto, id)
        d = FuncionarioDAO()
        d.update(f)