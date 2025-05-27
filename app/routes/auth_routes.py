from flask import Flask, jsonify, request, redirect, render_template_string, url_for
from app import app


# Página de login com formulário HTML básico
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aqui poderia validar usuário/senha, mas vamos direto redirecionar
        return redirect(url_for('flasgger.apidocs'))
    
    # HTML do formulário
    return render_template_string("""
    <!doctype html>
    <html>
    <head><title>Login</title></head>
    <body>
        <h2>Login</h2>
        <form method="post">
            <label>Usuário:</label><br>
            <input type="text" name="username"><br>
            <label>Senha:</label><br>
            <input type="password" name="password"><br><br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """)




