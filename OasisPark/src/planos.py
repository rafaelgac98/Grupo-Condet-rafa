import os
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import tkinter
from tkinter import messagebox
from datetime import datetime

class Planos:
    def __init__(self, mysql):
        self.mysql = mysql

    def gravarplano(self):
        idPlano = request.form['idPlano']
        nomePlano = request.form['nomePlano']

        if idPlano and nomePlano:
            conn = self.mysql.connect()
            cursor = conn.cursos()
            cursor.execute('insert into Planos (idPlano, nomePlano) VALUES (%s, %s)',
                            (idPlano, nomePlano))
            conn.commit()
        return redirect('/planos')