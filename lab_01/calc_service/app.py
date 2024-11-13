from flask import Flask, Response, request, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.route('/rpc', methods=['POST'])
def calc_rpc():
    data = request.json
    method = data.get("method")
    args = data.get("data", {}).get("args", [])
    
    if method == "calc.summ":
        result = sum(args)
    elif method == "calc.sub":
        result = args[0] - sum(args[1:])
    elif method == "calc.mult":
        result = 1
        for num in args:
            result *= num
    elif method == "calc.div" and args[1] != 0:
        result = args[0] / args[1] if len(args) >= 2 else "Error"
    else:
        return jsonify({"error": "Method not found"}), 404

    return jsonify({"result": result})

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
