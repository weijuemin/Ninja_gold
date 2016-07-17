from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "randomKey"

@app.route('/')
def index():
	session['gold'] = 0
	if 'log' in session:
		session.pop('log')
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	bldg = request.form['bldg']
	goldHad = request.form['record']
	if bldg == 'farm':
		rand = random.randrange(10,20)
		session['gold'] = rand + int(goldHad)
		session['log'] = 'Earned {} golds from the {}'.format(rand, bldg)
	elif bldg == 'cave':
		rand = random.randrange(5,10)
		session['gold'] = rand + int(goldHad)
		session['log'] = 'Earned {} golds from the {}'.format(rand, bldg)
	elif bldg == 'house':
		rand = random.randrange(2,5)
		session['gold'] = rand + int(goldHad)
		session['log'] = 'Earned {} golds from the {}'.format(rand, bldg)
	elif bldg == 'casino':
		rand = random.randrange(-50,50)
		session['gold'] = rand + int(goldHad)
		if session['gold'] >= 0:
			session['log'] = 'Entered a casino and earned {} golds'.format(rand)
		else:
			session['log'] = 'Entered a casino and lost {} golds...Ouch'.format(rand)	
	return render_template('index.html')

app.run(debug=True)