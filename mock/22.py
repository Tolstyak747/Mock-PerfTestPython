import random
import argparse

from flask import Flask, jsonify, request, make_response
from flask import abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

parser = argparse.ArgumentParser()
parser.add_argument('-port', dest="port", default=5000)
arg = parser.parse_args()

app = Flask(__name__)
auth = HTTPBasicAuth()

user = {'USER_6': generate_password_hash("qwerty")}


@auth.verify_password
def verify_password(username, password):
    if username in user and check_password_hash(user.get(username), password):
        return username
    return None


issues = []


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Запрос не существует'}), 404)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/')
@auth.login_required
def hello():
    return "<h1>Так называемая заглушка</h1>"


@app.route('/rest/api/2/issue/', methods=['GET'])
@auth.login_required
def get():
    return jsonify({'issues': issues})


@app.route('/rest/api/2/issue/<int:issue_id>', methods=['GET'])
@auth.login_required
def get_issue(issue_id):
    iss = list(filter(lambda i: i['id'] == issue_id, issues))
    if len(iss) == 0:
        abort(404)
    print('Response: ', iss[0])
    return jsonify({'issue': iss[0]})


@app.route('/rest/api/2/issue/', methods=['POST'])
@auth.login_required
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


@app.route('/rest/api/2/issue/<int:issue_id>', methods=['PUT'])
@auth.login_required
def update_issue(issue_id):
    iss = list(filter(lambda i: i['id'] == issue_id, issues))
    if len(iss) == 0:
        abort(404)
    if not request.json:
        abort(400)
    issues.remove(iss[0])
    iss[0] = {
        'id': iss[0]['id'],
        'key': iss[0]['key'],
        'summary': request.json['summary'],
        'priority': request.json['priority'],
        'description': request.json['description'],
        'self': iss[0]['self']
    }
    issues.append(iss[0])
    return jsonify()


@app.route('/rest/api/2/issue/<int:issue_id>', methods=['DELETE'])
@auth.login_required
def delete_issue(issue_id):
    iss = list(filter(lambda i: i['id'] == issue_id, issues))
    if len(iss) == 0:
        abort(404)
    issues.remove(iss[0])
    return jsonify()


if __name__ == "__main__":
    app.run(debug=True, port=f"{arg.port}")
