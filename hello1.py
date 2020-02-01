from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return 'Info2'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)