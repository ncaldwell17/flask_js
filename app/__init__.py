from flask import Flask
from flask import jsonify, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    params = request.args.get('text', None)
    params = str(params).capitalize
    print(params)
    return jsonify(params)
    # return jsonify({"data": params})

if __name__ == '__main__':
    app.run
