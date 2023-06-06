import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')


# loading the saved model
loaded_model = pickle.load(open('C:/Users/ankit/OneDrive/Desktop/streamlit_dashboard/trained_model_hospital.pkl'
                                , 'rb'))
age = 0
gender = 0
bmi = 0
hypertensive = 0
atrialfibrillation = 0
chd_with_no_MI = 0
diabetes = 0
deficiencyanemias = 0
depression = 0
hyperlipemia = 0
renal_failure = 0
copd = 0
heart_rate = 0
systolic_blood_pressure	 = 0
diastolic_blood_pressure = 0
respiratory_rate = 0
temp = 0
sp_O2 = 0
urine_output = 0
hematocrit	= 0
rbc = 0
mch = 0
mchc = 0
mcv = 0
rdw = 0
leucocyte = 0
platelets = 0
neutrophils = 0
basophils = 0
lymphocyte = 0
pt = 0
inr = 0
nt_probnp = 0
creatine_kinase = 0
creatinine = 0
urea_nitrogen = 0
glucose = 0
blood_potassium = 0
blood_sodium = 0
blood_calcium = 0
chloride = 0
anion_gap = 0
magnesium_ion = 0
ph = 0
bicarbonate = 0
lactic_acid = 0
pc02 = 0
ef = 0

def mortality(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0]==0):
        return st.success('Patient is not Alive')
    else:
        return st.error('Patient is Alive')

def main():

    # giving a title
    st.title('Hospital Mortality Prediction')

    # getting the input data from the user
    age = st.text_input('Age')
    gender = st.radio('Select whether male or female', ('1', '0'))
    if (gender == '1'):
        st.info("Male")
    else:
        st.info("Female")
    bmi = st.text_input('BMI')
    hypertensive = st.radio('Select whether patient is hypertensive or not', ('1', '0'))
    if (hypertensive == '1'):
        st.info("hypertensive")
    else:
        st.info("Not hypertensive")
    atrialfibrillation = st.text_input('a trial fibrillation , choose 0 or 1')
    chd_with_no_MI = st.text_input('chd with no MI , choose 0 or 1')
    diabetes = st.radio('Select whether has diabetes or not', ('1', '0'))
    if (gender == '1'):
        st.info("Person is diabetic")
    else:
        st.info("Person is not diabetic")
    deficiencyanemias = st.radio('Select whether has deficiency of Iron or not', ('1', '0'))
    if (gender == '1'):
        st.info("Person has deficiency of Iron")
    else:
        st.info("Person has no deficiency of Iron")

    depression = st.radio('Select whether person has depression or not', ('1', '0'))
    if (gender == '1'):
        st.info("Person is in depression")
    else:
        st.info("Person has no depression")

    hyperlipemia = st.radio('Select whether person have hyperlipemia or not', ('1', '0'))
    if (gender == '1'):
        st.info("Person has hyperlipemia")
    else:
        st.info("Person has no hyperlipemia")
    renal_failure = st.text_input('renal failure , choose 0 or 1')
    copd = st.text_input('COPD , choose 0 or 1')
    heart_rate = st.text_input('Heart Rate')
    systolic_blood_pressure = st.text_input('Systolic blood pressure')
    diastolic_blood_pressure = st.text_input('Diastolic blood pressure')
    respiratory_rate = st.text_input('Respiratory blood pressure')
    temp = st.text_input('Patient Temperature')
    sp_O2 = st.text_input('SP 02')
    urine_output = st.text_input('Urine Output')
    hematocrit = st.text_input('Hematocrit')
    rbc = st.text_input('RBC')
    mch = st.text_input('MCH')
    mchc = st.text_input('MCHC')
    mcv = st.text_input('MCV')
    rdw = st.text_input('RDW')
    leucocyte = st.text_input('Leucocyte')
    platelets = st.text_input('Platelets')
    neutrophils = st.text_input('Neutrophils')
    basophils = st.text_input('Basophils')
    lymphocyte = st.text_input('Lymphocyte')
    pt  = st.text_input('PT')
    inr = st.text_input('INR')
    nt_probnp = st.text_input('NT Probnp')
    creatine_kinase = st.text_input('creatine kinase')
    creatinine = st.text_input('creatinine')
    urea_nitrogen = st.text_input('Urea Nitrogen')
    Glucose = st.text_input('Glucose')
    blood_potassium = st.text_input('Blood potassium')
    blood_sodium = st.text_input('Blood Sodium')
    blood_calcium = st.text_input('Blood calcium')
    chloride = st.text_input('Chloride')
    anion_gap = st.text_input('anion gap')
    magnesium_ion = st.text_input('magnesium ion')
    ph = st.text_input('PH')
    bicarbonate = st.text_input('Bicarbonate')
    lactic_acid = st.text_input('lactic acid')
    pc02 = st.text_input('PC 02')
    ef = st.text_input('EF')

    if st.button('Hospital Mortality Prediction'):
        result = mortality(
            [age,gender,bmi,hypertensive,atrialfibrillation,chd_with_no_MI,diabetes,deficiencyanemias,depression,hyperlipemia,
             renal_failure,copd,heart_rate,systolic_blood_pressure,diastolic_blood_pressure,respiratory_rate,temp,sp_O2,urine_output,
             hematocrit,rbc,mch,mchc,mcv,rdw,leucocyte,platelets,neutrophils,basophils,lymphocyte,pt,inr,nt_probnp,creatine_kinase,
             creatinine,urea_nitrogen,glucose,blood_sodium,blood_potassium,blood_calcium,chloride,anion_gap,magnesium_ion,ph,
             bicarbonate,lactic_acid,pc02,ef])


if __name__ == '__main__':
    main()


