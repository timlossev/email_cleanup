#!/usr/bin/env python

import json
import talon
import re
from talon import quotations
from talon import signature
from talon.signature.bruteforce import extract_signature

from flask import Flask, request, jsonify

talon.init()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'alive': 'yes', 'app_id': 'talon'})

@app.route('/', methods=['POST'])
def process_message():
    question = request.data.decode('utf-8')
    email_sender = request.sender.decode('utf-8')
    question = re.sub(r'\\r', '\r', question)
    question = re.sub(r'\\n', '\n', question)
    question = re.sub(r'\\t', '\t', question)
    last_transaction = quotations.extract_from(question, request.content_type)

    if (sender == ""):
        reply, signature = signature.extract(last_transaction, sender=email_sender)
    else:
        reply, signature = extract_signature(last_transaction)

    if (request.headers['accept'] == 'application/json'):
        return jsonify({'response': reply})
    else:
        return reply

from waitress import serve
serve(app, host="0.0.0.0", port=3000)
