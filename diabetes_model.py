import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open(r"C:\Dhruv_ML\diabetes_model.sav", "rb"))

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.array(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'No Diabetic'
    else:
        return 'Diabetic'

def main():
    st.title('Diabetes Prediction Web App')
    
    gnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    Age = st.text_input("Age Of The Person")
    
    diagnosis=''
    
    if st.button("Diabetes Test Result"):
        try:
            input_data = [float(gnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            diagnosis = diabetes_prediction(input_data)
            st.success(diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

if __name__ == '__main__':
    main()