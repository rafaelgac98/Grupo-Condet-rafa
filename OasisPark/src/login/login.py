import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox
from datetime import datetime

class Login:
    def __init__(self, mysql):
        self.mysql = mysql

    def entrar(self):
        msg = ''

        if request.method == 'POST' and 'userLogin' in request.form and 'passwordLogin' in request.form:
            # Create variables for easy access
            userLogin = request.form['userLogin']
            #global userLogin
            passwordLogin = request.form['passwordLogin']
            conn = self.mysql.connect()
            cursor = conn.cursor()  
            
            cursor.execute(f"select * from Usuarios where Usuario = '{userLogin}' and Senha = '{passwordLogin}'")
            account = cursor.fetchone()
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                #print(account)
                session['id'] = account[0]
                session['username'] = account[1]
                # Redirect to home page
                return redirect('/')            
            else:
                cursor.execute(f"select * from Usuarios where Usuario = '{userLogin}' or Senha = '{passwordLogin}'")
                account2 = cursor.fetchone()
                if account2 != ():
                    msg = 'Incorrect username/password!'
                else:
                    # Account doesnt exist or username/password incorrect
                    msg = ''

        return render_template('login.html', msg=msg)
    
    def logout(self):
        # Remove session data, this will log the user out
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        # Redirect to login page
        return redirect('/login/entrar')
    
    def register(self):
        # Output message if something goes wrong...
        #msg = ''
        # Check if "username", "password" and "email" POST requests exist (user submitted form)
        if request.method == 'POST' and 'userRegister' in request.form and 'passwordRegister' in request.form and 'email' in request.form and 'nome' in request.form:
            # Create variables for easy access
            userRegister = request.form['userRegister']
            passwordRegister = request.form['passwordRegister']
            nome = request.form['nome']
            email = request.form['email']       
            
            # Check if account exists using MySQL
            conn = self.mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute('INSERT INTO Usuarios (Usuario, Senha, Nome, Email, Telefone, Liberacao) VALUES (%s, %s, %s,%s,Null,"N")', (userRegister, passwordRegister,nome, email))
            conn.commit()
            #msg = 'You have successfully registered!'
        return redirect('/login')