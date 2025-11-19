from flask import Flask, render_template, request, redirect
import sqlite3
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# --------------------- BANCO DE DADOS -------------------------

def criar_banco():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

criar_banco()

# ------------------- ROTAS DO SISTEMA --------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        categoria = request.form["categoria"]
        preco = float(request.form["preco"])
        quantidade = int(request.form["quantidade"])

        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?)",
                       (nome, categoria, preco, quantidade))
        conn.commit()
        conn.close()

        return redirect("/listar")

    return render_template("cadastrar.html")

@app.route("/listar")
def listar():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    return render_template("listar.html", produtos=produtos)

@app.route("/excluir/<int:id>")
def excluir(id):
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/listar")

@app.route("/relatorios")
def relatorios():

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, quantidade FROM produtos")
    dados = cursor.fetchall()
    conn.close()

    # Criar gráfico
    if dados:
        nomes = [x[0] for x in dados]
        quantidades = [x[1] for x in dados]

        plt.figure(figsize=(8,4))
        plt.bar(nomes, quantidades)
        plt.title("Quantidade em Estoque")
        plt.ylabel("Qtd.")
        plt.xticks(rotation=45)

        if not os.path.exists("static"):
            os.makedirs("static")

        plt.tight_layout()
        plt.savefig("static/grafico.png")
        plt.close()

    return render_template("relatorios.html", dados=dados)

# EXECUÇÃO 

if __name__ == "__main__":
    app.run(debug=True)
