from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
