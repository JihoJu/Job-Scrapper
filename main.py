from flask import Flask, render_template, request, redirect, send_file
from get_jobs import get_jobs
from exporter import save_to_file

db = {}
app = Flask("Job-Scrapper")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    word = request.args.get("word")
    if word:
        word = word.lower()
        if word in db:
            jobs = db[word]
        else:
            jobs = get_jobs(word)
            db[word] = list(jobs)
    else:
        return redirect('/')
    return render_template("search.html", searchingBy=word, resultNumber=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs, word)
        return send_file(f"{word}.csv")
    except:
        return redirect("/")


app.run(host="127.0.0.1")
