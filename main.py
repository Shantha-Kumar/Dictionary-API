from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def meaning(word):
    result = { "Word": word.title(), "Definition": word.upper() }
    return result


if __name__ == "__main__":
    app.run(debug=True)
