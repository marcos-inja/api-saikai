from flask import Flask, jsonify
import crawler
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return '<h4>Welcome to SAIKAI API</h4>'

@app.route('/info_novel/<string:name>', methods=['GET'])
def get(name):
    novel_info = crawler.main(name)
    return jsonify(novel_info)

app.run()