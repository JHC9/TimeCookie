from flask import Flask, render_template, request, make_response, jsonify

import json
#import pandas as pd
app = Flask(__name__)


@app.route("/save_timetable", methods=["GET", "POST"])
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

  if request.method == "POST":
    data = request.form

  for i in range(7, 24):
    row.append(str(i) + ':00')
    l1.append(data.get('mon-' + str(i) + ' '))
    l2.append(data.get('tue-' + str(i)))
    l3.append(data.get('wed-' + str(i)))
    l4.append(data.get('thu-' + str(i)))
    l5.append(data.get('fri-' + str(i)))
    l6.append(data.get('sat-' + str(i)))
    l7.append(data.get('sun-' + str(i)))

  mainlist.append(list(l1))
  mainlist.append(list(l2))
  mainlist.append(list(l3))
  mainlist.append(list(l4))
  mainlist.append(list(l5))
  mainlist.append(list(l6))
  mainlist.append(list(l7))

  for item in mainlist:
    for x in range(len(item)):
      if item[x] == '':
        item[x] = "NA"
  

  rendered_template = render_template('redirect.html')

  # Save the data to a database or a file here
  response = make_response(rendered_template)
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
  

  if cookie_data is None:
    print('No cookie found.')

  else:
    data1 = json.loads(cookie_data)

    return render_template('timetable_pdf.html', data1=data1)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
