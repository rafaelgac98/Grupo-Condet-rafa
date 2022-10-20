import os
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)


############################ ------------- HISTORICO ---------- ############################

@app.route('/historico',  methods=['POST', 'GET'])
def historico():
    conn = mysql.connect()
    cursor = conn.cursor()  
    
    cursor.execute('select idVeiculo, Placa, Cor, Modelo, idCliente, idVaga, DataHora_Entrada, DataHora_Saida, Valor, idAtendente, Comprovante from Veiculo where DataHora_Saida is not null')
    data = cursor.fetchall()
    conn.commit()
    return render_template('historico.html',datas=data)



############################ ------------- FIM HISTORICO ---------- ############################


@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')


########################### ------------- INICIO ROTAS CLIENTE ---------- ############################


#### ---------------- ROTA PAGINA CLIENTE ------------ #######

@app.route('/cliente', methods=['POST', 'GET'])
def selectcliente():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente from Cliente')
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastrocliente.html',datas=data)


####  ---------------  GRAVAR CLIENTE ------------- #####

@app.route('/gravarcliente', methods=['POST', 'GET'])
def gravarcliente():
    cpfcliente = request.form['cpfCliente']
    nomecliente = request.form['nomeCliente']
    sobrenomecliente = request.form['sobrenomeCliente']
    rgcliente = request.form['rgCliente']
    enderecocliente = request.form['enderecoCliente']
    idAtendente = request.form['idAtendente']
    telefonecliente = request.form['telefoneCliente']

    if cpfcliente and nomecliente and sobrenomecliente and rgcliente and enderecocliente and idAtendente and telefonecliente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Cliente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (cpfcliente, nomecliente, sobrenomecliente, rgcliente, enderecocliente, idAtendente, telefonecliente))
        conn.commit()
    return render_template('cadastrocliente.html')


####  ---------------  UPDATE CLIENTE ------------- #####


@app.route('/listaparaalteracliente/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteracliente(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente from Cliente where idCliente = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    return render_template('alteracliente.html', datas=data, pk = pk)


@app.route('/alterarcliente/<int:pk>/', methods=['POST', 'GET'])
def alterarcliente(pk):
    cpfcliente = request.form['cpfClinte']
    nomecliente = request.form['nomeCliente']
    sobrenomecliente = request.form['sobrenomeCliente']
    rgcliente = request.form['rgCliente']
    enderecocliente = request.form['enderecoCliente']
    telefonecliente = request.form['telefCliente']

    if cpfcliente and nomecliente and sobrenomecliente and rgcliente and enderecocliente and telefonecliente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE Cliente SET CpfCliente=%s, NomeCliente=%s, SobrenomeCliente=%s, RgCliente=%s, EnderecoCliente=%s, TelefoneCliente=%s WHERE idCliente=%s',
                       (cpfcliente, nomecliente, sobrenomecliente, rgcliente, enderecocliente, telefonecliente, str(pk)))

    return render_template('alteracliente.html', pk = pk)



####  ---------------  LISTAR CLIENTE ------------- #####

@app.route('/listarcliente/<int:pk>/', methods=['GET'])
def listarcliente(pk):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente from Cliente where idCliente = ' + str(pk))
    data = cursor.fetchall()
    conn.commit()
    return render_template('listacliente.html', datas=data, pk = pk)


####  ---------------  DELETAR CLIENTE ------------- #####

@app.route('/deletecliente/<int:pk>/', methods=['GET'])
def deletecliente(pk):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('DELETE from Cliente where idCliente = ' + str(pk))
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastrocliente.html', datas=data, pk = pk)



############################ ------------- FIM ROTAS CLIENTE ---------- ############################




############################ ------------- INICIO ROTAS ATENDENTE ---------- ############################


####  ---------------  ROTA PAGINA ATENDENTE ------------- #####
@app.route('/atendente', methods=['POST', 'GET'])
def selectatendente():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente')
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastroatendente.html',datas=data)




#### ------------- GRAVAR ATENDENTE ---------- ####
@app.route('/gravaratendente', methods=['POST', 'GET'])
def gravaratendente():
    cpfatendente = request.form['cpfAtendente']
    nomeatendente = request.form['nomeAtendente']
    sobrenomeatendente = request.form['sobrenomeAtendente']
    rgatendente = request.form['rgAtendente']
    enderecoatendente = request.form['enderecoAtendente']
    salarioatendente = request.form['salarioAtendente']
    telefoneatendente = request.form['telefoneAtendente']
    if cpfatendente and nomeatendente and sobrenomeatendente and rgatendente and enderecoatendente and salarioatendente and telefoneatendente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) values (%s, %s, %s, %s, %s, %s, %s)',
                       (cpfatendente, nomeatendente, sobrenomeatendente, rgatendente, enderecoatendente, salarioatendente, telefoneatendente))
        conn.commit()
    return render_template('cadastroatendente.html')


#### ------------- LISTAR E ALTERAR ATENDENTE ---------- ####
@app.route('/listaparaalteraatendente/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteraatendente(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente where idAtendente = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    return render_template('alteraatendente.html', datas=data, pk = pk)


@app.route('/alteraratendente/<int:pk>/', methods=['POST', 'GET'])
def alteraratendente(pk):
    cpfAtendente = request.form['cpfAtendente']
    nomeAtendente = request.form['nomeAtendente']
    sobrenomeAtendente = request.form['sobrenomeAtendente']
    rgAtendente = request.form['rgAtendente']
    enderecoAtendente = request.form['enderecoAtendente']
    salarioAtendente = request.form['salarioAtendente']
    telefoneAtendente = request.form['telefoneAtendente']

    if cpfAtendente and nomeAtendente and sobrenomeAtendente and rgAtendente and enderecoAtendente and salarioAtendente and telefoneAtendente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE Atendente SET CpfAtendente=%s, NomeAtendente=%s, SobrenomeAtendente=%s, RgAtendente=%s, EnderecoAtendente=%s, SalarioAtendente=%s, TelefoneAtendente=%s WHERE idAtendente=%s',
                       (cpfAtendente, nomeAtendente, sobrenomeAtendente, rgAtendente, enderecoAtendente, salarioAtendente,telefoneAtendente, str(pk)))
        conn.commit()

    return render_template('alteraatendente.html', pk = pk)



#### ------------- LISTAR ATENDENTE ---------- ####
@app.route('/listaratendente/<int:pk>/', methods=['GET'])
def listaratendente(pk):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente where idAtendente = ' + str(pk))
    data = cursor.fetchall()
    conn.commit()
    return render_template('listaatendente.html', datas=data, pk = pk)



#### ------------- DELETAR ATENDENTE ---------- ####
@app.route('/deletaratendente/<int:pk>/', methods=['GET'])
def deletaratendente(pk):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('DELETE from Atendente where idAtendente = ' + str(pk))
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastroatendente.html', datas=data, pk = pk)



############################ ------------- FIM ROTAS ATENDENTE ---------- ############################



############################ ------------- INICIO ROTAS MANOBRISTA ---------- ############################



#### ------------- ROTA PAGINA MANOBRISTA ---------- ####
@app.route('/manobrista')
def selectmanobrista():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idManobrista, CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista from Manobrista')
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastromanobrista.html',datas=data)


#### ------------- GRAVAR MANOBRISTA ---------- ####
@app.route('/gravarmanobrista', methods=['POST', 'GET'])
def gravarmanobrista():
    cnhmanobrista = request.form['cnhmanobrista']
    nomemanobrista = request.form['nomemanobrista']
    sobrenomemanobrista = request.form['sobrenomemanobrista']
    rgmanobrista = request.form['rgmanobrista']
    enderecomanobrista = request.form['enderecomanobrista']
    salariomanobrista = request.form['salariomanobrista']
    telefonemanobrista = request.form['telefonemanobrista']
    if cnhmanobrista and nomemanobrista and sobrenomemanobrista and rgmanobrista and enderecomanobrista and salariomanobrista and telefonemanobrista:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Manobrista (CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (cnhmanobrista, nomemanobrista, sobrenomemanobrista, rgmanobrista, enderecomanobrista, salariomanobrista, telefonemanobrista))
        conn.commit()
    return render_template('cadastromanobrista.html')


#### ------------- LISTAR E ALTERAR MANOBRISTA ---------- ####
@app.route('/listaparaalteramanobrista/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteramanobrista(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idManobrista, CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista from Manobrista where idManobrista = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    return render_template('alteramanobrista.html', datas=data, pk = pk)


@app.route('/alterarmanobrista/<int:pk>/', methods=['POST', 'GET'])
def alterarmanobrista(pk):
    cpfmanobrista = request.form['cnhManobrista']
    nomemanobrista = request.form['nomeManobrista']
    sobrenomecmanobrista = request.form['sobrenomeManobrista']
    rgcmanobrista = request.form['rgManobrista']
    enderecomanobrista = request.form['enderecoManobrista']
    salrariomanobrista = request.form['salarioManobrista']
    telefonemanobrista = request.form['telefManobrista']

    if cpfmanobrista and nomemanobrista and sobrenomecmanobrista and rgcmanobrista and enderecomanobrista and salrariomanobrista and telefonemanobrista:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE Manobrista SET CnhManobrista=%s, NomeManobrista=%s, SobrenomeManobrista=%s, RgManobrista=%s, EnderecoManobrista=%s, SalarioManobrista=%s, TelefoneManobrista=%s WHERE idManobrista=%s',
                       (cpfmanobrista, nomemanobrista, sobrenomecmanobrista, rgcmanobrista, enderecomanobrista, salrariomanobrista, telefonemanobrista, str(pk)))

    return render_template('alteramanobrista.html', pk = pk)

#### ------------- DELETAR MANOBRISTA ---------- ####

#@app.route('/deletarmanobrista/<int:pk>/', methods=['GET'])
#def deletaratendente(pk):
#      conn = mysql.connect()
#      cursor = conn.cursor()
#      cursor.execute('DELETE from Manobrista where idManobrista = ' + str(pk))
#      data = cursor.fetchall()
#      conn.commit()
#      return render_template('cadastromanobrista.html', datas=data, pk = pk)

############################ ------------- FIM ROTAS MANOBRISTA ---------- ############################




############################ ------------- INICIO ROTAS VAGA ---------- ############################




#### ------------- ROTA PAGINA VAGA ---------- ####
@app.route('/vaga')
def selectvaga():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idVaga, NumeroVaga, Situacao from Vaga')
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastrovaga.html', datas=data)




#### ------------- GRAVAR VAGA ---------- ####
@app.route('/gravarvaga', methods=['POST', 'GET'])
def gravarvaga():
    numerovaga = request.form['numerovaga']
    situacaovaga = request.form['situacaovaga']
    
    if numerovaga and situacaovaga:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Vaga (NumeroVaga, Situacao) VALUES (%s, %s)',
                       (numerovaga, situacaovaga))
        conn.commit()
    return render_template('cadastrovaga.html')


#### ------------- LISTAR E ALTERAR VAGA ---------- ####
@app.route('/listaparaalteravaga/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteravaga(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idVaga, NumeroVaga, Situacao from Vaga where idVaga = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    return render_template('alteravaga.html', datas=data, pk = pk)


@app.route('/alterarvaga/<int:pk>/', methods=['POST', 'GET'])
def alterarvaga(pk):
    numerovaga = request.form['numeroVaga']
    situacaovaga = request.form['situacaoVaga']

    if numerovaga and situacaovaga:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE Vaga SET NumeroVaga=%s, Situacao=%s WHERE idVaga=%s',
                       (numerovaga, situacaovaga, str(pk)))

    return render_template('alteravaga.html', pk = pk)
#### ------------- DELETAR VAGA ---------- ####

#@app.route('/deletarvaga/<int:pk>/', methods=['GET'])
#def deletaratendente(pk):
#    conn = mysql.connect()
#    cursor = conn.cursor()
#    cursor.execute('DELETE from Vaga where idVaga = ' + str(pk))
#    data = cursor.fetchall()
#    conn.commit()
#    return render_template('cadastrovaga.html', datas=data, pk = pk)

############################ ------------- FIM ROTAS VAGA ---------- ############################




############################ ------------- INICIO ROTAS VEICULO ---------- ############################




#### ------------- GRAVAR VEICULO ---------- ####
@app.route('/',  methods=['POST', 'GET'])
def main():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idCliente from Cliente')
    cliente = cursor.fetchall()
    cursor.execute('select idVaga from Vaga where Situacao = "Desocupado"')
    vaga = cursor.fetchall()
    cursor.execute('select idAtendente from Atendente')
    atendente = cursor.fetchall()  
    
    
    cursor.execute('select idVeiculo, Placa, Cor, Modelo, idCliente, idVaga, DataHora_Entrada, DataHora_Saida, Valor, idAtendente, Comprovante from Veiculo where DataHora_Saida is null')
    data = cursor.fetchall()
    conn.commit()
    return render_template('index.html',datas=data, cliente=cliente, vaga=vaga, atendente=atendente)

#@app.route('/selectparaforcliente', methods=['POST', 'GET'])
def selectparaforcliente():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idCliente from Cliente')
    data = cursor.fetchall()
    conn.commit()
    return render_template('index.html',cliente=data)




#### ------------- GRAVAR VEICULO ---------- ####
@app.route('/gravarveiculo', methods=['POST', 'GET'])
def gravarveiculo():
    placaveiculo = request.form['placaveiculo']
    corveiculo = request.form['corveiculo']
    modeloveiculo = request.form['modeloveiculo']
    cpfcliente = request.form['cpfcliente']
    numerovaga = request.form['numerovaga']
    cpfatendente = request.form['cpfatendente']
    if placaveiculo and corveiculo and modeloveiculo and cpfcliente and numerovaga and cpfatendente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Veiculo (Placa, Cor, Modelo, idCliente, idVaga, DataHora_Entrada, DataHora_Saida, Valor, idAtendente, Comprovante) VALUES (%s, %s, %s, %s, %s, now(), null, null, %s, "teste")',
                       (placaveiculo, corveiculo, modeloveiculo, cpfcliente, numerovaga,cpfatendente))
        cursor.execute('UPDATE Vaga SET Situacao="Ocupado" WHERE idVaga=%s', (numerovaga))
        conn.commit()
    
    return render_template('index.html')



@app.route('/registrarsaida/<int:pk>/', methods=['POST', 'GET'])
def registrarsaida(pk):
    #numerovaga = request.form['numerovaga']
    conn = mysql.connect()
    cursor = conn.cursor()
    id = cursor.execute('select idVaga from Veiculo where idVeiculo=%s', (str(pk)))
    cursor.execute('UPDATE Veiculo SET DataHora_Saida = now() WHERE idVeiculo=%s', (str(pk)))
    cursor.execute('UPDATE Vaga SET Situacao="Desocupado" WHERE idVaga=%s', (id))
    conn.commit()

    return render_template('index.html', pk = pk)

#### ------------- DELETAR VEICULO ---------- ####

#@app.route('/deletarveiculo/<int:pk>/', methods=['GET'])
#def deletaratendente(pk):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('DELETE from Veiculo where idVeiculo = ' + str(pk))
#     data = cursor.fetchall()
#     conn.commit()
#     return render_template('cadastroveiculo.html', datas=data, pk = pk)

############################ ------------- FIM ROTAS VEICULO ---------- ############################



#DELETE

#DELETAR ATENDENTE
# @app.route('/deletaratendente/<int:pk>/', methods=['GET'])
# def deletaratendente(pk):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('DELETE from Atendente where idAtendente = ' + str(pk))
#     data = cursor.fetchall()
#     conn.commit()
#     return render_template('cadastroatendente.html', datas=data, pk = pk)

# #DELETAR MANOBRISTA
# @app.route('/deletarmanobrista/<int:pk>/', methods=['GET'])
# def deletaratendente(pk):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('DELETE from Manobrista where idManobrista = ' + str(pk))
#     data = cursor.fetchall()
#     conn.commit()
#     return render_template('cadastromanobrista.html', datas=data, pk = pk)

# #DELETAR CLIENTE
# @app.route('/deletarcliente/<int:pk>/', methods=['GET'])
# def deletaratendente(pk):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('DELETE from Cliente where idCliente = ' + str(pk))
#     data = cursor.fetchall()
#     conn.commit()
#     return render_template('cadastrocliente.html', datas=data, pk = pk)

# #DELETAR VAGA
# @app.route('/deletarvaga/<int:pk>/', methods=['GET'])
# def deletaratendente(pk):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('DELETE from Vaga where idVaga = ' + str(pk))
#     data = cursor.fetchall()
#     conn.commit()
#     return render_template('cadastrovaga.html', datas=data, pk = pk)

# #DELETAR VEICULO
# @app.route('/deletarveiculo/<int:pk>/', methods=['GET'])
# def deletaratendente(pk):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('DELETE from Veiculo where idVeiculo = ' + str(pk))
#     data = cursor.fetchall()
#     conn.commit()
#     return render_template('cadastroveiculo.html', datas=data, pk = pk)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)
