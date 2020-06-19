import os
from flask import Flask, render_template, request, redirect, send_from_directory
import mailing

app = Flask(__name__)

@app.route('/')
@app.route('/main.html')
def index():
    return render_template('main.html')

@app.route('/readmore.html')
def read_more():
    return render_template('readmore.html')

@app.route('/submit', methods=['POST'])
def email():
    form_data = request.form

    name    = form_data['name']
    email   = form_data['email']
    message = form_data['message']

    try:
        mailing.send_email(
            name=name,
            email=email,
            message=message
        )
        return render_template('main.html')
    except Exception as e:
        raise e

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
