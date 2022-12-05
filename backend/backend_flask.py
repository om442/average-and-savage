from flask import Flask, request

app = Flask(__name__)


@app.route('/recomendation', methods=['GET'])
def recomendation():
    print(request)
    args = request.args
    name = request.args['name']
    email = request.args['id']
    print(name,email)
    
    return args


if __name__ == '__main__':
    app.run()