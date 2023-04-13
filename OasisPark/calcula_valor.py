from datetime import datetime, timedelta

data1 = input("Digite a primeira data e hora (formato: dd/mm/aaaa hh:mm): ")
data2 = input("Digite a segunda data e hora (formato: dd/mm/aaaa hh:mm): ")

# Converte as strings de data e hora para o formato datetime
dt1 = datetime.strptime(data1, '%d/%m/%Y %H:%M')
dt2 = datetime.strptime(data2, '%d/%m/%Y %H:%M')

# Calcula a diferença entre as datas
diferenca = dt2 - dt1

# Calcula o valor correspondente às horas trabalhadas
horas_trabalhadas = diferenca.seconds / 3600

if horas_trabalhadas >= 1:
  valor_horas = 10 + (horas_trabalhadas - 1) * 3
else:
  valor_horas = 0

print("O valor das horas trabalhadas é R$", valor_horas)
