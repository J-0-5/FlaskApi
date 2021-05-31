from flask import Flask, request, jsonify
from flask_cors import CORS

from db_simulation import (commerce_types, commerces, products,)


app = Flask(__name__)
CORS(app)
    
###---commerce_types---###


@app.route('/commerce_types')  # ---index---#
def getCommerceTypes():
    return jsonify({"status": 200, "message": "commerce_types list", "data": commerce_types})


@app.route('/commerce_type/<string:name>')  # ---show---#
def getCommerceType(name):

    commerce_type = [
        commerce_type for commerce_type in commerce_types if commerce_type['name'] == name]

    if (len(commerce_type) == 0):
        return jsonify({"status": 404, "message": "commerce_type not found", "data": None})

    return jsonify({"status": 200, "message": "commerce_type data", "data": commerce_type})


@app.route('/commerce_type', methods=['POST'])  # ---create---#
def addCommecerType():

    commerce_type = [
        commerce_type for commerce_type in commerce_types if commerce_type['name'] == request.json['name']]

    if(len(commerce_type) != 0):
        return jsonify({"status": 409, "message": "commerce_type already exists", "data": commerce_types})

    auto_increment_id = commerce_types[-1]["id"] + 1

    new_commerce_type = {
        "id": auto_increment_id,
        "name": request.json['name']
    }

    commerce_types.append(new_commerce_type)

    return jsonify({"status": 200, "message": "commerce_type added", "data": commerce_types})


@app.route('/commerce_type/<string:name>', methods=['PUT'])  # ---update---#
def updateCommecerType(name):

    commerce_type = [
        commerce_type for commerce_type in commerce_types if commerce_type['name'] == name]

    if(len(commerce_type) == 0):
        return jsonify({"status": 404, "message": "commerce_type not found", "data": commerce_types})

    commerce_type[0]['name'] = request.json['name']

    return jsonify({"status": 200, "message": "commerce_type updated", "data": commerce_type})


@app.route('/commerce_type/<string:name>', methods=['DELETE'])  # ---delete---#
def deleteCommecerType(name):

    commerce_type = [
        commerce_type for commerce_type in commerce_types if commerce_type['name'] == name]

    if(len(commerce_type) == 0):
        return jsonify({"status": 404, "message": "commerce_type not found", "data": commerce_types})

    commerce_types.remove(commerce_type[0])

    return jsonify({"status": 200, "message": "commerce_type deleted", "data": commerce_types})


if (__name__ == '__main__'):
    app.run(debug=True, port=8080)
