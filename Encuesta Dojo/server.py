from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods=['GET', 'POST'])
def formulario():
    print(request.form)
    if request.method == 'POST':
        session['name'] = request.form['nombre']
        session['location'] = request.form['ubicacion']
        session['languaje'] = request.form['idioma']
        session['coment'] = request.form['comentario']
        return redirect('/results')
    return render_template('base.html')

@app.route('/results')
def resultado():
    nombre = session.get('name')
    ubicacion = session.get('location')
    idioma = session.get('languaje')
    comentario = session.get('coment')
    return render_template('resultados.html', nombre=nombre, ubicacion=ubicacion, idioma=idioma, comentario=comentario)

if __name__=="__main__":
    app.run(debug=True)
