from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    try:
        response = {}
        response["status_code"] = 200
        response["message"] = "API deployed on AWS successfully"
    except Exception as e:
        print(e)
        response["error"] = "Something went wrong."
        response["status_code"] = "500"
    return app.response_class(
            response=json.dumps(response), status=response["status_code"],
            mimetype="application/json"
        )

if __name__ == "__main__":
	app.run()