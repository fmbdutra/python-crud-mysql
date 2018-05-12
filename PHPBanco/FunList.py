'''
Fabiano Matheus B. Dutra
Faculdade SENAI de Tecnologia Porto Alegre
Análise e Desenvolvimento de Sistema
Python CRUD and MYSQL
'''

from PHPBanco.FuncionarioDAO import FuncionarioDAO

class FunList:

    def getList(self):
        d = FuncionarioDAO()
        d.list()