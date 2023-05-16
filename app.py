from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dados fictícios de usuários
users = [
    {"username": "mbaccin", "password": "senha1"},
    {"username": "mhenrique", "password": "senha2"},
    {"username": "gmendes", "password": "senha3"}
]

# Rota da página principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota da página de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        for user in users:
            if user["username"] == username and user["password"] == password:
                return redirect("/contact")

        return render_template("login.html", error=True)

    return render_template("login.html", error=False)

# Rota da página de formulário de contato
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Lógica para enviar e-mail aqui
        return redirect("/")

    return render_template("contact.html")

# Rota da página com lista de links
@app.route("/links")
def links():
    links = [
        {"url": "https://pt.wikipedia.org/wiki/Clube_de_Regatas_do_Flamengo", "title": "Exemplo 1"},
        {"url": "https://pt.wikipedia.org/wiki/S%C3%A3o_Paulo_Futebol_Clube", "title": "Exemplo 2"},
        {"url": "https://pt.wikipedia.org/wiki/Sport_Club_Corinthians_Paulista", "title": "Exemplo 3"}
    ]
    return render_template("links.html", links=links)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
