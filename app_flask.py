from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route("/soma")
def soma():
    valor1 = request.args.get("valor1")
    valor2 = request.args.get("valor2")
    return(f'A soma de {valor1} + {valor2} é {int(valor1) + int(valor2)}')

@app.route("/subtrair")
def subtrair():
    valor1 = request.args.get("valor1")
    valor2 = request.args.get("valor2")
    return(f'A subtração de {valor1} - {valor2} é igual á: {int(valor1)-int(valor2)}')

@app.route("/multiplicar")
def multiplicar():
    valor1 = request.args.get("valor1")
    valor2 = request.args.get("valor2")
    return(f'A Multiplicação de {valor1} X {valor2} é igual á: {int(valor1)*int(valor2)}')

@app.route("/dividir")
def dividir():
    valor1 = request.args.get("valor1")
    valor2 = request.args.get("valor2")
    if int(valor1) == 0:
        return('Por favor, coloque algum numero que não seja igual a 0.')
    elif int(valor2) == 0:
        return('Por favor, coloque algum numero que não seja igual a 0.')
    else:
        return(f'A Divisão de {valor1} / {valor2} é igual á: {int(valor1)/int(valor2):.2f}')

if __name__ == "__main__":
    app.run(debug=True)
