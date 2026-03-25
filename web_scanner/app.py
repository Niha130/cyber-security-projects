from flask import Flask, request, render_template
from scanner import scan

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        results = scan(url)
        return render_template("result.html", results=results)
    return render_template("index.html")

app.run(debug=True)
