'''
Fabiano Matheus B. Dutra
Faculdade SENAI de Tecnologia Porto Alegre
Análise e Desenvolvimento de Sistema
Python CRUD and MYSQL
'''

from PHPBanco.FuncionarioTO import FuncionarioTO
from PHPBanco.FuncionarioDAO import FuncionarioDAO


class FunDelete:

    def getDel(self):
        id = input("Digite o ID para delete: ")
        nasc = ''
        nome = ''
        foto = ''
        salario = ''

        f = FuncionarioTO(nome, nasc, salario, foto, id)
        d = FuncionarioDAO()
        d.delete(f)