from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Hacks Edwuard Castañeda 07/09/2024
@app.route('/users',methods=['GET'])
def h1():
    res = {'payload':'success'}
    return res

@app.route('/user',methods=['POST'])
def h2():
    res = {'payload':'success'}
    return res

@app.route('/user',methods=['DELETE'])
def h3():
    res = {'payload':'success'}
    return res

@app.route('/user',methods=['PUT'])
def h4():
    res = {'payload':'success','error':False}
    return res

@app.route('/api/v1/users',methods=['GET'])
def h5():
    lista = []
    res = {'payload': lista}
    return res

@app.route('/api/v1/user',methods=['POST'])
def h6():
    email = request.args.get('email')
    name  = request.args.get('name')
    res = {'payload': {
            'email':email,
            'name':name,
             }
          }
    return res

@app.route('/api/v1/user/add',methods=['POST'])
def h7():
    email = request.form.get('email')
    name  = request.form.get('name')
    id  = request.form.get('id')
    res = {'payload': {
            'email':email,
            'name':name,
            'id':id
             }
          }
    return res

@app.route('/api/v1/user/create',methods=['POST'])
def h8():
    data = request.get_json()
    email = data['email']
    name  = data['name']
    id    = data['id']
    res = {'payload': {
            'email':email,
            'name':name,
            'id':id
             }
          }
    return res


if __name__ == "__main__":
    app.run(debug=True)