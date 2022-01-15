from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/AmbiencePlayer")
def ambiencePlayer():
	return render_template("playerManager.html")

if __name__ == "__main__":
	app.run()