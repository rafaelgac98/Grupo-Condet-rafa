import pymysql

#abrir conexao
conexao = pymysql.connect(host="localhost", port=3306,database="oasis",user="root",
                          password="root",autocommit=True)

#criar um cursor
cursor = conexao.cursor()

#insert
try:
    cursor.execute("INSERT INTO Atendente (CpfAtendente) values ('12345678901')")
    cursor.execute("INSERT INTO Atendente (NomeAtendente) values ('Danilo')")
    cursor.execute("INSERT INTO Atendente (SobrenomeAtendente) values ('Balieiro')")
    cursor.execute("INSERT INTO Atendente (RgAtendente) values ('123456789')")
    cursor.execute("INSERT INTO Atendente (EnderecoAtendente) values ('Rua Qualquer, 127')")
    cursor.execute("INSERT INTO Atendente (SalarioAtendente) values ('1500')")
    cursor.execute("INSERT INTO Atendente (TelefoneAtendente) values ('55555555')")
except Exception as e:
    print(f"Erro: {e}")
    
#select
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())    
    
#update
# try:
#     cursor.execute("UPDATE cliente SET nome='Bruno' where id=1")
# except Exception as e:
#     print(f"Erro: {e}")
    
#delete
# try:
#     cursor.execute("DELETE FROM cliente where id=1")
# except Exception as e:
#     print(f"Erro: {e}")
    
conexao.close
