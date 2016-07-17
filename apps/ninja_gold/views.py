from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
	request.session['log'] = []
	request.session['goldSum'] = 0
	return render(request, 'index.html')


def process_money(request):
	bldg = request.POST['bldg']
	if bldg == 'farm':
		rand = random.randrange(10,20)
		request.session['log'].append('Earned {} golds from the {}'.format(rand, bldg))
	elif bldg == 'cave':
		rand = random.randrange(5,10)
		request.session['log'].append('Earned {} golds from the {}'.format(rand, bldg))
	elif bldg == 'house':
		rand = random.randrange(2,5)
		request.session['log'].append('Earned {} golds from the {}'.format(rand, bldg))
	elif bldg == 'casino':
		rand = random.randrange(-50,50)
		if rand >= 0:
			request.session['log'].append('Entered a casino and earned {} golds'.format(rand))
		else:
			request.session['log'].append('Entered a casino and lost {} golds...Ouch'.format(rand))
	request.session['gold'] = rand
	return redirect('/sumup')

def calculation(request):
	request.session['goldSum'] += request.session['gold']
	print request.session['log']
	return render(request, 'index.html')