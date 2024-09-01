from flask import Flask, render_template, request, redirect, url_for, session


class Vagas:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_vaga(self):
        conn = self.mysql.connect()
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
        

    def input_vaga(self):
        numerovaga = request.form['numerovaga']
        situacaovaga = request.form['situacaovaga']
        
        if numerovaga and situacaovaga:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('insert into Vaga (NumeroVaga, Situacao) VALUES (%s, %s)',
                        (numerovaga, situacaovaga))
            conn.commit()
        return render_template('cadastrovaga.html')
    

    def get_to_update_vaga(self, pk):    
        conn1 = self.mysql.connect()
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
        

    def update_vaga(self, pk):
        numerovaga = request.form['numeroVaga']
        situacaovaga = request.form['situacaoVaga']

        if numerovaga and situacaovaga:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('UPDATE Vaga SET NumeroVaga=%s, Situacao=%s WHERE idVaga=%s',
                        (numerovaga, situacaovaga, str(pk)))
            conn.commit()
        return render_template('alteravaga.html', pk = pk)