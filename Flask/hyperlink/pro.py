# IMPORTING 
from flask import Flask , render_template
import os

# INTERACTION 
app = Flask(__name__)
picfolder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = picfolder

# MAPPING 
@app.route('/')

# INPUTS
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'],'EE.jpg')
    pic_1 = os.path.join(app.config['UPLOAD_FOLDER'],'idea.png')
    return render_template("home.html",user_image = pic, user=pic_1)

# MAPPING 
@app.route('/second')

# INPUTS
def second():
    return "Welcome to second page"

# MAIN
if __name__ == '__main__':
    app.run(debug=True)