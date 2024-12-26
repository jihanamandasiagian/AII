from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from Model import main  # Pastikan file Model.py ada dan mengandung fungsi main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data input dari form
    input_data = [
        float(request.form['age']),
        float(request.form['trestbps']),
        float(request.form['chol']),
        float(request.form['oldpeak']),
        int(request.form['ca']),
        int(request.form['thalch']),
        
        # Menggunakan get() dan memberikan default 0 jika tidak ada pilihan
        int(request.form.get('cp_asymptomatic', 0) != '0'),
        int(request.form.get('cp_atypical_angina', 0) != '0'),
        int(request.form.get('cp_non_anginal', 0) != '0'),
        int(request.form.get('cp_typical_angina', 0) != '0'),
        
        int(request.form.get('restecg_lv_hypertrophy', 0) != '0'),
        int(request.form.get('restecg_normal', 0) != '0'),
        int(request.form.get('restecg_st_t_abnormality', 0) != '0'),
        
        # Sex (Menentukan 1 jika ada, 0 jika tidak ada)
        int(request.form.get('sex_Female', 0) != '0'),
        int(request.form.get('sex_Male', 0) != '0'),
        
        # Exang dan FBS
        int(request.form.get('exang_False', 0) != '0'),
        int(request.form.get('exang_True', 0) != '0'),
        int(request.form.get('fbs_False', 0) != '0'),
        int(request.form.get('fbs_True', 0) != '0')
    ]

    # Panggil fungsi main untuk mendapatkan prediksi
    prediction = main(input_data)
    
    # Tentukan hasilnya
    if prediction >= 1:
        result = f"Heart Disease {prediction}"
    else:
        result = "No Heart Disease"
    
    return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
