'''
Fabiano Matheus B. Dutra
Faculdade SENAI de Tecnologia Porto Alegre
Análise e Desenvolvimento de Sistema
Python CRUD and MYSQL
'''


from PHPBanco.FuncionarioDAO import FuncionarioDAO
from PHPBanco.FuncionarioTO import FuncionarioTO

class FunInsert:

    def getIns(self):

        nome = input("Digite o nome: ")
        nasc = input("Digite a data de nascimento (aaaa-mm-dd): ")
        salario = input("Digite o salario: ")
        foto = input("Digite nome do arquivo da foto: ")
        id = None

        f = FuncionarioTO(nome, nasc, salario, foto, id)
        d = FuncionarioDAO()
        d.insert(f)