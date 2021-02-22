from flask import Flask, render_template

app = Flask(__name__)
"""
@app.route('/')
def home():
    return "Hola mundo"

@app.route('/Pagina')
def Pagina():
    return "Pagina"
    """    


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Pagina')
def Pagina():
    return render_template('Pagina.html')

@app.route('/Prueba')
def Prueba():
    return render_template('Prueba.html')  



if __name__ == '__main__':
   app.run(debug=True, port=8000)