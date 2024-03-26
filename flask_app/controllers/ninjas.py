from flask_app import app
from flask import render_template  , redirect , request , session , flash
from flask_app.models import ninja , dojo




@app.route('/ninjas')
def home():
    print('______________________________________________________________')
    print((dojo.Dojo.dojodata())[0].name)
    return render_template ('ninja.html' , dojos = dojo.Dojo.dojodata())
    

@app.route('/ninja/dojo' , methods = ['POST'])
def created_ninja():
    data = {
        'dojo_iddojos' : request.form['dojo_iddojos'] , 
        'first_name':request.form['first_name'] ,
        'last_name':request.form['last_name'] , 
        'age':request.form['age']
    }
    ninja.Ninja.save(data)
    return redirect('/')



@app.route('/dojoss/<int:dojo_id>')
def show_dojo_with_ninjas(dojo_id):
    print('heloooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
    dojo_and_ninjas = ninja.Ninja.getninjasanddojos(dojo_id)
    print(dojo_and_ninjas)
    return render_template('dojos.html' , dojowithninjas = dojo_and_ninjas)






















# @app.route ('/ninjas')
# def main():
#     return render_template('dojos.html' , ninjadojo = NinjaDojo.ninjasdojo())


# @app.route('/all/dojos' , methods = ['POST'])
# def created_user():
#     data = {
#         'first_name' :request.form['first_name'] , 'last_name':request.form['last_name'] , 'age':request.form['age'] , 'name':request.form['name']
#     }
#     NinjaDojo.joinedninjadojo(data)
#     return redirect ('/')



# @app.route('/dojosdata')
# def show_ninja_dojos_page(data):
#     NinjaDojo.ninjasdojo()
#     return render_template('dojos.html')



