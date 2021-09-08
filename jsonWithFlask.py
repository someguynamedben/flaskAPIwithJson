from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def addTwoNumbers():
    jsonData = request.get_json()
    
    firstNum = int(jsonData['input1'])
    secondNum = int(jsonData['input2'])
    output = firstNum + secondNum

    answer = {
        'answer':output,
    }

    return jsonify(answer)

app.run(port=5000)