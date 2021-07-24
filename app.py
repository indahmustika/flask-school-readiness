from tensorflow.keras.models import load_model
from flask import Flask, render_template, request 

app   = Flask(__name__)
model = load_model("nadam.h5")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	inputs   	= request.form
	name 		= inputs['name']
	gender		= int(inputs['gender'])
	age			= int(inputs['age'])
	position	= int(inputs['position'])
	siblings	= int(inputs['siblings'])
	preschool	= int(inputs['preschool'])
	fatheredu	= int(inputs['fatheredu'])
	motheredu	= int(inputs['motheredu'])

	features	= [[gender,age,position,siblings,preschool,fatheredu,motheredu]]
	prediction  = model.predict(features)

	if(prediction[0][0] > prediction[0][1]):
		if(prediction[0][0] > prediction[0][2]):
			readiness = "Dipertimbangkan"
		else:
			readiness = "Tidak Disarankan"
	elif(prediction[0][1] > prediction[0][0]):
		if(prediction[0][1] > prediction[0][2]):
			readiness = "Disarankan"
		else:
			readiness = "Tidak Disarankan"
	elif(prediction[0][2] > prediction[0][0]):
		if(prediction[0][2] > prediction[0][1]):
			readiness = "Tidak Disarankan"
		else: 
			readiness = "Disarankan"
	return render_template('index.html', name=name, gender=gender, age=age, position=position, siblings=siblings, preschool=preschool, fatheredu=fatheredu, motheredu=motheredu, readiness=readiness)

if __name__ == "__main__":
	app.run(debug=True)
