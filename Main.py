'''
Fabiano Matheus B. Dutra
Faculdade SENAI de Tecnologia Porto Alegre
Análise e Desenvolvimento de Sistema
Python CRUD and MYSQL
'''

from PHPBanco.FunInsert import FunInsert
from PHPBanco.FunDelete import FunDelete
from PHPBanco.FunUpdate import FunUpdate
from PHPBanco.FunList import FunList


class Main:

    fins = FunInsert()

    fdel = FunDelete()

    fupd = FunUpdate()

    flist = FunList()

    fins.getIns()

    flist.getList()