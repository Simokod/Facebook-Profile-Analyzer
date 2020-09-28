import managerV2
from flask import Flask, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/output")
def output():
	return render_template('scan_result.html', scan_result="Hello World!")

@app.route('/')
def home():
   return render_template('home2.html')

@app.route("/analyze/<email>/<password>/<int:mod>/<int:scrape_mod>", methods=['GET'])
def analyze(email, password, mod, scrape_mod):
	# scan_result = managerV2.scrape_and_analyze(email, password, mod, scrape_mod)
	return render_template('index.html')

if __name__ == "__main__":
	app.run()