import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

#loading the saved model

loaded_model_dia = pickle.load(open('DiabetesPrediction.pickle', 'rb'))
loaded_model_chd = pickle.load(open('CHDmodel.pickle', 'rb'))
loaded_model_bre = pickle.load(open('BreastCancerPrediction.pickle', 'rb'))
loaded_model_par = pickle.load(open('parkinsons_model.pickle', 'rb'))

# creating a predictive function
def dia_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model_dia.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def bre_prediction (input_data):
        
    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for one datapoint
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model_chd.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'The Breast cancer is Malignant'

    else:
        return 'The Breast Cancer is Benign'

def par_prediction (input_data):
    my_df = pd.DataFrame([input_data])
    minmaxdata = [[32.0,0.0,0.0,83.5,48.0,113.0,0.0,0.0,40.0,0.0],[70.0,1.0,70.0,295.0,142.5,464.0,1.0,1.0,394.0,1.0]]
    minmaxdata_df = pd.DataFrame(minmaxdata)
    frames = [my_df,minmaxdata_df]
    res = pd.concat(frames)
    scaler = MinMaxScaler(feature_range=(0,1)) 
    # assign scaler to column:
    my_df_scaled = pd.DataFrame(scaler.fit_transform(res), columns=res.columns)
    my_df_scaled_df = pd.DataFrame([my_df_scaled.iloc[0]])
    my_y_pred = loaded_model_chd.predict(my_df_scaled_df)
    if my_y_pred == 1:
        return "The patient will develop a Parkinsons Disease."
    else:
        return "The patient will not develop a Parkinsons Disease."

def chd_prediction (input_data):
    my_df = pd.DataFrame([input_data])
    minmaxdata = [[32.0,0.0,0.0,83.5,48.0,113.0,0.0,0.0,40.0,0.0],[70.0,1.0,70.0,295.0,142.5,464.0,1.0,1.0,394.0,1.0]]
    minmaxdata_df = pd.DataFrame(minmaxdata)
    frames = [my_df,minmaxdata_df]
    res = pd.concat(frames)
    scaler = MinMaxScaler(feature_range=(0,1)) 
    # assign scaler to column:
    my_df_scaled = pd.DataFrame(scaler.fit_transform(res), columns=res.columns)
    my_df_scaled_df = pd.DataFrame([my_df_scaled.iloc[0]])
    my_y_pred = loaded_model_chd.predict(my_df_scaled_df)
    if my_y_pred == 1:
        return "The patient will develop a Heart Disease."
    else:
        return "The patient will not develop a Heart Disease."
