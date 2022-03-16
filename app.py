#!/usr/bin/env python
import json
import talon
from talon import quotations
from flask import Flask, request, jsonify

talon.init()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'alive': 'yes', 'app_id': 'talon'})

@app.route('/', methods=['POST'])
def process_message():
    reply = quotations.extract_from(request.data.decode('utf-8'), request.content_type)
    return jsonify({'response': reply})

from waitress import serve
serve(app, host="0.0.0.0", port=3000)
