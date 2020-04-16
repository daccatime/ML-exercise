
from flask import Flask, request

app = Flask(__name__)

@app.route('', methods=['POST'])
def say_hello():
    data = request.get_json(force=True)
    name = data['name']
    return "hello {0}".format(name)

if __name__ == '__main__':
    print('run from main')
    app.run(port=10001, debug=True)
