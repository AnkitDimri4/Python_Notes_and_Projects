# IMPORTING 
from flask import Flask, render_template, request

# INTERACTION
web = Flask(__name__)   

#MAPPING 
@web.route('/')  
@web.route('/register')

# INPUTS
def homepage():
    return render_template('register.html')
# MAPPING 
@web.route("/confirmation", methods = ['POST','GET'])

#INPUTS 
def register():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        ph = request.form.get('phone_number')
        return render_template('confirm.html', name=n, city=c, phone_number=ph)


#MAIN
if __name__ == "__main__":
    web.run(debug=True) 