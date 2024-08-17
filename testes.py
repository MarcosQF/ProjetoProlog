from pyswip import Prolog


prolog = Prolog()
prolog.consult("prolog_db.pl")

consulta_maior = list(prolog.query("filme(Nome, Diretor, Genero, Ano)."))


if __name__ == "__main__":
    for x in consulta_maior:
        print(type(x))
        print(x)


  
