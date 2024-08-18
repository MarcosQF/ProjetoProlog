from flask import Flask, request, render_template
from pyswip import Prolog

app = Flask(__name__)


prolog = Prolog()
prolog.consult("prolog_db.pl")

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        consulta = request.form['consulta']

        resultado = prolog.query(consulta)

        for x in resultado:
            print(f'resultado: {x}')
        
    return render_template("home_page.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
