from flask import Flask
app = Flask(__name__)

@app.route('/')
def terminal():
    return 'Hola estamos iniciando con flask desde el contenedor o guacamayas!!!!!'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)