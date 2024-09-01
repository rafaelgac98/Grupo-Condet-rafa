import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox
from datetime import datetime

class Registra_Entrada_Saida:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def registrarentrada(self):
        classe = ''
        msg=''
        test = '''  2;/ '''
        idcliente = request.form["cpfcliente"]
        idveiculo = request.form["idveiculo"] 
        numerovaga = request.form["numerovaga"]
        idatendente = request.form["cpfatendente"]
        nomeplano = request.form["plano"]
        if idcliente and idveiculo  and numerovaga and idatendente and nomeplano:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('insert into Historico (idCliente, idVeiculo, idVaga, DataHora_Entrada, DataHora_Saida, Valor, idAtendente, nomePlano) VALUES (%s, %s, %s, now(),null, null,%s,%s)',
                        (idcliente, idveiculo,numerovaga, idatendente, nomeplano))
            cursor.execute('UPDATE Vaga SET Situacao="Ocupado" WHERE idVaga=%s', (numerovaga))
            conn.commit()
            classe = "alert alert-success"
            msg = "Entrada registrada com sucesso!"
        
        return render_template('index.html', classe=classe, msg=msg, test=test)
    
    def registrarsaida(self, pk):
        conn = self.mysql.connect()
        conn2 = self.mysql.connect()
        
        cursor = conn.cursor()
        cursor.execute('select idVaga from Historico where idHist=%s', (pk))
        id = cursor.fetchall()
        
        cursor2 = conn2.cursor()
        cursor2.execute('select DataHora_Entrada, nomePlano from Historico WHERE idHist=%s', (pk))
        teste = cursor2.fetchone()
        
        data1 = str(teste[0])
        data2 =  datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        
        dt1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
        dt2 = datetime.strptime(data2, "%Y-%m-%d %H:%M:%S")

        # Calcula a diferença entre as datas
        diferenca = dt2 - dt1
        print(diferenca.days)
        # Calcula o valor correspondente às horas trabalhadas
        horas_trabalhadas = diferenca.seconds / 3600
        print(horas_trabalhadas)

        if teste[1] == "DIARIA":
            if horas_trabalhadas > 0.15:
                if horas_trabalhadas > 0 and horas_trabalhadas < 1:
                    horas_trabalhadas = 0
                else:
                    horas_trabalhadas = horas_trabalhadas - 1
                    if horas_trabalhadas > 0 and horas_trabalhadas < 1:
                        horas_trabalhadas = 1
                    else:
                        horas_trabalhadas = int(horas_trabalhadas) + 1

                valor_horas = 10 + horas_trabalhadas * 3
            else:
                valor_horas = 0
        else:
            if horas_trabalhadas > 12.00:
                if horas_trabalhadas > 0 and horas_trabalhadas < 1:
                    horas_trabalhadas = 0
                else:
                    horas_trabalhadas = horas_trabalhadas - 1
                    if horas_trabalhadas > 0 and horas_trabalhadas < 1:
                        horas_trabalhadas = 1
                    else:
                        horas_trabalhadas = int(horas_trabalhadas) + 1

                valor_horas = 200 + horas_trabalhadas * 3
            else:
                valor_horas = 200

        cursor.execute('UPDATE Historico SET DataHora_Saida = %s, Valor=%s WHERE idHist=%s', (dt2, valor_horas, pk))
        cursor.execute('UPDATE Vaga SET Situacao="Desocupado" WHERE idVaga=%s', (id))
        conn.commit()

        return redirect(url_for('main', pk=pk))