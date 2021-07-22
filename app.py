from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/cE")
def cE():
    return render_template("compraExitosa.html")

@app.route("/combo")
def combo():
    return render_template("combos.html")

@app.route("/quien")
def quien():
    return render_template("quienesSomos.html")

@app.route("/termino")
def termino():
    return render_template("terminoCondiciones.html")


@app.route('/Bienvenido/<nombre>')
def Bienvenido_nombre(nombre):
    return 'Bienvenido ' + nombre + '!'

if __name__ == "__main__":
    app.run(debug=True)
