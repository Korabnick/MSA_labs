from prometheus_client import Counter, generate_latest
from flask import Flask, Response

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.route('/static')
def static_content():
    return "Static content served here."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')
