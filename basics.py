from flask import Flask ,request, render_template
import pandas as pd
# import pickle
import numpy as np
# model = pickle.load(open('PRML Course Project Deploy.pkl', 'rb')) 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index1.html")

@app.route('/predict', methods =['POST'])
def predict():
    features = [i for i in request.form.values()]
    features[1]=float(features[1])
    features[2]=int(features[2])
    features[3]=int(features[3])
    features[7]=float(features[7])
    features[8]=float(features[8])

    array_features = [np.array(features)]
    array_features = pd.DataFrame([array_features])
    # prediction = model.predict(array_features)


    # if prediction == 1:
    #     return render_template('index1.html', 
    #                             result = 'The patient is likely to have Stroke')
    # else:
    #     return render_template('index1.html', 
    #                             result = 'The patient is not likely to have Stroke')


if __name__=="__main__":
    app.run(debug=True)



