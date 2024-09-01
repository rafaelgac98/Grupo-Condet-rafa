from flask import Flask, render_template, request, redirect, url_for, session


class Manobrista:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def get_manobrista(self):
        conn = self.mysql.connect()
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
        
    def input_manobrista(self):
        cnhmanobrista = request.form['cnhmanobrista']
        nomemanobrista = request.form['nomemanobrista']
        sobrenomemanobrista = request.form['sobrenomemanobrista']
        rgmanobrista = request.form['rgmanobrista']
        enderecomanobrista = request.form['enderecomanobrista']
        salariomanobrista = request.form['salariomanobrista']
        telefonemanobrista = request.form['telefonemanobrista']
        if cnhmanobrista and nomemanobrista and sobrenomemanobrista and rgmanobrista and enderecomanobrista and salariomanobrista and telefonemanobrista:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('insert into Manobrista (CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (cnhmanobrista, nomemanobrista, sobrenomemanobrista, rgmanobrista, enderecomanobrista, salariomanobrista, telefonemanobrista))
            conn.commit()
        return redirect('/gravarmanobrista')
    
    def get_to_alt_manobrista(self, pk):    
        conn1 = self.mysql.connect()
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
        
    def update_manobrista(self, pk):
        cpfmanobrista = request.form['cnhManobrista']
        nomemanobrista = request.form['nomeManobrista']
        sobrenomecmanobrista = request.form['sobrenomeManobrista']
        rgcmanobrista = request.form['rgManobrista']
        enderecomanobrista = request.form['enderecoManobrista']
        salrariomanobrista = request.form['salarioManobrista']
        telefonemanobrista = request.form['telefManobrista']

        if cpfmanobrista and nomemanobrista and sobrenomecmanobrista and rgcmanobrista and enderecomanobrista and salrariomanobrista and telefonemanobrista:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('UPDATE Manobrista SET CnhManobrista=%s, NomeManobrista=%s, SobrenomeManobrista=%s, RgManobrista=%s, EnderecoManobrista=%s, SalarioManobrista=%s, TelefoneManobrista=%s WHERE idManobrista=%s',
                        (cpfmanobrista, nomemanobrista, sobrenomecmanobrista, rgcmanobrista, enderecomanobrista, salrariomanobrista, telefonemanobrista, str(pk)))
            conn.commit()

        return render_template('alteramanobrista.html', pk = pk)