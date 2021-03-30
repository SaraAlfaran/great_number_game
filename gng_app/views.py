from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):

    if ('reset' not in request.session):
        request.session['reset'] = True

    if (request.session['reset'] == True):
        request.session['pick'] = random.randint(1,100)
        print(request.session['pick'])

        request.session['counter'] = 0
        request.session['status'] = ''
        request.session['reset'] = False
    
    if ('players' not in request.session):
        request.session['players'] = []
         
    return render(request, 'index.html')

def submit(request):
    request.session['num'] = int(request.POST['guess'])
    request.session['counter'] += 1

    if (request.session['counter'] == 5 and request.session['num'] != request.session['pick']):
        request.session['status'] = 'game_over'
        return redirect('/')

    if (request.session['num'] < request.session['pick']):
        request.session['status'] = 'Too low!'
    elif (request.session['num'] > request.session['pick']):
        request.session['status'] = 'Too high!'
    else:
        request.session['status'] = 'correct'

    return redirect('/')

def clear(request):
    request.session['reset'] = True
    return redirect('/')

def leaderboard(request):

    temp = request.session['players']

    temp.append({'name': request.POST['name'], 'num': request.session['counter']})

    request.session['players'] = temp

    return render(request, "leader.html")