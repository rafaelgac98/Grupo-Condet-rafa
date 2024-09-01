from flask import Flask, render_template, request, redirect, url_for, session

class Atendente:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_atendente(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente')
        data = cursor.fetchall()
        conn.commit()

        # Check if user is loggedin
        if 'loggedin' in session:
            cursor.execute('select idUser, Liberacao from Usuarios where  idUser =%s', (session['id']))
            resp = cursor.fetchall()
            #if resp[0] == 1 or resp[1] == 'L':
            #    libe = 'Verdadeiro'
                #return render_template('alteracliente.html', datas=data, pk = pk, resplibe=libe)
        # User is loggedin show them the home page
            return render_template('cadastroatendente.html',datas=data, resplibe=resp)
        # User is not loggedin redirect to login page
        else:
            return redirect('/login/entrar')
    
    def input_atendente(self):
        cpfatendente = request.form['cpfAtendente']
        nomeatendente = request.form['nomeAtendente']
        sobrenomeatendente = request.form['sobrenomeAtendente']
        rgatendente = request.form['rgAtendente']
        enderecoatendente = request.form['enderecoAtendente']
        salarioatendente = request.form['salarioAtendente']
        telefoneatendente = request.form['telefoneAtendente']
        if cpfatendente and nomeatendente and sobrenomeatendente and rgatendente and enderecoatendente and salarioatendente and telefoneatendente:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('insert into Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) values (%s, %s, %s, %s, %s, %s, %s)',
                        (cpfatendente, nomeatendente, sobrenomeatendente, rgatendente, enderecoatendente, salarioatendente, telefoneatendente))
            conn.commit()
        return redirect('/atendente')
    
    def get_to_update_cliente(self, pk):    
        conn1 = self.mysql.connect()
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
        
    def update_cliente(self, pk):
        cpfAtendente = request.form['cpfAtendente']
        nomeAtendente = request.form['nomeAtendente']
        sobrenomeAtendente = request.form['sobrenomeAtendente']
        rgAtendente = request.form['rgAtendente']
        enderecoAtendente = request.form['enderecoAtendente']
        salarioAtendente = request.form['salarioAtendente']
        telefoneAtendente = request.form['telefoneAtendente']

        if cpfAtendente and nomeAtendente and sobrenomeAtendente and rgAtendente and enderecoAtendente and salarioAtendente and telefoneAtendente:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('UPDATE Atendente SET CpfAtendente=%s, NomeAtendente=%s, SobrenomeAtendente=%s, RgAtendente=%s, EnderecoAtendente=%s, SalarioAtendente=%s, TelefoneAtendente=%s WHERE idAtendente=%s',
                        (cpfAtendente, nomeAtendente, sobrenomeAtendente, rgAtendente, enderecoAtendente, salarioAtendente,telefoneAtendente, str(pk)))
            conn.commit()

        return render_template('alteraatendente.html', pk = pk)
    
    def get_to_list_cliente(self, pk):
        conn = self.mysql.connect()
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
        
    def delete_atendente(self, pk):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE from Atendente where idAtendente = ' + str(pk))
        data = cursor.fetchall()
        conn.commit()
        return render_template('cadastroatendente.html', datas=data, pk = pk)