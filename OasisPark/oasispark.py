import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'oasis'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/atendente')
def atendente():
    return render_template('cadastroatendente.html')

# @app.route('/cliente')
# def cliente():
#     return render_template('cadastrocliente.html')

@app.route('/gravaratendente', methods=['POST', 'GET'])
def gravaratendente():
    cpf = request.form['cpf']
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    rg = request.form['rg']
    endereco = request.form['endereco']
    salario = request.form['salario']
    telefone = request.form['telefone']
    if cpf and nome and sobrenome and rg and endereco and salario and telefone:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) values (%s, %s, %s, %s, %s, %s, %s)', (cpf, nome, sobrenome, rg, endereco, salario, telefone))
        conn.commit()
    return render_template('index.html')


# @app.route('/cadastrocliente')
# def cliente():
#     return render_template('cadastrocliente.html')

# @app.route('/gravarcliente', methods=['POST', 'GET'])
# def cadastrocliente():
#     Cliente = Cliente(request.form['CpfCliente'],
#                      request.form['NomeCliente'],
#                      request.form['SobrenomeCliente'],
#                      request.form['RgCliente'],
#                      request.form['EnderecoCliente'],
#                      request.form['Cpfatendente'],
#                      request.form['TelefoneCliente'])
    
#     if Cliente.CpfCliente and Cliente.NomeCliente and Cliente.SobrenomeCliente and Cliente.RgCliente and Cliente.EnderecoCliente and Cliente.Cpfatendente and Cliente.TelefoneCliente:
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute('insert into Atendente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cpfatendente, TelefoneCliente) VALUES (%s, %s, %s, %s, %s, %s, %s)',
#                            (Cliente.CpfCliente, Cliente.NomeCliente, Cliente.SobrenomeCliente, Cliente.RgCliente, Cliente.EnderecoCliente, Cliente.Cpfatendente, Cliente.TelefoneCliente))
#         conn.commit()
#     return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3306))
    app.run(host='0.0.0.0', port=port)
