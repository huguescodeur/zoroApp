import platform
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/acceuil/")
def acceuil():
    return render_template("acceuil.html")


@app.route("/acceuil/magasin/")
def magasin():
    return render_template("magasin.html")


@app.route("/acceuil/magasin/ajouter/")
def ajouter():
    return render_template("ajouter.html")


@app.route("/acceuil/magasin/modifier/")
def modifier():
    return render_template("modifier.html")


@app.route("/acceuil/magasin/traitement/")
def traitement():
    return render_template("traitement.html")


@app.route("/acceuil/magasin/suppression/")
def suppression():
    return render_template("suppression.html")


@app.route("/acceuil/magasin/supprimer/")
def supprimer():
    return render_template("supprimer.html")


@app.route("/acceuil/magasin/enregistrer/")
def enregistrer():
    return render_template("enregistrer.html")


if __name__ == "__main__":
    # app.run(debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    if platform.system() == "Windows":
        app.run(host='0.0.0.0', port=50000, debug=True)
