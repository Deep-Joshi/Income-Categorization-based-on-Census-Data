from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__,static_url_path='/static')

@app.route('/')
def predict():
   return render_template('Home.html')

@app.route('/prediction',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		federal_gov,local_gov,never_worked,private,self_emp_inc,self_emp_not_inc,state_gov,without_pay = 0,0,0,0,0,0,0,0
		
		age = request.form.get('age')
		education_number = request.form.get('education_number')
		marital_status = request.form.get('marital_status')
		work_class = request.form.get('work_class')
		occupation = request.form.get('occupation')
		relationship = request.form.get('relationship')
		race = request.form.get('race')
		gender = request.form.get('gender')
		country = request.form.get('country')	
		capital_gain = request.form.get('capital_gain')
		capital_loss = request.form.get('capital_loss')
		hours_per_week = request.form.get('hours_per_week')
		
		if work_class == 'Federal-gov':
			federal_gov = 1
		elif work_class == 'Local-gov':
			local_gov = 1
		elif work_class == ' Never-worked':
			never_worked = 1
		elif work_class == 'Private':
			private = 1
		elif work_class == 'Self-emp-inc':
			self_emp_inc = 1
		elif work_class == 'Self-emp-not-inc':
			self_emp_not_inc = 1
		elif work_class == 'State-gov':
			state_gov = 1
		else:
			without_pay = 1
		
		male, female = 0,0
		if gender == 'Male':
			male = 1
		else:
			female = 1
		
		independent, married = 0,0
		if marital_status == 'independent':
			independent = 1
		else:
			married = 1
		
		amer_indian_eskimo, asian_pac_islander, black, other, white = 0,0,0,0,0
		if race == 'Amer-Indian-Eskimo':
			amer_indian_eskimo = 1
		elif race == 'Asian-Pac-Islander':
			asian_pac_islander = 1
		elif race == 'Black':
			black = 1
		elif race == 'Other':
			other = 1
		else:
			white = 1 
		
		testing = pd.DataFrame([age,education_number,occupation,relationship,capital_gain,capital_loss,hours_per_week,country,
						federal_gov,local_gov,never_worked,private,self_emp_inc,self_emp_not_inc,state_gov,without_pay,
						female,male,independent,married,amer_indian_eskimo,asian_pac_islander,black,other,white])
		testing = testing.values.reshape(1,25)
		
		with open(r'C:\Users\Deep Joshi\Desktop\Data Analysis\Machine Learning\Income Prediction\models\model_pickle_optimized_XGBoost','rb') as f:
			mp = pickle.load(f)
			res = mp.predict(testing)
		
		if res == 0:
			outcome = "Based on the input, the person has an annual income below or equal to 50K!"
		else:
			outcome = "Based on the input the person has an annual income above 50K!"
		
		return render_template("Home.html",	prediction_text = outcome)

if __name__ == '__main__':
   app.run(debug = True)
