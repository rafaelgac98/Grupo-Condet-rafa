import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox
from datetime import datetime
from src.login.login import Login
from src.historico import Historico
from src.main_page import Main_Page
from src.ticket import Ticket
from src.placa_filter import Placa_filter
from src.registra_entrada_saida import Registra_Entrada_Saida
from src.users import Users
from src.cliente import Cliente
from src.atendente import Atendente
from src.manobrista import Manobrista
from src.vaga import Vagas
from src.veiculo import Veiculo
from src.planos import Planos

root = tkinter.Tk()
root.withdraw()


mysql = MySQL()
app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'HashTestByOasisPark1234567'

#conexão com banco mysql local
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'oasisparkdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3307
 
mysql.init_app(app)

############################ ------------- LOGIN AND REGISTER---------- ############################

@app.route('/login',  methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/login/entrar',  methods=['POST', 'GET'])
def entrar():
    entrar = Login(mysql)
    return entrar.entrar()

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/login/logout')
def logout():
    sair = Login(mysql)
    return sair.logout()
   

# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/login/registrar', methods=['GET', 'POST'])
def register():
    registrar = Login(mysql)
    return registrar.register()

    




############################ ------------- HISTORICO ---------- ############################

@app.route('/historico',  methods=['POST', 'GET'])
def historico():
    get_hist = Historico(mysql)
    return get_hist.get_historico()
    



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
    main_page = Main_Page(mysql)
    return main_page.main_page()
    
##################################### ------------- TICKET ---------- ######################################

@app.route('/ticket/<int:pk>/', methods=['POST', 'GET'])
def ticket(pk):    
    get_ticket = Ticket(mysql)
    return get_ticket.get_ticket(pk)



########################### ------------- FILTRAR VEICULOS POR PLACA ---------- ############################    
@app.route('/filtrarplaca',  methods=['POST', 'GET'])
def filtrarplaca():
    get_filter = Placa_filter(mysql)
    return get_filter.get_filtrarplaca()
    
########################### ------------- CADASTRAR ENTRADA DE VEICULO ---------- ############################

@app.route('/registrarentrada', methods=['POST', 'GET'])
def registrarentrada():
    registra_ve = Registra_Entrada_Saida(mysql)
    return registra_ve.registrarentrada()


@app.route('/registrarsaida/<int:pk>/', methods=['POST', 'GET'])
def registrarsaida(pk):
    registra_saida = Registra_Entrada_Saida(mysql)
    return registra_saida.registrarsaida(pk)

########################### ------------- INICIO ROTAS CLIENTE ---------- ############################


#### ---------------- ROTA PAGINA USERS ------------ #######

@app.route('/stusuario', methods=['POST', 'GET'])
def selectusuario():
    user = Users(mysql)
    return user.get_user()

@app.route('/altiusuario', methods=['POST', 'GET'])
def alterarusuario():
    alt_user = Users(mysql)
    return alt_user.alter_user()    

####  ---------------  GRAVAR CLIENTE ------------- #####

@app.route('/cliente', methods=['POST', 'GET'])
def selectcliente():
    cliente = Cliente(mysql)
    return cliente.get_cliente()

@app.route('/gravarcliente', methods=['POST', 'GET'])
def gravarcliente():
    cliente = Cliente(mysql)
    return cliente.input_cliente()


####  ---------------  UPDATE CLIENTE ------------- #####


@app.route('/listaparaalteracliente/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteracliente(pk):    
    cliente = Cliente(mysql)
    return cliente.get_to_alt_cliente(pk)
    


@app.route('/alterarcliente/<int:pk>/', methods=['POST', 'GET'])
def alterarcliente(pk):
    cliente = Cliente(mysql)
    return cliente.update_cliente(pk)



####  ---------------  LISTAR CLIENTE ------------- #####

@app.route('/listarcliente/<int:pk>/', methods=['GET'])
def listarcliente(pk):
    cliente = Cliente(mysql)
    return cliente.get_list_cliente(pk)



############################ ------------- FIM ROTAS CLIENTE ---------- ############################




############################ ------------- INICIO ROTAS ATENDENTE ---------- ############################


####  ---------------  ROTA PAGINA ATENDENTE ------------- #####
@app.route('/atendente', methods=['POST', 'GET'])
def selectatendente():
    atendente = Atendente(mysql)
    return atendente.get_atendente()
    




#### ------------- GRAVAR ATENDENTE ---------- ####
@app.route('/gravaratendente', methods=['POST', 'GET'])
def gravaratendente():
    atendente = Atendente(mysql)
    return atendente.input_atendente()


#### ------------- LISTAR E ALTERAR ATENDENTE ---------- ####

@app.route('/listaparaalteraatendente/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteraatendente(pk):    
    atendente = Atendente(mysql)
    return atendente.get_to_update_cliente(pk)
    


@app.route('/alteraratendente/<int:pk>/', methods=['POST', 'GET'])
def alteraratendente(pk):
    atendente = Atendente(mysql)
    return atendente.update_cliente(pk)



#### ------------- LISTAR ATENDENTE ---------- ####
@app.route('/listaratendente/<int:pk>/', methods=['GET'])
def listaratendente(pk):
    atendente = Atendente(mysql)
    return atendente.get_to_list_cliente(pk)
    


#### ------------- DELETAR ATENDENTE ---------- ####
@app.route('/deletaratendente/<int:pk>/', methods=['GET'])
def deletaratendente(pk):
    atendente = Atendente(mysql)
    return atendente.delete_atendente(pk)



############################ ------------- FIM ROTAS ATENDENTE ---------- ############################



############################ ------------- INICIO ROTAS MANOBRISTA ---------- ############################



#### ------------- ROTA PAGINA MANOBRISTA ---------- ####
@app.route('/manobrista')
def selectmanobrista():
    manobrista = Manobrista(mysql)
    return manobrista.get_manobrista()
    


#### ------------- GRAVAR MANOBRISTA ---------- ####
@app.route('/gravarmanobrista', methods=['POST', 'GET'])
def gravarmanobrista():
    manobrista = Manobrista(mysql)
    return manobrista.input_manobrista()


#### ------------- LISTAR E ALTERAR MANOBRISTA ---------- ####
@app.route('/listaparaalteramanobrista/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteramanobrista(pk):    
    manobrista = Manobrista(mysql)
    return manobrista.get_to_alt_manobrista(pk)
    


@app.route('/alterarmanobrista/<int:pk>/', methods=['POST', 'GET'])
def alterarmanobrista(pk):
    manobrista = Manobrista(mysql)
    return manobrista.update_manobrista(pk)


############################ ------------- FIM ROTAS MANOBRISTA ---------- ############################




############################ ------------- INICIO ROTAS VAGA ---------- ############################




#### ------------- ROTA PAGINA VAGA ---------- ####
@app.route('/vaga')
def selectvaga():
    vaga = Vagas(mysql)
    return vaga.get_vaga()

#### ------------- GRAVAR VAGA ---------- ####
@app.route('/gravarvaga', methods=['POST', 'GET'])
def gravarvaga():
    vaga = Vagas(mysql)
    return vaga.input_vaga()


#### ------------- LISTAR E ALTERAR VAGA ---------- ####
@app.route('/listaparaalteravaga/<int:pk>/', methods=['POST', 'GET'])
def listaparaalteravaga(pk):    
    vaga = Vagas(mysql)
    return vaga.get_to_update_vaga(pk)
    


@app.route('/alterarvaga/<int:pk>/', methods=['POST', 'GET'])
def alterarvaga(pk):
    vaga = Vagas(mysql)
    return vaga.update_vaga(pk)


############################ ------------- FIM ROTAS VAGA ---------- ############################




############################ ------------- INICIO ROTAS VEICULO ---------- ############################


#### ------------- GRAVAR VEICULO ---------- ####
@app.route('/veiculo',  methods=['POST', 'GET'])
def veiculo():
    veiculo = Veiculo(mysql)
    return veiculo.get_veiculo()
    

#### ------------- GRAVAR VEICULO ---------- ####
@app.route('/gravarveiculo', methods=['POST', 'GET'])
def gravarveiculo():
    veiculo = Veiculo(mysql)
    return veiculo.gravarveiculo()


###   ---------------  GRAVAR PLANO ------------- #####
@app.route('/gravarplano', methods=['POST', 'GET'])
def gravarplano():
    planos = Planos(mysql)
    return planos.gravarplano()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port, debug=True)