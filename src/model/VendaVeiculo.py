from datetime import date
class VendaVeiculo:
    def __init__(self, 
                 idVenda:int=None,
                 dataVenda:date=None
                 ):
        ### SETTERS ###
        def set_idVenda(self, idVenda:int,dataVenda):
            self.idVenda = idVenda
            self.dataVenda = dataVenda
        
        ### GETTERS ###

    def get_idVenda(self) -> int:
        return self.codigo
    def get_dataVenda(self) -> date:
        return self.codigo

    def to_string(self) -> str:
        return f"Codigo: {self.get_codigo()} | Descrição: {self.get_idVenda()}"
    ### DUVIDA ###