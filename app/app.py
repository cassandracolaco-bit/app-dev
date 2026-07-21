import json
import os
from flask import Flask, jsonify, render_template_string
import platform
import socket
import time

START_TIME = time.time()

app = Flask(__name__)

def load_config(path='config.json'):
    with open(path, 'r') as f:
        return json.load(f)

@app.get('/')
def home():
    cfg = load_config()
    html = (
        '<h1>{{ name }}</h1>'
        '<p>Version: {{ ver }}</p>'
        '<p><a href="/api/name">/api/name</a></p>'
     )
    return render_template_string(
        html,
        name=cfg['app_name'],
        ver=cfg['version']
     )

@app.get('/api/name')
def report():
    return jsonify({
        'author': "Cassandra Colaco"
 })


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080)),
        debug=True
    )