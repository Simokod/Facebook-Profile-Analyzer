import managerV2
from scan_result import ScanResult
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# @app.route("/output")
# def output():
#	return render_template('scan_result.html', scan_result="Hello World!")

@app.route('/')
def home():
   return render_template('Homepage.html')

@app.route('/scan_specific_user')
def scan_specific_user():
   return render_template('ScanSpecificUser.html')

@app.route('/scan_all_friends')
def scan_all_friends():
   return render_template('ScanAllFriends.html')

@app.route("/scan_specific_user/scan", methods=['POST'])
def scan_specific_user_by_url():
	email = request.json['email']
	password = request.json['password']
	user_url = request.json['user_url']
	mod = 0
	scrape_mod = 0
	scan_result = managerV2.scrape_and_analyze(email, password, mod, scrape_mod)
	print(scan_result.offensiveness_result)
	print(scan_result.potentialFakeNews_result)
	print(scan_result.subjects_result)
	return render_template('scan_result.html',
							offensiveness_result=scan_result.offensiveness_result,
							potentialFakeNews_result=scan_result.potentialFakeNews_result,
							subjects_result=scan_result.subjects_result)

if __name__ == "__main__":
	app.run()