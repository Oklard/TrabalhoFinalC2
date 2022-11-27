from pandas import DataFrame
from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open('/home/labdatabase/Desktop/TrabalhoFinalC2/src/sql/relatorio_veiculos.sql') as f:
            self.query_relatorio_veiculo = f.read()


        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("/home/labdatabase/Desktop/TrabalhoFinalC2/src/sql/relatorio_clientes.sql") as f:
            self.query_relatorio_cliente = f.read()
    def get_relatorio_veiculo(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_veiculo))
        input("Pressione Enter para Sair do Relatório de Veiculos")

    def get_relatorio_cliente(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_cliente))
        input("Pressione Enter para Sair do Relatório de Cliente")