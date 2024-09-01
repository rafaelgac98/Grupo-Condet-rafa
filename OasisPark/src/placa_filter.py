import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox
from datetime import datetime

class Placa_filter:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_filtrarplaca(self):
        placaveiculo = request.form['placaveiculo']
        classe = ''
        msg=''
        test = '''  2;/ '''
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select idCliente, CpfCliente from Cliente')
        cliente = cursor.fetchall()
        cursor.execute('select idAtendente from Atendente')
        atendente = cursor.fetchall()  
        cursor.execute('select idVaga from Vaga where Situacao = "Desocupado"')
        vagas = cursor.fetchall()
        cursor.execute("select v.Placa from historico h inner join Veiculo v on h.idVeiculo = v.idVeiculo where DataHora_Saida is null")
        veiculosIn = cursor.fetchall()
        #print(veiculosIn)
        i = 0

        while i < len(veiculosIn):
            if placaveiculo == veiculosIn[i][0]:
                classe = "alert alert-danger"
                msg = "Veículo já se encontra no estacionamento!"
                return render_template('index.html', classe=classe, msg=msg, test=test)   
            i += 1

        cursor.execute("select idVeiculo,Placa,Modelo,Cor, Veiculo.idCliente, CpfCliente, Veiculo.idAtendente, CpfAtendente,Cliente.nomePlano from Veiculo inner join Cliente on Veiculo.idCliente = Cliente.idCliente inner join Atendente on Veiculo.idAtendente = Atendente.idAtendente where Veiculo.Placa = '" + str(placaveiculo)+"'")
        data = cursor.fetchall()
        conn.commit()
        # Check if user is loggedin

        if len(data) != 0:
            classe = "alert alert-primary"
            msg = "Veículo já cadastrado! Poderá registrar a entrada."
                # User is loggedin show them the home page
            return render_template('index.html', infos=data, classe=classe, msg=msg, vagas=vagas)
        else:
            classe = "alert alert-danger"
            msg = "Veículo não cadastrado! Favor cadastrar."
            return render_template('cadastrarveiculo.html', classe=classe, msg=msg,cliente=cliente, atendente=atendente)
        # if 'loggedin' in session:
            
        # # User is not loggedin redirect to login page
        # else:
        #     return redirect('/login/entrar')