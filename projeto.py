from flask import Flask, request, jsonify, render_template
from pyswip import Prolog

app = Flask(__name__)

prolog = Prolog()
prolog.consult("prolog_db.pl")

@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        query = data.get('query', '')
        
        print('nossaaa')
        resultados = str(prolog.query(query))
        print('nossaaa2222')


        return jsonify({'result': resultados})
    
    return render_template("home_page.html")

if __name__ == "__main__":
    app.run(debug=True)

