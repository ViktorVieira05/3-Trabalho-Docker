from flask import Flask, render_template, request, redirect, url_for
from config import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', produtos=produtos)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)', (nome, preco, quantidade))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
