from flask_restful import Resource, Api
from flask import Flask, jsonify, request
import json

class Demonstration(Resource):

    def get(self):
        
        message = "Hello World"
        if message:
           return jsonify(code = 200, body={"data": message})
        else:
            return jsonify(code = 404)