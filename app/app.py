import os
from flask import Flask, jsonify, render_template, request, make_response, send_from_directory

application = Flask(__name__)

db = []

@application.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    :return: Http 200 response
    """
    return jsonify(success=True, status='Happy!')

@application.route('/favicon.ico')
def favicon():
        return send_from_directory(os.path.join(application.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

@application.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@application.route('/submit', methods=['POST', 'OPTIONS'])
def submit():
    if request.method == "OPTIONS": # CORS preflight
            return _build_cors_prelight_response()
    data = request.json
    question = data["question"]
    db.append(question)
    print(db)
    return jsonify(success=True)

@application.route('/clear', methods=['GET'])
def clear():
    db.clear()
    print(db)
    return jsonify(success=True)

@application.route('/display', methods=['GET'])
def display():
    return render_template("display.html")

@application.route('/questions', methods=['GET'])
def questions():
    return _corsify_actual_response(jsonify(db))

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(json):
    response=make_response(json)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(host="0.0.0.0", port=80, threaded=False, debug=True)
