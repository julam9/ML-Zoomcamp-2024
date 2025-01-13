<<<<<<< HEAD
from flask import Flask 

app = Flask('ping')

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG' 

if __name__ == "__main__":
=======
from flask import Flask 

app = Flask('ping')

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG' 

if __name__ == "__main__":
>>>>>>> aedf18eebee25552de09539b402896df33e30238
    app.run(debug=True, host='0.0.0.0', port=9696)