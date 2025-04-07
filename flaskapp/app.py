from flask import Flask

# Créer une application Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask fonctionne bien !"

if __name__ == '__main__':
    app.run(debug=True)
