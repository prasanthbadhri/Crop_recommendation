from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        N = request.form['N']
        P = request.form['P']
        K = request.form['K']
        temperature = request.form['temperature']
        humidity = request.form['humidity']
        ph = request.form['ph']
        rainfall = request.form['rainfall']

        data = [[float(N),float(P),float(K),float(temperature),float(humidity),float(ph),float(rainfall)]]
        lr = pickle.load(open('crop_recommendation.pkl','rb'))
        prediction = lr.predict(data)[0]
    return render_template('index.html',prediction=prediction)
if __name__=="__main__":
    app.run(debug=True)