# IMPORTING 
from flask import Flask , render_template

# INTERACTION 
app = Flask(__name__)


# MAPPING 
@app.route('/')

# INPUTS
def home():
    return render_template("index.html")

# MAIN
if __name__ == '__main__':
    app.run(debug=True)