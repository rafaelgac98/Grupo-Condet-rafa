import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

class Atendente:
    def _init_(self, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente):
        self.CpfAtendente = CpfAtendente
        self.NomeAtendente = NomeAtendente
        self.SobrenomeAtendente = SobrenomeAtendente
        self.RgAtendente = RgAtendente
        self.EnderecoAtendente = EnderecoAtendente
        self.SalarioAtendente = SalarioAtendente
        self.TelefoneAtendente = TelefoneAtendente

class Cliente:
    def _init_(self, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cpfatendente, TelefoneCliente):
        self.CpfCliente = CpfCliente
        self.NomeCliente = NomeCliente
        self.SobrenomeCliente = SobrenomeCliente
        self.RgCliente = RgCliente
        self.EnderecoCliente = EnderecoCliente
        self.Cpfatendente = Cpfatendente
        self.TelefoneCliente = TelefoneCliente

class Manobrista:
    def _init_(self, CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista):
        self.CnhManobrista = CnhManobrista
        self.NomeManobrista = NomeManobrista
        self.SobrenomeManobrista = SobrenomeManobrista
        self.RgManobrista = RgManobrista
        self.EnderecoManobrista = EnderecoManobrista
        self.SalarioManobrista = SalarioManobrista
        self.TelefoneManobrista = TelefoneManobrista

class Vaga:
    def _init_(self, NumeroVaga, Situacao):
        self.NumeroVaga = NumeroVaga
        self.Situacao = Situacao
        

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'oasis'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/cadastroatendente', methods=['POST','GET'])
def atendente():
    return render_template('cadastroatendente.html')

def cadastroatendente():
  cpf = request.form[Atendente.CpfAtendente]
  nome = request.form[Atendente.NomeAtendente]
  sobrenome = request.form[Atendente.SobrenomeAtendente]
  rg = request.form[Atendente.RgAtendente]
  endereco = request.form[Atendente.EnderecoAtendente]
  salario = request.form[Atendente.SalarioAtendente]
  telefone = request.form[Atendente.TelefoneAtendente]
  if cpf and nome and sobrenome and rg and endereco and salario and telefone:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) VALUES (%s, %s, %s, %s, %s, %s, %s)', (cpf, nome, sobrenome, rg, endereco, salario, telefone))
    conn.commit()
  return render_template('index.html')

@app.route('/cadastrocliente', methods=['POST','GET'])
def cliente():
    return render_template('cadastrocliente.html')

@app.route('/cadastrocliente', methods=['POST','GET'])
def cadastrocliente():
  cpf = request.form[Cliente.CpfCliente]
  nome = request.form[Cliente.NomeCliente]
  sobrenome = request.form[Cliente.SobrenomeCliente]
  rg = request.form[Cliente.RgCliente]
  endereco = request.form[Cliente.EnderecoCliente]
  cpfatendente = request.form[Cliente.Cpfatendente]
  telefone = request.form[Cliente.TelefoneCliente]
  if cpf and nome and sobrenome and rg and endereco and cpfatendente and telefone:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into Cliente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cpfatendente, TelefoneCliente) VALUES (%s, %s, %s, %s, %s, %s, %s)', (cpf, nome, sobrenome, rg, endereco, cpfatendente, telefone))
    conn.commit()
  return render_template('index.html')
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3306))
    app.run(host='127.0.0.1', port=port)
