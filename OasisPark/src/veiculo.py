from flask import Flask, render_template, request, redirect, url_for, session


class Veiculo:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def get_veiculo(self):
        conn = self.mysql.connect()
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
        

    def selectparaforcliente(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select idCliente from Cliente')
        data = cursor.fetchall()
        conn.commit()
        return render_template('index.html',cliente=data)
    
    def gravarveiculo(self):
        placaveiculo = request.form['placaveiculo']
        corveiculo = request.form['corveiculo']
        modeloveiculo = request.form['modeloveiculo']
        cpfcliente = request.form['cpfcliente']
        cpfatendente = request.form['cpfatendente']
        if placaveiculo and corveiculo and modeloveiculo and cpfcliente and cpfatendente:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('insert into Veiculo (Placa, Cor, Modelo, idCliente, idAtendente) VALUES (%s, %s, %s, %s, %s)',
                        (placaveiculo, corveiculo, modeloveiculo, cpfcliente, cpfatendente))
            #cursor.execute('UPDATE Vaga SET Situacao="Ocupado" WHERE idVaga=%s', (numerovaga))
            conn.commit()
        
        return redirect('/veiculo')