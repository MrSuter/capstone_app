
import pickle
import sklearn
import numpy as np
import streamlit as st
from webapp import admitpredict
from PIL import Image


def main():
    #title
    st.title('Graduate School Prediction Web App')

    model = pickle.load(open('finalized_model.sav', 'rb'))

    #adding an image to the page
    img = Image.open("output.png")
    st.image(img)

    #Get input from user
    #GRE Score,TOEFL Score,University Rating,SOP,LOR,CGPA,Research
    GREScore = st.text_input('GRE test score (out of 340)')
    TOEFLScore = st.text_input('TOEFL test score (Out of 190)')
    UniversityRating = st.text_input('University Rating (1 - 5 scale)')
    SOPRating = st.text_input('Statement of Purpose strength rating (1 - 5 scale)')
    LORRating = st.text_input('Letter of Recommendation strength rating (1 - 5 scale')
    GPARating = st.text_input('Undergraduate GPA (10 point scale)')
    Research = st.text_input('Research experience? 1 = yes, 0 = no')
    
    


    
    
    

    
    #Code for prediction
    acceptance = ''

    #Create prediction button
    if st.button('Acceptance Prediction'):
        GREScore = float(GREScore)
        TOEFLScore = float(TOEFLScore)
        UniversityRating = float(UniversityRating)
        SOPRating = float(SOPRating)
        LORRating = float(LORRating)
        GPARating = float(GPARating)
        Research = float(Research)
        acceptance = admitpredict([GREScore, TOEFLScore, UniversityRating, SOPRating, LORRating, GPARating, Research])

    st.success(acceptance)

if __name__ == '__main__':
    main()





