from flask import Flask, render_template
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/download")
def download():
    return render_template('DownloadPage.html')

@app.route("/contacts")
def contacts():
    return render_template('ContactsPage.html')


@app.route("/about")
def about():
    return render_template('AboutWantersV1.html')

@app.route("/terms")
def terms():
    return render_template('TermsOfService.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
