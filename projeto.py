from flask import Flask, request, render_template,jsonify
from pyswip import Prolog

app = Flask(__name__)

prolog = Prolog()
prolog.consult("prolog_db.pl")

#testes
print(list(prolog.query("filme('The Dark Knight', Diretor, Genero, Ano)")))

@app.route('/', methods=['GET', 'POST'])
def home_page():
    resultado = None
    if request.method == 'POST':
        consulta = request.form['consulta']
        print(type({consulta}))
        print(consulta)

        resultado = consulta
        #resultado = list(prolog.query(consulta))
       
    return render_template("home_page.html", resultado=resultado)






if __name__ == "__main__":
    app.run(debug=True)
