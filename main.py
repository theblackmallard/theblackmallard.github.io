import flask
from flask import render_template, redirect, url_for, request
import requests
import threading
import json

app = flask.Flask(__name__)
package = {}
start = True

def refresh_blocks():
    global node, block, notarize, start
    threading.Timer(300.0, refresh_blocks).start()
    package['nodes'] = requests.get("https://komodostats.com/api/coin/nodecount.json").json()['count']
    data = requests.get("http://kmd.explorer.dexstats.info/insight-api-komodo/status").json()['info']
    package['blocks'] = data['blocks']
    package['notarized'] = data['notarized']
    start = False
    with open('data.json', 'w') as f:
        json.dump(package, f)

if start is True:
    refresh_blocks()

@app.route('/', methods=['GET'])
def get_node_count():
    with open('data.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    blocks = obj['blocks']
    notarized = obj['notarized']
    nodes = obj['nodes']
    return render_template('index.html', var1=blocks, var2=notarized, var3=nodes)


if __name__ == '__main__':
    app.run(port=5000)
