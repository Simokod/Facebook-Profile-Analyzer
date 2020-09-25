import managerV2
from flask import Flask, request
app = Flask(__name__)

@app.route("/output")
def output():
	return "Hello World!"

@app.route("/analyze/<email>/<password>/<int:mod>/<int:scrape_mod>", methods=['GET'])
def analyze(email, password, mod, scrape_mod):
	return managerV2.scrape_and_analyze(email, password, mod, scrape_mod)

if __name__ == "__main__":
	app.run()