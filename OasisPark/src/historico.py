import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox
from datetime import datetime
from src.login.login import Login

class Historico:
    def __init__(self, mysql):
        self.mysql = mysql
        
    def get_historico(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()  
        
        cursor.execute('select idHist, idCliente, idVeiculo, idVaga, DataHora_Entrada, DataHora_Saida, Valor, idAtendente, nomePlano from Historico where DataHora_Saida is not null')
        data = cursor.fetchall()
        conn.commit()
        # Check if user is loggedin
        if 'loggedin' in session:
            # User is loggedin show them the home page
            return render_template('historico.html',datas=data)#, valor=session['username']
        # User is not loggedin redirect to login page
        else:
            return redirect('/login/entrar')