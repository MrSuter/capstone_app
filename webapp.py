import numpy as np
import pickle
import streamlit as st


#creating a function for prediction
def admitpredict(input_data, model):

    input_data_array = np.asarray(input_data)

    input_data_reshaped = input_data_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)


    if(prediction[0] == 0):
        return 'Not likely to be accepted'
    else:
        return 'Likely to be accepted'



#Xnew = [[300,195,3,3,3.5,8,1]]
#ynew = model.predict(Xnew)
#print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
