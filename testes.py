from pyswip import Prolog


prolog = Prolog()
prolog.consult("prolog_db.pl")

consulta_maior = prolog.query("filme(Nome, Diretor, Genero, Ano).")

for x in consulta_maior:
    print(f'resultado: {x}')

if __name__ == "__main__":
   pass 


  
