import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox
from datetime import datetime

class Ticket:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def get_ticket(self, pk):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select idHist,Placa,Modelo,Cor, CpfCliente,idVaga, DataHora_Entrada, NomeCliente, SobrenomeCliente  from Historico inner join Cliente on Historico.idCliente  = Cliente.idCliente inner join Veiculo on Historico.idVeiculo = Veiculo.idVeiculo where DataHora_Saida is null and idHist = %s', (pk))
        data = cursor.fetchall()
        conn.commit()
        
        # Check if user is loggedin
        if 'loggedin' in session:
        # User is loggedin show them the home page
            return render_template('ticket.html', datas=data, pk = pk)
        # User is not loggedin redirect to login page
        else:
            return redirect('/login/entrar')