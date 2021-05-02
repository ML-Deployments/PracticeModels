from flask import Flask, request, Response, jsonify, render_template
# import numpy as np
# import pickle

root_path = '' #'/content/drive/MyDrive/Colab Notebooks/Inc Prediction App/'

# running the Flask app
app = Flask(__name__, template_folder=root_path + 'templates/')
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    output = 10000 # round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

app.run()