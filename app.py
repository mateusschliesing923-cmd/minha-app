from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Minha App - Azure</h1>
    <p>Aplicação Python executando no Microsoft Azure.</p>
    <p>1</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
