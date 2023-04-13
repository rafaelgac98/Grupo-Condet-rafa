CREATE DATABASE oasis;
USE oasis;

SELECT * FROM Atendente;
SELECT * FROM Cliente;
SELECT * FROM Manobrista;
SELECT * FROM Vaga;
SELECT * FROM Veiculo;

CREATE TABLE Atendente (
    CpfAtendente int NOT NULL,
    NomeAtendente varchar(30) NOT NULL,
  	SobrenomeAtendente varchar(50) NOT NULL,
    RgAtendente int,
  	EnderecoAtendente varchar(100),
  	SalarioAtendente int NOT NULL,
  	TelefoneAtendente int NOT NULL,
    PRIMARY KEY (CpfAtendente), 
    UNIQUE (CpfAtendente)
);

CREATE TABLE Cliente (
    CpfCliente int NOT NULL,
    NomeCliente varchar(30) NOT NULL,
  	SobrenomeCliente varchar(50) NOT NULL,
    RgCliente int,
  	EnderecoCliente varchar(100),
  	Cpfatendente int NOT NULL,
  	TelefoneCliente int NOT NULL,
    PRIMARY KEY (CpfCliente), 
    UNIQUE (CpfCliente),
  	FOREIGN KEY (Cpfatendente) REFERENCES Atendente(Cpfatendente)  	
);

CREATE TABLE Manobrista (
    CnhManobrista int NOT NULL,
    NomeManobrista varchar(30) NOT NULL,
  	SobrenomeManobrista varchar(50) NOT NULL,
    RgManobrista int,
  	EnderecoManobrista varchar(100),
  	SalarioManobrista int NOT NULL,
  	TelefoneManobrista int NOT NULL,
    PRIMARY KEY (CnhManobrista), 
    UNIQUE (CnhManobrista)
);

CREATE TABLE Vaga (
    NumeroVaga int NOT NULL,    
  	Situacao varchar(15) NOT NULL,
    PRIMARY KEY (NumeroVaga), 
    UNIQUE (NumeroVaga)
);

CREATE TABLE Veiculo (
    Placa int NOT NULL,
    Cor varchar(15) NOT NULL,
  	Modelo varchar(20) NOT NULL,
    CpfCliente int,
  	NumeroVaga int,
  	DataHora_Entrada datetime,
  	DataHora_Saida datetime,
  	Valor decimal(10,2),
  	CpfAtendente int NOT NULL,
  	Comprovante varchar(100),
    PRIMARY KEY (Placa), 
    UNIQUE (Placa),
  	FOREIGN KEY (CpfCliente) REFERENCES Cliente(CpfCliente),
  	FOREIGN KEY (NumeroVaga) REFERENCES Vaga(NumeroVaga),
  	FOREIGN KEY (CpfAtendente) REFERENCES Atendente(CpfAtendente)
);
