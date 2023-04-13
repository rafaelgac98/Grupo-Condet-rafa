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
    nomePlano varchar(20) NOT NULL,
    PRIMARY KEY (idCliente),
  	UNIQUE(idCliente),
    UNIQUE (CpfCliente),
  	FOREIGN KEY (idAtendente) REFERENCES Atendente(idAtendente)  	
);

insert into Cliente Values (CpfCliente)

alter table Cliente add column nomePlano varchar(20)
#drop table Cliente


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
UPDATE Vaga SET Situacao="Desocupado" WHERE idVaga= 5

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

select idVeiculo,Placa,Modelo,Cor, Veiculo.idCliente, CpfCliente, Veiculo.idAtendente, CpfAtendente  from Veiculo 
inner join Cliente on Veiculo.idCliente = Cliente.idCliente
inner join Atendente on Veiculo.idAtendente = Atendente.idAtendente
		

CREATE TABLE Ticket (
	idTicket int AUTO_INCREMENT NOT NULL,
  	idVeiculo int NOT NULL,
    Placa CHAR(7) NOT NULL,
    Cor varchar(15) NOT NULL,
  	Modelo varchar(20) NOT NULL,
    idCliente int,
  	idVaga int,
  	DataHora_Entrada datetime,
  	Valor decimal(10,2),
  	idAtendente int NOT NULL,
    PRIMARY KEY (idTicket),
	FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
  	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
  	FOREIGN KEY (idVaga) REFERENCES Vaga(idVaga),
  	FOREIGN KEY (idAtendente) REFERENCES Atendente(idAtendente)
);




CREATE TABLE Nota_Fiscal (
	idNotaFiscal int AUTO_INCREMENT NOT NULL,
	idTicket int NOT NULL,
  	idVeiculo int NOT NULL,
    Placa CHAR(7) NOT NULL,
    Cor varchar(15) NOT NULL,
  	Modelo varchar(20) NOT NULL,
    idCliente int,
  	idVaga int,
  	DataHora_Entrada datetime,
  	DataHora_Saida datetime,
  	Valor decimal(10,2),
  	idAtendente int NOT NULL,
    PRIMARY KEY (idNotaFiscal),
	FOREIGN KEY (idTicket) REFERENCES Ticket(idTicket),
	FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo),
  	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
  	FOREIGN KEY (idVaga) REFERENCES Vaga(idVaga),
  	FOREIGN KEY (idAtendente) REFERENCES Atendente(idAtendente)
);

select Placa from Veiculo where Placa 

CREATE TABLE Usuarios (
  	idUser int AUTO_INCREMENT NOT NULL,
	Usuario varchar(20) NOT NULL,    
  	Senha varchar(20) NOT NULL,
	Nome varchar(50) NOT NULL,
    Email varchar(50) NULL,
	Telefone varchar(20) NULL,
	PRIMARY KEY (idUser),
  	UNIQUE(idUser),
    UNIQUE (Usuario)
);

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

select * from historico
select idHist,Placa,Modelo,Cor, CpfCliente,idVaga, DataHora_Entrada  from Historico inner join Cliente on Historico.idCliente  = Cliente.idCliente inner join Veiculo on Historico.idVeiculo = Veiculo.idVeiculo where DataHora_Saida is null
select idVeiculo,Placa,Modelo,Cor, Veiculo.idCliente, CpfCliente, Veiculo.idAtendente, CpfAtendente, Cliente.nomePlano from Veiculo inner join Cliente on Veiculo.idCliente = Cliente.idCliente inner join Atendente on Veiculo.idAtendente = Atendente.idAtendente where Veiculo.Placa = 'CHB0601'


select idVaga from Historico where idVeiculo=1

select * from Vaga

update Vaga
set Situacao = "Desocupado"
where idVaga = 2

select idVaga from Historico where idHist=33
select idHist,Placa,Modelo,Cor, CpfCliente,idVaga, DataHora_Entrada  from Historico inner join Cliente on Historico.idCliente  = Cliente.idCliente inner join Veiculo on Historico.idVeiculo = Veiculo.idVeiculo







drop table Atendente
truncate table Atendente
drop table Cliente 
drop table Manobrista 
drop table Nota_fiscal 
drop table Ticket 
drop table Usuarios 
drop table Vaga 
drop table Veiculo
truncate table Veiculo 
select * from Usuarios where Usuario = 'rafa' and Senha = '123'

insert into Usuarios (Usuario, Senha , Nome) values ('rafa','123', 'RAFAEL')
