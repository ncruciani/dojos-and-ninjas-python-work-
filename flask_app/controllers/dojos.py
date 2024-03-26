from flask_app import app
from flask import render_template  , redirect , request , session , flash
from flask_app.models.dojo import Dojo

@app.route('/')
def hello():
    return render_template('index.html', dojos = Dojo.dojodata())

@app.route('/ninjas' , methods = ['POST'])
def create_dojo():
    name = request.form['name']
    data = {'name':name}
    Dojo.save(data)
    return redirect('/')


@app.route('/ninja')
def created_dojos(name):
    Dojo.dojodata()
    return render_template ('index.html')

#@app.route('/all/dojos')
#def created():
    #return render_template('dojos.html')


