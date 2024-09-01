from flask import Flask, render_template, request, redirect, url_for, session

class Users:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_user(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        #cursor.execute('select idAtendente, CpfAtendente from Atendente')
        #atendente = cursor.fetchall()
        if session['id'] == 1:
            cursor.execute('select idUser, Usuario, Senha, Nome, email, Liberacao from Usuarios')
            data = cursor.fetchall()
        else:
            if session['id'] > 1:
                cursor.execute('select idUser, Usuario, Senha, Nome, email, Liberacao from Usuarios where  idUser =%s', (session['id']))
                data = cursor.fetchall()
        valtotal = len(data)
        conn.commit()        
        # Check if user is loggedin
        if 'loggedin' in session:
        # User is loggedin show them the home page
            return render_template('stusuario.html',datas=data, idp=session['id'], totall=valtotal)#totall=valtotal,datas=data, atendente=atendente
        # User is not loggedin redirect to login page
        else:
            return redirect('/login/entrar')
    
    def alter_user(self):
        idUsuario = request.form['idUsuario']   
        nomeUsuario = request.form['nomeUsuario']
        senhaUsuario = request.form['senhaUsuario']
        sobrenomeUsuario = request.form['sobrenomeUsuario']
        emailUsuario = request.form['emailUsuario']
        liberacaoSitu = request.form['liberacaoSitu']

        if idUsuario and nomeUsuario and senhaUsuario and sobrenomeUsuario and emailUsuario and liberacaoSitu:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            #cursor.execute(f"select * from Usuarios where Usuario = '{nomeUsuario}' and Senha = '{senhaUsuario}'")
            #account = cursor.fetchone()
            #pk = account[0]
            cursor.execute('UPDATE Usuarios SET Usuario=%s, Senha=%s, Nome=%s, Email=%s, Liberacao=%s WHERE idUser=%s',
                        (nomeUsuario, senhaUsuario, sobrenomeUsuario, emailUsuario, liberacaoSitu, idUsuario))
            conn.commit()

        return redirect('/stusuario')