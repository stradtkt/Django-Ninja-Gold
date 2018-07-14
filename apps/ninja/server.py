# from flask import Flask, render_template, redirect, request, session
# import datetime
# import random
# app = Flask(__name__)
# app.secret_key = 'abcdefghijklmnopqrstuvwxyz'

# @app.route('/')
# def index():
#   if 'gold' in session:
#     session['gold'] = session['gold']
#   else:
#     session['gold'] = 0
#   if 'append' not in session:
#     session['append'] = []

#   session['farm'] = random.randrange(10,20)
#   session['cave'] = random.randrange(5,10)
#   session['house'] = random.randrange(2,5)
#   session['casino'] = random.randrange(-50,50)
#   return render_template('index.html')

# @app.route('/process_gold', methods=['POST'])
# def gold():
#   if request.form['location'] == 'farm':
#     session['gold'] += session['farm']
#     session['append'].insert(0, "Gained " + str(session['farm']) + " from the farm. " + str(datetime.datetime.now()))
#   if request.form['location'] == 'cave':
#     session['gold'] += session['cave']
#     session['append'].insert(0, "Gained " + str(session['cave']) + " from the cave. " + str(datetime.datetime.now()))
#   if request.form['location'] == 'house':
#     session['gold'] += session['house']
#     session['append'].insert(0, "Gained " + str(session['house']) + " from the house " + str(datetime.datetime.now()))
#   if request.form['location'] == 'casino':
#     session['gold'] += session['casino']
#     session['append'].insert(0, str(session['casino']) + " from the casino " + str(datetime.datetime.now()))
#   return redirect('/')

# @app.route('/reset')
# def reset():
#   session.clear()
#   return redirect('/')

# app.run(debug=True)

# def process_farm(request):
#     if 'gold' in request.session:
#         request.session['gold'] = request.session['gold']
#     else:
#         request.session['gold'] = 0
#         if 'append' not in request.session:
#             request.session = []
#     request.session['farm'] = random.randrange(10, 20)
#     if request.POST['location'] == "farm":
#         request.session['gold'] += request.session['farm']
#         session['append'].insert(0, "Gained " + str(request.session['farm']) + " from the farm. " + str(datetime.datetime.now()))
#     return redirect('/')

# def process_cave(request):
#     if 'gold' in request.session:
#         request.session['gold'] = request.session['gold']
#     else:
#         request.session['gold'] = 0
#         if 'append' not in request.session:
#             request.session = []
        
#     request.session['cave'] = random.randrange(5, 10)
#     if request.POST['location'] == "cave":
#         request.session['gold'] += request.session['cave']
#         request.session['append'].insert(0, "Gained " + str(request.session['cave']) + " from the cave. " + str(datetime.datetime.now()))
#     return redirect('/')

# def process_house(request):
#     if 'gold' in request.session:
#         request.session['gold'] = request.session['gold']
#     else:
#         request.session['gold'] = 0
#         if 'append' not in request.session:
#             request.session = []
        
#     request.session['house'] = random.randrange(2, 5)
#     if request.POST['location'] == "house":
#         request.session['gold'] += request.session['house']
#         request.session['append'].insert(0, "Gained " + str(request.session['house']) + " from the house. " + str(datetime.datetime.now()))
#     return redirect('/')

# def process_casino(request):
#     if 'gold' in request.session:
#         request.session['gold'] = request.session['gold']
#     else:
#         request.session['gold'] = 0
#         if 'append' not in request.session:
#             request.session = []
        
#     request.session['casino'] = random.randrange(-50, 50)
#     if request.POST['location'] == "casino":
#         request.session['gold'] += request.session['casino']
#         request.session['append'].insert(0, str(request.session['casino']) + " from the casino. " + str(datetime.datetime.now()))
#     return redirect('/')