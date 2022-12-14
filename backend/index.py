from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
def main_page():
    main_css = url_for('static', filename='/styles/main.css')
    main_script = url_for('static', filename='/scripts/main.js')
    return render_template('index.html', main_css=main_css, main_script=main_script)