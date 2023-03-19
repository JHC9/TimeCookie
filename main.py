from flask import Flask, render_template, request, make_response, jsonify
from werkzeug.datastructures import ImmutableMultiDict

import json
#import pandas as pd
app = Flask(__name__)



@app.route("/save_timetable", methods=["GET","POST"])
def save_timetable():
  mainlist = []
  l1 = []
  l2 = []
  l3 = []
  l4 = []
  l5 = []
  l6 = []
  l7 = []
  row = []
  column = ['Monday',"Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  if request.method=="POST":
    data = request.form
  print(data)
  
  for i in range(7,24):
    row.append(str(i)+':00')
    l1.append(data.getlist('mon-'+str(i)))
    l2.append(data.getlist('tues-'+str(i)))
    l3.append(data.getlist('wed-'+str(i)))
    l4.append(data.getlist('thurs-'+str(i)))
    l5.append(data.getlist('fri-'+str(i)))
    l6.append(data.getlist('sat-'+str(i)))
    l7.append(data.getlist('sun-'+str(i)))

  mainlist.append(list(l1))
  mainlist.append(list(l2))
  mainlist.append(list(l3))
  mainlist.append(list(l4))
  mainlist.append(list(l5))
  mainlist.append(list(l6))
  mainlist.append(list(l7))

  x = data.get('mon-7 ')
  print(x)
  print(True)
  
  #df = pd.DataFrame(data, columns =column, index=row)

  
    
      
  

  
  
  # replace empty values with NaN
  #df = df.replace('', pd.NA)
  
  # display the resulting table
  #print(df)
  

    
  # Save the data to a database or a file here
  response = make_response(jsonify({'status': 'success'}))
  response.set_cookie('timetable', json.dumps(mainlist))
  return response







# # define a route to render the homepage
@app.route('/')
def index():
  # read the timetable data from the cookie
  timetable_cookie = request.cookies.get('timetable')
  timetable = json.loads(timetable_cookie) if timetable_cookie else None
  return render_template('index.html', timetable=timetable)

@app.route('/read-cookie')
def read_cookie():
    cookie_data = request.cookies.get('timetable')
    print(cookie_data)
    if cookie_data is not None:
        data1 = json.loads(cookie_data)
        
    else:
        print('No cookie found.')
    return render_template('timetable_pdf.html',data1 = data1)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True) 
