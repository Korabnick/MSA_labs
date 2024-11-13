from prometheus_client import Counter, generate_latest
from flask import Flask, Response, request, jsonify
import requests

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.route('/rpc', methods=['POST'])
def rpc():
    data = request.json
    method = data.get("method")
    if method.startswith("calc."):
        response = requests.post("http://calc_service:5002/rpc", json=data)
        return jsonify(response.json())
    return jsonify({"error": "Method not found"}), 404

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


