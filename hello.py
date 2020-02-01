from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/info')
def info():
    return 'Info'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)