from bs4 import BeautifulSoup
import requests
from time import sleep
from flask import Flask, jsonify, json, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def retrieve_all_products():
	for i in range(20):
		sleep(5)
		page = requests.get("https://www.flipkart.com/taparia-tcs-14-metal-cutter/p/itmf3pt8bkmnjece?pid=CUTF3PT8NT5GK8ZR&srno=b_1_5&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_2.dealCard.OMU_WLIAEDLJE3YO_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_2_NA_view-all_2&lid=LSTCUTF3PT8NT5GK8ZRTL3YDF&fm=neo%2Fmerchandising&iid=b793e24f-8929-4cb4-9a02-542b1373e44d.CUTF3PT8NT5GK8ZR.SEARCH&ppt=browse&ppn=browse&ssid=xmb1ofo2136egqgw1560364383776")
		soup = BeautifulSoup(page.content, 'html.parser')
		print(soup.find('div', class_='_1vC4OE _3qQ9m1'))

@app.route("/")
def home():
	return render_template('home.html',topic='Home')


@app.route('/', methods = ['GET', 'POST'])
def new():
	if request.method == 'POST':
		url = request.form['product']
		email = request.form['email']
		price = request.form['price']

		for i in range(5):
			sleep(10)
			page = requests.get(url)
			soup = BeautifulSoup(page.content, 'html.parser')
			product = soup.find('div', class_='_1vC4OE _3qQ9m1')
			amt = product.get_text().strip().strip('₹')
			amt = amt.replace(',', '')
			print(amt)
			if int(amt,10) < int(price,10):
				print("yeet boiz")

	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)