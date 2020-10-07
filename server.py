import managerV2
from scan_result import ScanResult
from modes import Scrape_mode, Mode
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
	mod = Mode.Release							# release mode
	scrape_mod = Scrape_mode.Scrape_specific  	# scrape specific profile
	scan_result = managerV2.scrape_and_analyze(email, password, mod, scrape_mod, user_url)[0]

	return render_template('scan_result.html',
							offensiveness_result=scan_result.offensiveness_result,
							potentialFakeNews_result=scan_result.potentialFakeNews_result,
							subjects_result=scan_result.subjects_result)

@app.route("/scan_all_friends/scan", methods=['POST'])
def scan_all_friends_scan():
	print("aaaa")
	email = request.json['email']
	password = request.json['password']
	mod = Mode.Release						# release mode
	scrape_mod = Scrape_mode.Scrape_all  	# scrape all friends
	scan_result = managerV2.scrape_and_analyze(email, password, mod, scrape_mod, "")

	return render_template('scan_result.html',
							offensiveness_result=scan_result.offensiveness_result,
							potentialFakeNews_result=scan_result.potentialFakeNews_result,
							subjects_result=scan_result.subjects_result)

if __name__ == "__main__":
	app.run()