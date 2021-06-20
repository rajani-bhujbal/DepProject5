from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['Post','Get'])
def index():
    return" This is my 3rd project"

if __name__ == "__main__":
    app.run(debug=True)