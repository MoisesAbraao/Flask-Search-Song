#encoding: utf8
from flask import Flask, render_template, request, url_for
from vagalume import lyrics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_song', methods=['GET', 'POST'])
def get_song():
    if request.method == 'POST':
        banda = request.form.get("banda")
        cancao = request.form.get("cancao")

        if banda and cancao:
            resultado = lyrics.find(banda, cancao)
            song = (resultado.song.lyric)
        else:
            song = "Por favor informe os valores dos campos!"
    return render_template("index.html", song=song, cancao=cancao)

if __name__ == "__main__":
    app.run(debug=True)