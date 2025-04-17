from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template_string("""
        <h1>Hello, CloudThat!!!</h1>
        <img src="{{ url_for('static', filename='cloudthat.jpg') }}" alt="Hello Image" width="300">
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
