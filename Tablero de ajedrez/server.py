from flask import Flask, render_template
app = Flask(__name__)  

# 1. localhost:5000: debería mostrar un tablero de ajedrez de 8 por 8
@app.route('/')         
def tablero_uno():
    return render_template('base.html', fila=4, columna=4)

# 2. localhost:5000/4: debería mostrar un tablero de ajedrez de 8 por 4
@app.route('/4')         
def tablero_dos():
    return render_template('base.html', fila=2, columna=4)

# 3. localhost:5000/(x)/(y): debería mostrar un tablero de ajedrez de x por y. Por ejemplo,
#  localhost:5000/10/10 debería mostrar un tablero de ajedrez de 10 por 10
@app.route('/<int:x>/<int:y>')         
def tablero_tres(x, y):
    return render_template('base.html', fila=x, columna=y)

# BONUS SENSEI: Haz que otra ruta acepte 4 parámetro (es decir, "/<x>/<y>/<color1>/<color2>")
# y renderiza un tablero de ajedrez con x filas e y columnas, con colores alternos, color1 y color2
@app.route('/<int:x>/<int:y>/<color1>/<color2>')         
def tablero_color(x, y, color1, color2):
    return render_template('base.html', fila=x, columna=y, color1=color1, color2=color2)

if __name__=="__main__": 
    app.run(debug=True)
