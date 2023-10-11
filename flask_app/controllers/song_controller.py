from flask import Flask, render_template, redirect
from flask_app import app
from flask_app.models.song import Song


@app.route("/")
def index():
    songs = Song.get_all()
    return render_template("index.html", songs=songs)

@app.route("/songs/add", methods=["GET", "POST"])
def add_song(request):
    if request.method == "GET":
        return render_template("add_song.html")
    data = {
        "title": request.form["title"],
        "artist": request.form["artist"],
        "rating": request.form["rating"],
    }
    Song.save(data)
    return redirect("/")


@app.route("/songs/<int:id>")
def show_song(id):
    song = Song.get_one(id)
    print(song)
    return render_template("single_song.html", song=song)
