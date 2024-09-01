from flask import Flask, render_template, request, redirect, url_for, session


class Cliente:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_cliente(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select idAtendente, CpfAtendente from Atendente')
        atendente = cursor.fetchall()
        cursor.execute('select idCliente, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cliente.idAtendente, TelefoneCliente, nomePlano from Cliente inner join Atendente on Cliente.idAtendente = Atendente.idAtendente')
        data = cursor.fetchall()
        conn.commit()
        # Check if user is loggedin
        if 'loggedin' in session:
        # User is loggedin show them the home page
            return render_template('cadastrocliente.html',datas=data, atendente=atendente)
        # User is not loggedin redirect to login page
        else:
            return redirect('/login/entrar')


    def input_cliente(self):
        cpfcliente = request.form['cpfCliente']
        nomecliente = request.form['nomeCliente']
        sobrenomecliente = request.form['sobrenomeCliente']
        rgcliente = request.form['rgCliente']
        enderecocliente = request.form['enderecoCliente']
        idAtendente = request.form['idAtendente']
        telefonecliente = request.form['telefoneCliente']
        nomePlano = request.form['nomePlano']
        #valor_acr = 0

        if cpfcliente and nomecliente and sobrenomecliente and rgcliente and enderecocliente and idAtendente and telefonecliente and nomePlano:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('insert into Cliente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente, nomePlano) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                        (cpfcliente, nomecliente, sobrenomecliente, rgcliente, enderecocliente, idAtendente, telefonecliente, nomePlano))
            conn.commit()
        return redirect('/cliente')

    def get_to_alt_cliente(self, pk):    
        conn1 = self.mysql.connect()
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
        
    def get_list_cliente(self, pk):
        conn = self.mysql.connect()
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

    def update_cliente(self, pk):
        cpfcliente = request.form['cpfCliente']
        nomecliente = request.form['nomeCliente']
        sobrenomecliente = request.form['sobrenomeCliente']
        rgcliente = request.form['rgCliente']
        enderecocliente = request.form['enderecoCliente']
        telefonecliente = request.form['telefCliente']

        if cpfcliente and nomecliente and sobrenomecliente and rgcliente and enderecocliente and telefonecliente:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('UPDATE Cliente SET CpfCliente=%s, NomeCliente=%s, SobrenomeCliente=%s, RgCliente=%s, EnderecoCliente=%s, TelefoneCliente=%s WHERE idCliente=%s',
                        (cpfcliente, nomecliente, sobrenomecliente, rgcliente, enderecocliente, telefonecliente, str(pk)))

        return render_template('alteracliente.html', pk = pk)
    
    