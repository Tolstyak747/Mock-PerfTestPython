import argparse
import random

from flask import Flask, jsonify, request, make_response
from flask import abort

parser = argparse.ArgumentParser()
parser.add_argument('-port', dest="port", default=5000)
arg = parser.parse_args()

app = Flask(__name__)

issues = []


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Запрос не существует'}), 404)


@app.route('/')
def hello():
    return "<h1>Так называемая заглушка</h1>"


@app.route('/rest/api/2/issue/', methods=['GET'])
def get():
    if len(issues) == 0:
        abort(404)
    else:
        return jsonify({'issue': random.choice(issues)})


@app.route('/rest/api/2/issue/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    iss = list(filter(lambda i: i['id'] == issue_id, issues))
    if len(iss) == 0:
        abort(404)
    print('Response: ', iss[0])
    return jsonify({'issue': iss[0]})


@app.route('/rest/api/2/issue/', methods=['POST'])
def create_issue():
    if not request.json:
        abort(400)
    id = random.randint(0, 1000)
    issue = {

        'id': id,
        'key': f"TEST-{random.randint(1000, 5000)}",
        'summary': request.json['summary'],
        'priority': random.randint(1, 5),
        'description': request.json['description'],
        "self": f"http://127.0.0.1:{arg.port}/rest/api/2/issue/{id}"
    }

    issues.append(issue)
    print('Response: ', {'id': issue['id'],
                         'key': issue['key'],
                         'self': issue['self']})
    return jsonify({'id': issue['id'],
                    'key': issue['key'],
                    'self': issue['self']}), 201


@app.route('/rest/api/2/issue/', methods=['PUT'])
def update_issue():
    if len(issues) == 0:
        abort(404)
    iss = random.choice(issues)
    if not request.json:
        abort(400)
    issues.remove(iss)
    iss = {
        'id': iss['id'],
        'key': iss['key'],
        'summary': request.json['summary'],
        'priority': request.json['priority'],
        'description': request.json['description'],
        'self': iss['self']
    }
    issues.append(iss)
    return jsonify()


@app.route('/rest/api/2/issue/', methods=['DELETE'])
def delete_issue():
    if len(issues) == 0:
        abort(404)
    iss = random.choice(issues)
    issues.remove(iss)
    return jsonify()


if __name__ == "__main__":
    app.run(debug=True, port=f"{arg.port}")
