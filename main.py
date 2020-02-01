import flask
from flask import render_template, redirect, url_for, request
import requests

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def get_node_count():
    nodes = requests.get("https://komodostats.com/api/coin/nodecount.json").json()['count']
    data = requests.get("http://kmd.explorer.dexstats.info/insight-api-komodo/status").json()['info']
    blocks = data['blocks']
    notarized = data['notarized']
    return render_template('admin.html', var1=blocks, var2=notarized, var3=nodes)


if __name__ == '__main__':
    app.run(port=5000)
