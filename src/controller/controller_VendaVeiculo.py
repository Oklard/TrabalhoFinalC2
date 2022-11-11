from model.Cliente import Cliente
from model.Veiculo import Veiculo
from model.VendaVeiculo import VendaVeiculo
from conexion.oracle_queries import OracleQueries

class Controller_VendaVeiculo:
    def __init__(self):
        pass
        
    def inserir_venda(self) -> VendaVeiculo:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo idVenda
        idVenda = input("idVenda (Novo): ")

        if self.verifica_existencia_venda(oracle, idVenda):
            # Solicita ao usuario o novo valorVenda
            valorVenda = input("valorVenda (Novo): ")
            # Insere e persiste o novo cliente
            oracle.write(f"insert into VendaVeiculo values ('{idVenda}', '{valorVenda}')")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_venda = oracle.sqlToDataFrame(f"select idVenda, valorVenda from cliente where idVenda = '{idVenda}'")
            # Cria um novo objeto Cliente
            nova_venda = VendaVeiculo(df_venda.idVenda.values[0], df_venda.valorVenda.values[0])
            # Exibe os atributos do novo cliente
            print(nova_venda.to_string())
            # Retorna o objeto novo_cliente para utilização posterior, caso necessário
            return nova_venda
        else:
            print(f"O idVenda {idVenda} já está cadastrado.")
            return None

    def atualizar_venda(self) -> VendaVeiculo:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do cliente a ser alterado
        idVenda = int(input("idVenda da venda que deseja alterar o valor da venda: "))

        # Verifica se o cliente existe na base de dados
        if not self.verifica_existencia_venda(oracle, idVenda):
            # Solicita a nova descrição do cliente
            novo_valor = input("valorVenda (Novo): ")
            # Atualiza o valorVenda do cliente existente
            oracle.write(f"update VendaVeiculo set valorVenda = '{novo_valor}' where idVenda = {idVenda}")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_venda = oracle.sqlToDataFrame(f"select idVenda, valorVenda from VendaVeiculo where idVenda = {idVenda}")
            # Cria um novo objeto cliente
            venda_atualizada = VendaVeiculo(df_venda.idVenda.values[0], df_venda.valorVenda.values[0])
            # Exibe os atributos do novo cliente
            print(venda_atualizada.to_string())
            # Retorna o objeto cliente_atualizado para utilização posterior, caso necessário
            return venda_atualizada
        else:
            print(f"O idVenda {idVenda} não existe.")
            return None

    def excluir_venda(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o idVenda do Cliente a ser alterado
        idVenda = int(input("idVenda da venda que irá excluir: "))        

        # Verifica se o cliente existe na base de dados
        if not self.verifica_existencia_venda(oracle, idVenda):            
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_venda = oracle.sqlToDataFrame(f"select idVenda, valorVenda from VendaVeiculo where idVenda = {idVenda}")
            # Revome o cliente da tabela
            oracle.write(f"delete from VendaVeiculo where idVenda = {idVenda}")            
            # Cria um novo objeto Cliente para informar que foi removido
            venda_excluida = VendaVeiculo(idVenda.values[0], df_venda.valorVenda.values[0])
            # Exibe os atributos do cliente excluído
            print("Venda Removida com Sucesso!")
            print(venda_excluida.to_string())
        else:
            print(f"O idVenda {idVenda} não existe.")

    def verifica_existencia_venda(self, oracle:OracleQueries, idVenda:str=None) -> bool:
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_venda = oracle.sqlToDataFrame(f"select idVenda, valorVenda from cliente where idVenda = {idVenda}")
        return df_venda.empty