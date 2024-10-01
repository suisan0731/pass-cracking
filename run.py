from flask import Flask, request
import os
import re
from dotenv import load_dotenv

app = Flask(__name__)

if os.path.isfile('./.env'):
    load_dotenv()

@app.route('/')
def root():
    try:
        auth_param = request.headers["Authorization"]
    except KeyError:
        return 'invalid header param "Authorization"'

    match = re.match(r'Bearer (.+)', auth_param)
    try:
        parse_auth_param = match.group(1)
    except AttributeError:
        return 'invalid header param "Authorization"'

    if parse_auth_param == os.environ['TOKEN']:
        return 'success!'
    return 'failed'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
