from orientacao import Atendente, Cliente
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

@app.route('/cadastroatendente')
def atendente():
    return render_template('cadastroatendente.html')

@app.route('/cadastroatendente', methods=['POST', 'GET'])
def cadastroatendente():
    Atendente = Atendente(request.form['CpfAtendente'],
                         request.form['NomeAtendente'],
                         request.form['SobrenomeAtendente'],
                         request.form['RgAtendente'],
                         request.form['EnderecoAtendente'],
                         request.form['SalarioAtendente'],
                         request.form['TelefoneAtendente'])

    if Atendente.CpfAtendente and Atendente.NomeAtendente and Atendente.SobrenomeAtendente and Atendente.RgAtendente and Atendente.EnderecoAtendente and Atendente.SalarioAtendente and Atendente.TelefoneAtendente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (Atendente.CpfAtendente, Atendente.NomeAtendente, Atendente.SobrenomeAtendente, Atendente.RgAtendente, Atendente.EnderecoAtendente, Atendente.SalarioAtendente, Atendente.TelefoneAtendente))
        conn.commit()
    return render_template('index.html')


@app.route('/cadastrocliente')
def cliente():
    return render_template('cadastrocliente.html')

@app.route('/cadastrocliente', methods=['POST', 'GET'])
def cadastrocliente():
    Cliente = Cliente(request.form['CpfCliente'],
                         request.form['NomeCliente'],
                         request.form['SobrenomeCliente'],
                         request.form['RgCliente'],
                         request.form['EnderecoCliente'],
                         request.form['Cpfatendente'],
                         request.form['TelefoneCliente'])
    
    if Cliente.CpfCliente and Cliente.NomeCliente and Cliente.SobrenomeCliente and Cliente.RgCliente and Cliente.EnderecoCliente and Cliente.Cpfatendente and Cliente.TelefoneCliente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Atendente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cpfatendente, TelefoneCliente) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (Cliente.CpfCliente, Cliente.NomeCliente, Cliente.SobrenomeCliente, Cliente.RgCliente, Cliente.EnderecoCliente, Cliente.Cpfatendente, Cliente.TelefoneCliente))
        conn.commit()
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3306))
    app.run(host='127.0.0.1', port=port)
