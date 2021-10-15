from flask import Flask, render_template,request
from ewr import Tone_and_style, introduction,structure, word_count


app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def index():
	if request.method == "POST":
		text = request.form['message']
		Tone = Tone_and_style(text)
		introductions = introduction(text)
		structures = structure(text)
		word_counts = word_count(text)
		return render_template("index.html",Tone=Tone, introductions=introductions, structures=structures, word_counts=word_counts)


	return render_template("index.html")



if __name__ == "__main__":
	app.run(debug=True)