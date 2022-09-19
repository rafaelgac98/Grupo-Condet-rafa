import pymysql

#abrir conexao
conexao = pymysql.connect(host="localhost", port=3306,database="oasis",user="root",
                          password="root",autocommit=True)

#criar um cursor
cursor = conexao.cursor()

#insert
try:
    cursor.execute("INSERT INTO Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) values ('12345678901', 'Danilo', 'Balieiro', '123456789', 'Rua Qualquer, 127', '1500', '1155555555')")
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
