from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')          
def tabla():

    lista_usuarios = [
        {'nombre' : 'Michael', 'apellido' : 'Choi'},
        {'nombre' : 'John', 'apellido' : 'Supsupin'},
        {'nombre' : 'Mark', 'apellido' : 'Guillen'},
        {'nombre' : 'KB', 'apellido' : 'Tonel'}
]

    return render_template('base.html', usuarios=lista_usuarios)


if __name__=="__main__":     
    app.run(debug=True)    
