from flask import Flask, request
from flask import render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/checkup')
def checkup():
    return render_template('checkup.html', )



@app.route('/imc')
def IMC():
    return render_template('IMC.html', )



@app.route('/agua')
def agua():
    return render_template('agua.html', )



@app.route('/circunferencia')
def circunferencia():
    return render_template('Circunferencia.html', )



@app.route('/agua.resultado')
def beba():
    peso = request.args.get('peso')
    peso = float(peso)
    agua = peso * 0.035
    agua = round(agua,2)
    return render_template('beba.html',agua=agua)


@app.route('/checkup.resultado')
def check():
    peso = request.args.get('peso')
    altura = request.args.get('altura')
    circ = request.args.get('circ')
    sexo = request.args.get('sexo')

        
    peso = float(peso)
    altura = float(altura)
    circ= float(circ)
    sexo = int(sexo)
#IMC
    if altura < 0 or peso < 0:
       classificacao = ('Digite um Peso e Altura maiores que 0')
    else:
        imc = peso / altura ** 2
        imc = round(imc,2)
    if imc > 40:
        classificacao = ('(Obesidade Grave)')
    elif imc > 30:
        classificacao = ('(Obesidade)')
    elif imc >= 25 and imc <= 29.9:
        classificacao = ('(Sobrepeso)')
    elif imc >= 18.5 and imc <= 24.9:
        classificacao = ('(Normal)')
    else:
        classificacao = ('(Abaixo do peso)')
            

#AGUA
    agua = peso * 0.035
    agua = round(agua,2)
#CIRCUNFERENCIA
    if sexo == 1 and circ >= 102 or sexo == 2 and circ >= 88:
       risco = ('Altíssimo')
       programa = ('Redução de Peso')
    elif sexo == 1 and circ >= 94 or sexo == 2 and circ >= 84:
       risco = ('Alto')
       programa = ('Redução de Peso')
    elif sexo == 1 and circ > 90 or sexo == 2 and circ > 80:
       risco = ('Médio ')
       programa = ('Redução de Peso')
    elif sexo == 1 and circ <= 90 or sexo == 2 and circ<= 80:
       risco = ('Normal')
       programa = ("Controle de Peso")
    else:
       programa = ("Digite um sexo válido")
    return render_template('check.html',classificacao = classificacao,imc = imc, agua = agua,risco = risco, programa = programa)

@app.route('/imc.resultado')
def imc():
 
  altura = request.args.get('altura')
  peso = request.args.get('peso')
  peso = float(peso)
  altura = float(altura)
        
#IMC
  if altura < 0 or peso < 0:
    classificacao = ('Digite um Peso e Altura maiores que 0')
  else:
    imc = peso / altura ** 2
    imc = round(imc,2)
    if imc > 40:
        classificacao = ('(Obesidade Grave)')
    elif imc > 30:
        classificacao = ('(Obesidade)')
    elif imc >= 25 and imc <= 29.9:
        classificacao = ('(Sobrepeso)')
    elif imc >= 18.5 and imc <= 24.9:
        classificacao = ('(Normal)')
    else:
        classificacao = ('(Abaixo do peso)')
        
    return render_template('imc.html',imc=imc,classificacao=classificacao)


@app.route('/circunferencia.resultado')
def Circunferencia():
 circ = request.args.get('circ') 
 sexo = request.args.get('sexo')
 circ= float(circ)
 sexo = int(sexo)
 if sexo == 1 and circ >= 102 or sexo == 2 and circ >= 88:
    risco = ('Altíssimo')
    programa = ('Redução de Peso')
 elif sexo == 1 and circ >= 94 or sexo == 2 and circ >= 84:
      risco = ('Alto')
      programa = ('Redução de Peso')
 elif sexo == 1 and circ > 90 or sexo == 2 and circ > 80:
      risco = ('Médio ')
      programa = ('Redução de Peso')
 elif sexo == 1 and circ <= 90 or sexo == 2 and circ<= 80:
      risco = ('Normal')
      programa = ("Controle de Peso")
 else:
      programa = ("Digite um sexo válido")
 return render_template('circunferencia.html',programa=programa,risco=risco)
app.run(host='0.0.0.0', port=81)
