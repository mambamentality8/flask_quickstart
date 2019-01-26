from flask import Flask,flash
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('temp_index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
