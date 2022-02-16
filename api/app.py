from flask import Flask, request, jsonify
from sklearn.ensemble        import RandomForestRegressor
import pickle

home_path = 'C:/Users/AMD/repos/absenteeism_at_work/models/'

colunas = ['age', 'work_load_average/day_']
modelo = pickle.load(open(home_path + 'model_tuned.pkl','rb'))


app = Flask(__name__)

@app.route('/predict/', methods=['POST'])
def predict():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    absenteismo = modelo.predict([[colunas]])
    return str(absenteismo)

app.run('0.0.0.0')
