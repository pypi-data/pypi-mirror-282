import sys
import json
from flask import Flask, Response
from flask import render_template, jsonify
from collections import OrderedDict

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD '] = True

SG = {}

@app.route('/')
def index():
    return render_template('graph.html', name='main')

@app.route('/sg/<name>')
def sg(name):
    if 'main' in SG:
        return Response(json.dumps(SG[name]), mimetype='application/json')
    else:
        return Response(json.dumps(SG), mimetype='application/json')

@app.route('/subgraph/<name>')
def subgraph(name):
    return render_template('graph.html', name=name)

def run(sg, host, port):
    global SG
    with open(sg, 'r') as f:
        SG = json.loads(f.read())
    app.run(debug=False, host=host, port=port)

def run_with_json(sg, host, port):
    global SG
    SG = sg
    app.run(debug=False, host=host, port=port)

if __name__ == '__main__':
    sg = sys.argv[1]
    with open(sg, 'r') as f:
        SG = json.loads(f.read())
    app.run(debug=True)