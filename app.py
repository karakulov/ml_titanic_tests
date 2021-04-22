import pickle

from flask import Flask, render_template, request

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def get_result():
	age = int(request.form['age'])
	pclass = int(request.form['pclass'])
	sex = int(request.form['sex'])
	SibSp = int(request.form['SibSp'])
	parch = int(request.form['parch'])

	pred_result = model.predict([[
		age, 
		SibSp, 
		parch, 
		1 if pclass == 1 else 0, 
		1 if pclass == 2 else 0, 
		1 if pclass == 3 else 0, 
		1 if sex == 0 else 0, # sex_female
		1 if sex == 1 else 0 # sex_male
		]])

	return render_template('result.html',
		result='Вы бы выжили!' if pred_result[0] == 1 else 'Похоже, Вы бы утонули :-(')

@app.route('/')
def index():
	return render_template('index.html',
		title='Выжили бы Вы на Титанике?')
