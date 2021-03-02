import os
from flask import Flask, render_template, request, jsonify, redirect
from db import get_device, add_device
from form import MyForm



db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)


#Dette er vores startside og viser index.html 
@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/create')
def create():       
    return render_template('create.html')

@app.route('/read')
def read():    
    return render_template('read.html')

@app.route('/update')
def update():    
    return render_template('update.html')

@app.route('/delete')
def delete():    
    return render_template('delete.html')


#Below this comment is all the API commands


@app.route('/api/read', methods=['GET'])
def api_read():
    return get_device()

@app.route('/api/test', methods=['POST', 'GET'])
def api_device():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/delete')
    return render_template('test.html', form=form)


@app.route('/api/create', methods=['POST'])
def api_create():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400  

        add_device(request.get_json())
        return 'Device Added'

    return get_device()



if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)