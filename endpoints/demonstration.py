from flask_restful import Resource, Api
from flask import Flask, jsonify, request
import json

class Demonstration(Resource):

    def get(self):
        
        message = "Olá Mundo"
        if message:
           return jsonify(code = 200, body={"data": message})
        else:
            return jsonify(code = 404)

    def post(self):
        request_data = request.get_json()
        print(f'## Request Payload: {request_data}')
        card  =  request_data['user']

        print(card)

        message = "Request recebido !!"
        if message:
            return jsonify(code = 200, body={"data": message})
        else:
            return jsonify(code = 404)