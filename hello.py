from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!<br><br>Teste apresentacao trabalho final!'
