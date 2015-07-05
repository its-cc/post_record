from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/push_record", methods=['POST'])
def push_record():
    if request.json:
        data = request.get_json()
    return render_template('record.html', data = data)

if __name__ == '__main__':
    port = 8082
    if len(sys.argv) >=2 :
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)

