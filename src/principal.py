from controller.controller_VendaVeiculo import Controller_VendaVeiculo
from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_Veiculo import Controller_Veiculo
from controller.controller_Cliente import Controller_Cliente
from controller.controller_VendaVeiculo import Controller_VendaVeiculo

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_Veiculo = Controller_Veiculo()
ctrl_cliente = Controller_Cliente()
ctrl_VendaVeiculo = Controller_VendaVeiculo()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_veiculo()            
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_cliente()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_vendaVeiculo()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_veiculo = ctrl_Veiculo.inserir_veiculo()
    elif opcao_inserir == 2:
        novo_cliente = ctrl_cliente.inserir_cliente()
    elif opcao_inserir == 3:
        nova_venda = ctrl_VendaVeiculo.inserir_venda()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_veiculo()
        produto_atualizado = ctrl_Veiculo.atualizar_Veiculo()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_cliente()
        cliente_atualizado = ctrl_cliente.atualizar_cliente()
        
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_vendaVeiculo()
        venda_atualizada = ctrl_VendaVeiculo.atualizar_venda()  

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_veiculo()
        ctrl_Veiculo.excluir_veiculo()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_cliente()
        ctrl_cliente.excluir_cliente()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_vendaVeiculo()
        ctrl_VendaVeiculo.excluir_venda()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-6]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()