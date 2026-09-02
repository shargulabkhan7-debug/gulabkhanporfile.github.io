from flask import Flask , render_template as render
app = Flask(__name__)

@app.route('/')
def Home():
    return render("index.html")

app.run()