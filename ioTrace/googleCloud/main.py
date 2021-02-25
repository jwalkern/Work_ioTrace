import os
from flask import Flask, render_template, request, jsonify
from db import get_device, add_device



db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)


#Dette er vores startside og viser index.html 
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/create', methods = ['POST'])
def create():
    
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
    
        add_device(request.get_json())
        return "Device added."
    json_file = get_device()
    
    return render_template('create.html', json_file=json_file)

@app.route('/read', methods=['GET'])
def read():
    
    json_file = get_device()
    
    return render_template('read.html', json_file=json_file)

@app.route('/update')
def update():
    
    return render_template('update.html')

@app.route('/delete')
def delete():
    
    return render_template('delete.html')


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)