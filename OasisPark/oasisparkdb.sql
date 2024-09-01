create database oasisparkdb
use oasisparkdb

CREATE TABLE Atendente (
  	idAtendente int AUTO_INCREMENT Not NULL,
    CpfAtendente char(11) NOT NULL,
    NomeAtendente varchar(30) NOT NULL,
  	SobrenomeAtendente varchar(50) NOT NULL,
    RgAtendente char(9),
  	EnderecoAtendente varchar(100),
  	SalarioAtendente decimal(10,2) NOT NULL,
  	TelefoneAtendente varchar(11) NOT NULL,
    PRIMARY KEY (idAtendente),
  	UNIQUE (idAtendente),
    UNIQUE (CpfAtendente)
);


CREATE TABLE Cliente (
  	idCliente int AUTO_INCREMENT NOT NULL,
    	CpfCliente char(11) NOT NULL,
    	NomeCliente varchar(30) NOT NULL,
  	SobrenomeCliente varchar(50) NOT NULL,
    	RgCliente char(9),
  	EnderecoCliente varchar(100),
  	idAtendente int NOT NULL,
  	TelefoneCliente varchar(11) NOT NULL,    
	nomePlano varchar(11) NOT NULL,
    	PRIMARY KEY (idCliente),
  	UNIQUE(idCliente),
    	UNIQUE (CpfCliente),
  	FOREIGN KEY (idAtendente) REFERENCES Atendente(idAtendente)
);


CREATE TABLE Manobrista (
  	idManobrista int AUTO_INCREMENT NOT NULL,
    CnhManobrista CHAR(11) NOT NULL,
    NomeManobrista varchar(30) NOT NULL,
  	SobrenomeManobrista varchar(50) NOT NULL,
    RgManobrista CHAR(9),
  	EnderecoManobrista varchar(100),
  	SalarioManobrista decimal(10,2) NOT NULL,
  	TelefoneManobrista VARCHAR(11) NOT NULL,
    PRIMARY KEY (idManobrista),
  	UNIQUE(idManobrista),
    UNIQUE (CnhManobrista)
);

CREATE TABLE Vaga (
  	idVaga int AUTO_INCREMENT NOT NULL,
    NumeroVaga char(2) NOT NULL,    
  	Situacao varchar(15) NOT NULL,
    PRIMARY KEY (idVaga),
  	UNIQUE(idVaga),
    UNIQUE (NumeroVaga)
);

CREATE TABLE Veiculo (
  	idVeiculo int AUTO_INCREMENT NOT NULL,
    	Placa CHAR(7) NOT NULL,
    	Cor varchar(15) NOT NULL,
  	Modelo varchar(20) NOT NULL,
    	idCliente int,
  	idAtendente int NOT NULL,
    	PRIMARY KEY (idVeiculo),
  	UNIQUE(idVeiculo),
    	UNIQUE (Placa),
  	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
  	FOREIGN KEY (idAtendente) REFERENCES Atendente(idAtendente)
);

CREATE TABLE Usuarios (
  	idUser int AUTO_INCREMENT NOT NULL,
	Usuario varchar(20) NOT NULL,    
  	Senha varchar(20) NOT NULL,
	Nome varchar(50) NOT NULL,
    	Email varchar(50) NULL,
	Telefone varchar(20) NULL,
    	Liberacao char(1) NOT NULL,
	PRIMARY KEY (idUser),
  	UNIQUE(idUser),
    UNIQUE (Usuario)
);

INSERT INTO Usuarios (Usuario, Senha, Nome, Email, Telefone, Liberacao) VALUES ('rafa', '123', 'Rafael Cavalcante','rafa@rafa.com',Null,"L")

#select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, TelefoneCliente, CpfAtendente, nomePlano from Cliente inner join Atendente on Cliente.idAtendente = Atendente.idAtendente inner join Plano on Cliente.idPlano = Plano.idPlano where idCliente = 1;

CREATE TABLE Historico (
	idHist int AUTO_INCREMENT NOT NULL,
	idCliente int NOT NULL,
  	idVeiculo int NOT NULL,    
  	idVaga int NOT NULL,
  	DataHora_Entrada datetime,
  	DataHora_Saida datetime,
  	Valor decimal(10,2),
  	idAtendente int NOT NULL,
  	nomePlano varchar(20) NOT NULL,
    	PRIMARY KEY (idHist),
  	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
  	FOREIGN KEY (idVaga) REFERENCES Vaga(idVaga),
  	FOREIGN KEY (idAtendente) REFERENCES Atendente(idAtendente)
);