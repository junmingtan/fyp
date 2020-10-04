from flask import Flask, jsonify, render_template, request

application = Flask(__name__)

db = []

@application.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    :return: Http 200 response
    """
    return jsonify(success=True, status='Happy!')

@application.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@application.route('/submit', methods=['POST'])
def submit():
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
    return jsonify(db)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(host="0.0.0.0", port=80, threaded=False, debug=True)