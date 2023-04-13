import os
from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox


root = tkinter.Tk()
root.withdraw()



mysql = MySQL()
app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'HashTestByOasisPark1234567'

#conexão com banco mysql no docker
# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
# app.config['MYSQL_DATABASE_DB'] = 'teste'
# app.config['MYSQL_DATABASE_HOST'] = 'db'

#conexão com banco mysql local
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'oasisparkdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
 
mysql.init_app(app)

############################ ------------- LOGIN AND REGISTER---------- ############################

@app.route('/login',  methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/login/entrar',  methods=['POST', 'GET'])
def entrar():
    msg = ''

    if request.method == 'POST' and 'userLogin' in request.form and 'passwordLogin' in request.form:
        # Create variables for easy access
        userLogin = request.form['userLogin']
        passwordLogin = request.form['passwordLogin']
        conn = mysql.connect()
        cursor = conn.cursor()  
        
        cursor.execute(f"select * from Usuarios where Usuario = '{userLogin}' and Senha = '{passwordLogin}'")
        account = cursor.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            #print(account)
            session['id'] = account[0]
            session['username'] = account[1]
            # Redirect to home page
            return redirect('/')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

    return render_template('login.html', msg=msg)

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/login/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect('/login/entrar')

# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/login/registrar', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'userRegister' in request.form and 'passwordRegister' in request.form and 'email' in request.form and 'nome' in request.form:
        # Create variables for easy access
        userRegister = request.form['userRegister']
        passwordRegister = request.form['passwordRegister']
        nome = request.form['nome']
        email = request.form['email']       
        
        # Check if account exists using MySQL
        conn = mysql.connect()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO Usuarios (Usuario, Senha, Nome, Email, Telefone) VALUES (%s, %s, %s,%s,Null)', (userRegister, passwordRegister,nome, email))
        conn.commit()
        msg = 'You have successfully registered!'
    return redirect('/login')


# def loginUser():
#     userLogin = request.form['userLogin']
#     passwordLogin = request.form['passwordLogin']

#     conn = mysql.connect()
#     cursor = conn.cursor()  
    
#     cursor.execute(f"select Senha from Usuarios where Usuario = '{userLogin}'")
#     senha = cursor.fetchall()
#     conn.commit()
#     print(senha[0][0])
#     if passwordLogin == senha[0][0]:
#         return render_template('/')
#     else:
#         return render_template('/login', messagebox.showinfo("ERRO", "Login não feito"))
    




############################ ------------- HISTORICO ---------- ############################

@app.route('/historico',  methods=['POST', 'GET'])
def historico():
    conn = mysql.connect()
    cursor = conn.cursor()  
    
    cursor.execute('select idHist, idCliente, idVeiculo, idVaga, DataHora_Entrada, DataHora_Saida, Valor, idAtendente, nomePlano from Historico where DataHora_Saida is not null')
    data = cursor.fetchall()
    conn.commit()
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('historico.html',datas=data)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    



############################ ------------- FIM HISTORICO ---------- ############################


@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')


########################### ------------- INICIO ROTAS PÁGINA PRINCIPAL ---------- ############################



########################### ------------- CARREGAMENTO PÁGINAS PRINCIPAIS ---------- ############################
@app.route('/',  methods=['POST', 'GET'])
def main():
    msg = ''
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idVaga from Vaga where Situacao = "Desocupado"')
    vaga = cursor.fetchall()
    
    
    cursor.execute('select idHist,Placa,Modelo,Cor, CpfCliente,idVaga, DataHora_Entrada  from Historico inner join Cliente on Historico.idCliente  = Cliente.idCliente inner join Veiculo on Historico.idVeiculo = Veiculo.idVeiculo where DataHora_Saida is null')
    data = cursor.fetchall()
    conn.commit()
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('index.html',datas=data, vaga=vaga, msg=msg)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
########################### ------------- FILTRAR VEICULOS POR PLACA ---------- ############################    
@app.route('/filtrarplaca',  methods=['POST', 'GET'])
def filtrarplaca():
    placaveiculo = request.form['placaveiculo']
    classe = ''
    msg=''
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idCliente, CpfCliente from Cliente')
    cliente = cursor.fetchall()
    cursor.execute('select idAtendente from Atendente')
    atendente = cursor.fetchall()  
    cursor.execute('select idVaga from Vaga where Situacao = "Desocupado"')
    vagas = cursor.fetchall()    
    
    cursor.execute("select idVeiculo,Placa,Modelo,Cor, Veiculo.idCliente, CpfCliente, Veiculo.idAtendente, CpfAtendente,Cliente.nomePlano from Veiculo inner join Cliente on Veiculo.idCliente = Cliente.idCliente inner join Atendente on Veiculo.idAtendente = Atendente.idAtendente where Veiculo.Placa = '" + str(placaveiculo)+"'")
    data = cursor.fetchall()
    conn.commit()
    # Check if user is loggedin

    if len(data) != 0:
        classe = "alert alert-primary"
        msg = "Veículo já cadastrado! Poderá registrar a entrada."
            # User is loggedin show them the home page
        return render_template('index.html', infos=data, classe=classe, msg=msg, vagas=vagas)
    else:
        classe = "alert alert-danger"
        msg = "Veículo não cadastrado! Favor cadastrar."
        return render_template('cadastrarveiculo.html', classe=classe, msg=msg,cliente=cliente, atendente=atendente)
    # if 'loggedin' in session:
        
    # # User is not loggedin redirect to login page
    # else:
    #     return redirect('/login/entrar')
    
########################### ------------- CADASTRAR ENTRADA DE VEICULO ---------- ############################
@app.route('/registrarentrada', methods=['POST', 'GET'])
def registrarentrada():
    classe = ''
    msg=''
    test = '''  3;/ '''
    idcliente = request.form["cpfcliente"]
    idveiculo = request.form["idveiculo"] 
    numerovaga = request.form["numerovaga"]
    idatendente = request.form["cpfatendente"]
    nomeplano = request.form["plano"]
    if idcliente and idveiculo  and numerovaga and idatendente and nomeplano:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Historico (idCliente, idVeiculo, idVaga, DataHora_Entrada, DataHora_Saida, Valor, idAtendente, nomePlano) VALUES (%s, %s, %s, now(),null, null,%s,%s)',
                       (idcliente, idveiculo,numerovaga, idatendente, nomeplano))
        cursor.execute('UPDATE Vaga SET Situacao="Ocupado" WHERE idVaga=%s', (numerovaga))
        conn.commit()
        classe = "alert alert-success"
        msg = "Entrada registrada com sucesso!"
    
    return render_template('index.html', classe=classe, msg=msg, test=test)


@app.route('/registrarsaida/<int:pk>/', methods=['POST', 'GET'])
def registrarsaida(pk):
    #numerovaga = request.form['numerovaga']
    conn = mysql.connect()
    print(pk)
    cursor = conn.cursor()
    id = cursor.execute('select idVaga from Historico where idHist=%s', (pk))
    print(id)
    cursor.execute('UPDATE Historico SET DataHora_Saida = now() WHERE idHist=%s', (pk))
    cursor.execute('UPDATE Vaga SET Situacao="Desocupado" WHERE idVaga=%s', (id))
    conn.commit()

    return redirect(url_for('main', pk=pk))

########################### ------------- INICIO ROTAS CLIENTE ---------- ############################
#### ---------------- ROTA PAGINA CLIENTE ------------ #######

@app.route('/cliente', methods=['POST', 'GET'])
def selectcliente():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idAtendente, CpfAtendente from Atendente')
    atendente = cursor.fetchall()
    cursor.execute('select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente, nomePlano from Cliente')
    data = cursor.fetchall()
    conn.commit()
    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('cadastrocliente.html',datas=data, atendente=atendente)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


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
    nomePlano = request.form['nomePlano']

    if cpfcliente and nomecliente and sobrenomecliente and rgcliente and enderecocliente and idAtendente and telefonecliente and nomePlano:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Cliente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente, nomePlano) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (cpfcliente, nomecliente, sobrenomecliente, rgcliente, enderecocliente, idAtendente, telefonecliente, nomePlano))
        conn.commit()
    return redirect('/cliente')


####  ---------------  UPDATE CLIENTE ------------- #####


@app.route('/listaparaalteracliente/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteracliente(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente from Cliente where idCliente = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('alteracliente.html', datas=data, pk = pk)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


@app.route('/alterarcliente/<int:pk>/', methods=['POST', 'GET'])
def alterarcliente(pk):
    cpfcliente = request.form['cpfCliente']
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
    cursor.execute('select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cliente.idAtendente, TelefoneCliente, CpfAtendente from Cliente inner join Atendente on Cliente.idAtendente = Atendente.idAtendente where idCliente = ' + str(pk))
    data = cursor.fetchall()
    conn.commit()

    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('listacliente.html', datas=data, pk = pk)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


####  ---------------  DELETAR CLIENTE ------------- #####

# @app.route('/deletecliente/<int:pk>/', methods=['GET'])
# def deletecliente(pk):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('DELETE from Cliente where idCliente = ' + str(pk))
#     data = cursor.fetchall()
#     conn.commit()
#     return render_template('cadastrocliente.html', datas=data, pk = pk)



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

    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('cadastroatendente.html',datas=data)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    




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
    return redirect('/atendente')


#### ------------- LISTAR E ALTERAR ATENDENTE ---------- ####

@app.route('/listaparaalteraatendente/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteraatendente(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente where idAtendente = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('alteraatendente.html', datas=data, pk = pk)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


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

    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('listaatendente.html', datas=data, pk = pk)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


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

    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('cadastromanobrista.html',datas=data)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


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
    return redirect('/gravarmanobrista')


#### ------------- LISTAR E ALTERAR MANOBRISTA ---------- ####
@app.route('/listaparaalteramanobrista/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteramanobrista(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idManobrista, CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista from Manobrista where idManobrista = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('alteramanobrista.html', datas=data, pk = pk)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


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
        conn.commit()

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


    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('cadastrovaga.html', datas=data)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    




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
    return redirect('/gravarvaga')


#### ------------- LISTAR E ALTERAR VAGA ---------- ####
@app.route('/listaparaalteravaga/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteravaga(pk):    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idVaga, NumeroVaga, Situacao from Vaga where idVaga = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    
    # Check if user is loggedin
    if 'loggedin' in session:
    # User is loggedin show them the home page
        return render_template('alteravaga.html', datas=data, pk = pk)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    


@app.route('/alterarvaga/<int:pk>/', methods=['POST', 'GET'])
def alterarvaga(pk):
    numerovaga = request.form['numeroVaga']
    situacaovaga = request.form['situacaoVaga']

    if numerovaga and situacaovaga:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE Vaga SET NumeroVaga=%s, Situacao=%s WHERE idVaga=%s',
                       (numerovaga, situacaovaga, str(pk)))
        conn.commit()
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
@app.route('/veiculo',  methods=['POST', 'GET'])
def veiculo():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idCliente, CpfCliente from Cliente')
    cliente = cursor.fetchall()
    cursor.execute('select idAtendente from Atendente')
    atendente = cursor.fetchall()  
    
    
    cursor.execute('select idVeiculo,Placa,Modelo,Cor, CpfCliente  from Veiculo inner join Cliente on Veiculo.idCliente = Cliente.idCliente')
    data = cursor.fetchall()
    conn.commit()
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('cadastrarveiculo.html',datas=data, cliente=cliente, atendente=atendente)
    # User is not loggedin redirect to login page
    else:
        return redirect('/login/entrar')
    

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
    cpfatendente = request.form['cpfatendente']
    if placaveiculo and corveiculo and modeloveiculo and cpfcliente and cpfatendente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Veiculo (Placa, Cor, Modelo, idCliente, idAtendente) VALUES (%s, %s, %s, %s, %s)',
                       (placaveiculo, corveiculo, modeloveiculo, cpfcliente, cpfatendente))
        #cursor.execute('UPDATE Vaga SET Situacao="Ocupado" WHERE idVaga=%s', (numerovaga))
        conn.commit()
    
    return redirect('/veiculo')





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

###   ---------------  GRAVAR PLANO ------------- #####

@app.route('/gravarplano', methods=['POST', 'GET'])
def gravarplano():
    idPlano = request.form['idPlano']
    nomePlano = request.form['nomePlano']

    if idPlano and nomePlano:
        conn = mysql.connect()
        cursor = conn.cursos()
        cursor.execute('insert into Planos (idPlano, nomePlano) VALUES (%s, %s)',
                        (idPlano, nomePlano))
        conn.commit()
    return redirect('/planos')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port, debug=True)