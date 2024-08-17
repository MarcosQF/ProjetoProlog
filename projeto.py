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

        #resultado = list(prolog.query(consulta)) 
        resultado = {'Nome': 'Whiplash', 'Diretor': 'damien_chazelle', 'Genero': 'drama', 'Ano': 2014}

    return render_template("home_page.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
