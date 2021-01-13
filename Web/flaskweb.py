from flask import Flask, render_template, escape, request, url_for
import pandas as pd

app = Flask(__name__)

estadisticas = pd.read_csv('../datos.csv')
winrates = pd.read_csv('../chart_winrate.csv')
activos = pd.read_csv('../chart_activos.csv')

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('home.html', title='Home', table=estadisticas, winrates=winrates, activos=activos)

@app.route("/about")
def about():
    return render_template('About.html', title='About')

@app.route("/contact")
def contact():
    return render_template('Contact.html', title='Contact')

ladder_general =  pd.read_csv('../datos/ladderfinal.csv') 
largo = len(ladder_general['Nombres'])

@app.route("/ladder")
def ladder():
    return render_template('ladder.html',  table=ladder_general, len=largo)

@app.route('/chart_activos.csv')
def asd():
	return render_template('activos.html')


if __name__ == '__main__':
	app.run(debug=True)

	