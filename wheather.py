import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('weather_model.sav', "rb"))

def weather_prediction(input_data):
    input_data_as_numpy_array = np.array(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'Rainy'
    elif prediction[0]==1:
        return 'Sunny'
    elif prediction[0]==2:
        return 'Overcast'
    elif prediction[0]==3:
        return 'Cloudy'
    else:
        return 'Snowy'

def main():
    cloud_cover = {'overcast':0,'partly cloudy':1,'clear':2,'cloudy':3}
    season={'Winter':0,'Spring':1,'Autumn':2,'Summer':3}
    location={'inland':0,'mountain':1,'coastal':2}
    st.title('Weather Prediction Web App')  
    
    temp = st.text_input("Enter Number of Temperature")
    humidity = st.text_input("Enter Humidity")
    wind_speed = st.text_input("Enter Wind Speed")
    precipitation = st.text_input("Enter Precipitation (%)")
    choice1 = st.selectbox("Cloud Cover:", cloud_cover)
    ap = st.text_input("Enter Atmospheric Pressure")
    uv = st.text_input("Enter UV Index")
    choice2 = st.selectbox("Season:", season)
    vis=st.text_input("Enter Visibility(km)")
    choice3 = st.selectbox("Location:", location)
    
    diagnosis=''
    
    if st.button("Weather Test Result"):
        try:
            input_data = [float(temp), float(humidity), float(wind_speed), float(precipitation),
                          cloud_cover[choice1], float(ap), float(uv),season[choice2],float(vis),location[choice3]]
            prediction = weather_prediction(input_data)
            st.success(prediction)
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

if __name__ == '__main__':
    main()
