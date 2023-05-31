from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

# 1. Localhost:5000/: haz que diga "¡Hola Mundo!"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!' # Devuelve la cadena '¡Hola Mundo!' como respuesta

# 2. Localhost:5000/dojo: haz que diga "¡Dojo!"
@app.route('/dojo')
def coding():
    return '!Dojo¡'

# 3. Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:
# localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
# localhost:5000/say/ Michael: haz que diga "¡Hola, Michael!"
# localhost:5000/say/john: haz que diga "¡Hola, John!"
@app.route('/say/<name>')
def patron(name):
    return f'!Hola, {name}!'

# 4. Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:
# localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
# localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
# localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces
@app.route('/repeat/<int:num>/<string:saludo>')
def repeticion(num, saludo):
    salida = ''
    for i in range(0, num):
        salida += f'<p>{saludo}</p>'
    return salida

if __name__=="__main__":  # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)   # Ejecuta la aplicación en modo de depuración
