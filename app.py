from bs4 import BeautifulSoup
import requests
from time import sleep
from flask import Flask, jsonify, json, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from file import *

app = Flask(__name__)

def get_price(email,name,url,price):
	f = 1
	for i in range(5):
		if not f:
			break
		sleep(10)
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		product = soup.find('div', class_='_1vC4OE _3qQ9m1')
		amt = product.get_text().strip().strip('₹')
		amt = amt.replace(',', '')
		print(amt)

		if int(amt,10) < int(price,10):
			send_email(email,name,price,amt,url)
			f = 0

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_email(email,name,above,actual,url):
	message_template = read_template('message.txt')
	
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(MY_ADDRESS, PASSWORD)

	msg = MIMEMultipart()
	message = message_template.substitute(PRODUCT_NAME=name,ACTUAL_PRICE=actual,PRODUCT_LINK=url,PRODUCT_PRICE=above)
	print(message)


	msg['From']=MY_ADDRESS
	msg['To']=email
	msg['Subject']="Congrats! The cost of your product has fallen"

	msg.attach(MIMEText(message, 'plain'))

	s.send_message(msg)
	del msg

	s.quit()

@app.route("/")
def home():
	return render_template('home.html',topic='Home')

@app.route("/url", methods = ['GET', 'POST'])
def confirm_url(url):
	return json.dumps(url)

@app.route('/', methods = ['GET', 'POST'])
def new():
	if request.method == 'POST':
		name = request.form['product']
		for i in range(5):
			page = "https://www.flipkart.com/search?q="
			page += name
			page = requests.get(page)
			soup = BeautifulSoup(page.content, 'html.parser')
			url = soup.find_all('a')
			url = soup.find_all('a', class_='_2cLu-l')

			if not url:
				url = soup.find_all('a', class_='_31qSD5')

			url_one = url[0]
			url = url_one.get('href')
			link = "https://www.flipkart.com"
			link += url
			print(link)
			return link
			break
			sleep(10)


	#return render_template('home.html')

@app.route('/price', methods = ['GET', 'POST'])
def price():
	data = request.get_json()
	url = data['link']
	name = data['name']
	email = data['email']
	price = data['price']

	get_price(email,name,url,price)
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)