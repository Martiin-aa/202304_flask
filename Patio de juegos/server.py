from flask import Flask, render_template
app = Flask(__name__)  

# Nivel 1: Cuando un usuario visite http://localhost:5000/play, haz que muestre tres cajas azules hermosas
@app.route('/play')         
def juego_uno():
    return render_template('index.html', num=3, color="#9fc5f8")

# Nivel 2: Cuando un usuario visite localhost:5000/play/(x), haz que muestre las hermosos cajas azules x veces
@app.route('/play/<int:num>')
def juego_dos(num):
    return render_template('index.html', num=num, color="#9fc5f8")

#Nivel 3: Cuando un usuario visite localhost:5000/play/(x)/(color), 
# haz que muestre cajas hermosos x veces, pero esta vez las cajas aparecen en (color)
@app.route ('/play/<int:num>/<color>')
def juego_tres(num, color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":       
    app.run(debug=True)    
