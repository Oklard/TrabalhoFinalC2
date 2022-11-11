CREATE SEQUENCE CLIENTE_IDCLIENTE_SEQ_1;

CREATE TABLE Cliente (
                idCliente NUMBER NOT NULL,
                nome VARCHAR2(50) NOT NULL,
                cpf VARCHAR2(11) NOT NULL,
                email VARCHAR2(50) NOT NULL,
                telefone VARCHAR2(15) NOT NULL,
                endereco VARCHAR2(255) NOT NULL,
                CONSTRAINT CLIENTE_PK PRIMARY KEY (idCliente)
);


CREATE TABLE Veiculo (
                idCarro NUMBER NOT NULL,
                modelo VARCHAR2(25) NOT NULL,
                cor VARCHAR2(25) NOT NULL,
                ano DATE NOT NULL,
                chassis VARCHAR2(25) NOT NULL,
                tipoCambio NUMBER NOT NULL,
                fabricante VARCHAR2(25) NOT NULL,
                CONSTRAINT VEICULO_PK PRIMARY KEY (idCarro)
);


CREATE TABLE VendaVeiculo (
                idVenda NUMBER NOT NULL,
                valorVenda NUMBER NOT NULL,
                dataVenda DATE NOT NULL,
                idCliente NUMBER NOT NULL,
                idCarro NUMBER,
                CONSTRAINT VENDAVEICULO_PK PRIMARY KEY (idVenda)
);


ALTER TABLE VendaVeiculo ADD CONSTRAINT CLIENTE_VENDAVEICULO_FK
FOREIGN KEY (idCliente)
REFERENCES Cliente (idCliente)
NOT DEFERRABLE;

ALTER TABLE VendaVeiculo ADD CONSTRAINT VEICULO_VENDAVEICULO_FK
FOREIGN KEY (idCarro)
REFERENCES Veiculo (idCarro)
NOT DEFERRABLE;