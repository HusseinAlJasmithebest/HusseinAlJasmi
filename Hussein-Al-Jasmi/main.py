from flask import Flask, render_template, url_for
from SQLAlchemy import SQLAlchemy

app=Flask(__name__, template_folder='templates')
print('printing?')
@app.route('/', methods=['GET','POST'])
def index():
  return render_template('index.html')

@app.route('/becometutor.html', methods=['GET','POST'])
def tutor():
  return render_template('becometutor.html')

@app.route('/science.html', methods=['GET','POST'])
def science():
  return render_template('science.html')

@app.route('/programming.html', methods=['GET','POST'])
def programming():
  return render_template('programming.html')

@app.route('/math.html', methods=['GET','POST'])
def math():
  return render_template('math.html')

"""is it necessary to have a seperate function for each page? can we just link the pages using html? if so, change it to be like that
secondly, how do you get rid of .html at the end of each page?
"""

if __name__=='__main__':
  app.run(debug=True)


