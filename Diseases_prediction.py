# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:51:26 2024

@author: Ritik
"""
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="centered",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
#working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('Diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('Heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('Parkinsons_model.sav', 'rb'))

breast_cancer_model=pickle.load(open('Breast_cancer_model.sav', 'rb'))

liver_disease_model=pickle.load(open('Liver_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:           
    selected = option_menu('Health Guard Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction',
                            'Liver Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart-half', 'capsule','shield-shaded','person-fill'],
                           default_index=0)

# Diabetes Prediction Page

if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.markdown("Diabetes is a chronic health condition that occurs when the body either doesn't produce enough insulin or cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood sugar (glucose) and allows it to enter cells to be used for energy. There are primarily two types of diabetes:")
    st.markdown("TYPE 1 DIABETES: This type occurs when the immune system attacks and destroys insulin-producing cells in the pancreas. People with Type 1 diabetes need to take insulin injections daily to survive.")
    st.markdown("TYPE 2 DIABETES: This is more common and usually develops in adults, although increasingly seen in children. In Type 2 diabetes, the body becomes resistant to insulin or doesn't produce enough insulin. This can often be managed with lifestyle changes such as diet, exercise, and sometimes medication.")
    st.markdown("Common symptoms of diabetes include frequent urination, increased thirst, unexplained weight loss, fatigue, blurred vision, slow wound healing, and increased susceptibility to infections. Long-term complications of diabetes can include heart disease, stroke, kidney damage, nerve damage (neuropathy), and vision loss.")
    st.markdown("Management of diabetes involves monitoring blood sugar levels, adopting a healthy diet, regular physical activity, taking medications as prescribed (including insulin for Type 1 diabetes), and managing other risk factors such as high blood pressure and cholesterol levels. Early diagnosis and effective management are crucial in preventing complications and maintaining a good quality of life for individuals with diabetes.")


# Insert custom CSS to change the color 
    pg_bg_img='''     
    <style>
    [data-testid="stApp"]{
    background: rgb(182,233,218);
    background: linear-gradient(90deg, rgba(182,233,218,1) 0%, rgba(255,186,187,1) 100%);
    }
        
    </style>
    '''
    st.markdown(pg_bg_img,unsafe_allow_html=True)
    
    st.image('C:/Users/Ritik/Downloads/diabetes.jpg')
    
    # page title
    st.subheader('Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page

if selected == 'Heart Disease Prediction':

    st.title('Heart Disease')
    st.markdown('Heart disease, also known as cardiovascular disease (CVD), encompasses various conditions affecting the heart and blood vessels. The most common form is coronary artery disease (CAD), caused by the buildup of plaque in the arteries supplying blood to the heart, leading to reduced blood flow and potential heart attacks.')
    st.markdown("Other types include heart failure (when the heart can't pump enough blood), arrhythmias (abnormal heart rhythms), and congenital heart defects (present at birth). Risk factors include high blood pressure, high cholesterol, smoking, diabetes, obesity, unhealthy diet, lack of exercise, excessive alcohol, and family history.")
    st.markdown('Preventive measures like healthy lifestyle changes (diet, exercise, quitting smoking), managing risk factors (blood pressure, cholesterol), and regular check-ups are essential. Treatment options include medications, procedures (angioplasty, bypass surgery), and devices (pacemakers). Early detection and management are crucial for reducing complications like heart attacks or strokes.')
    
# Insert custom CSS to change the color 
    pg_bg_img='''     
    <style>
    [data-testid="stApp"]{
    background: rgb(182,233,218);
    background: linear-gradient(90deg, rgba(182,233,218,1) 0%, rgba(255,186,187,1) 100%);
    }
        
    </style>
    '''
    st.markdown(pg_bg_img,unsafe_allow_html=True)
    
# Insert image    
    st.image('C:/Users/Ritik/Downloads/heart.jpg')
    
    # page title
    st.subheader('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having  heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'

    st.success(heart_diagnosis)

#for breast cancer disease
if selected == "Breast Cancer Prediction":
   
    
    st.title('Breast Cancer')
    st.markdown("Breast cancer is a malignant tumor that originates in the cells of the breast. It primarily affects women but can also occur in men. The cancer usually begins in the ducts (ductal carcinoma) or lobules (lobular carcinoma) of the breast. Risk factors include advancing age, family history of breast cancer, genetic mutations (like BRCA1 and BRCA2), hormonal influences (early menstruation, late menopause), radiation exposure, obesity, and alcohol consumption")
    st.markdown("Signs and symptoms of breast cancer can include a new lump in the breast or underarm, changes in breast size or shape, nipple changes (like inversion or discharge), and skin changes (such as dimpling or redness).")
    st.markdown("Early detection through regular mammograms and self-exams is key for successful treatment. Treatment options depend on the type and stage of cancer but may involve surgery, chemotherapy, radiation therapy, hormone therapy, or targeted therapy. Breast cancer awareness and timely medical consultation are crucial for improving outcomes and survival rates.")
    
# Insert custom CSS to change the color 
    pg_bg_img='''     
    <style>
    [data-testid="stApp"]{
    background: rgb(182,233,218);
    background: linear-gradient(90deg, rgba(182,233,218,1) 0%, rgba(255,186,187,1) 100%);
    }
        
    </style>
    '''
    st.markdown(pg_bg_img,unsafe_allow_html=True)
    
# Insert image    
    st.image('C:/Users/Ritik/Downloads/cancer.jpg')   
    
    # page title
    st.subheader("Breast Cancer Prediction")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        radius_mean = st.text_input('Radius of Lobes')
        
    with col2:
        texture_mean = st.text_input('Mean Of Surface Texture')

    with col3:
        perimeter_mean = st.text_input('Outer Perimeter Of Lobes')

    with col4:
        area_mean = st.text_input('Mean Area Of Lobes')    
        
    with col1:
        smoothness_mean = st.text_input('Mean Of Smoothness Level')
            
    with col2:
        compactness_mean = st.text_input('Mean Of Compactness')

    with col2:
        concavity_mean = st.text_input('Mean Of Concavity')

    with col3:
        concave_points_mean = st.text_input('Mean Of Concave Points')

    with col4:
        symmetry_mean = st.text_input('Mean Of Symmetry')
        
    with col1:
        fractal_dimension_mean = st.text_input('Mean Of Fractal Dimension')
        
    with col1:
        radius_se = st.text_input('Radius se')
        
    with col2:
        texture_se = st.text_input('Texture se')

    with col3:
        perimeter_se = st.text_input('Perimeter se')

    with col4:
        area_se = st.text_input('Area se')  
            
    with col1:
        smoothness_se = st.text_input('Smoothness se')

    with col2:
        compactness_se = st.text_input('Compactness se')

    with col3:
        concavity_se = st.text_input('Concavity se')
        
    with col4:
        concave_points_se = st.text_input('Concave Points se')
            
    with col1:
        symmetry_se = st.text_input('Symmetry se')

    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension se')
    
    with col3:
        radius_worst = st.text_input('Radius Worst')

    with col4:
        texture_worst = st.text_input('Texture Worst')
    
    with col1:
        perimeter_worst = st.text_input('Perimeter Worst')
      
    with col2:
        area_worst = st.text_input('Area Worst')
         
    with col3:
         smoothness_worst = st.text_input('Smoothness Worst')
         
    with col4:
        compactness_worst = st.text_input('Compactness Worst')
        
    with col1:
        concavity_worst = st.text_input('Concavity Worst')
        
    with col2:
        concave_points_worst = st.text_input('Concave Points Worst')
        
    with col3:
        symmetry_worst = st.text_input('Symmetry Worst')
        
    with col4:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')
        
    # code for Prediction
    cancer_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Cancer Test Result"):

        user_input = [ radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,compactness_mean, concavity_mean, concave_points_mean,symmetry_mean,
                      fractal_dimension_mean, radius_se, texture_se,perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, 
                      symmetry_se, fractal_dimension_se,radius_worst, texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,
                      concave_points_worst, symmetry_worst, fractal_dimension_worst]

        user_input = [float(x) for x in user_input]

        cancer_prediction = breast_cancer_model.predict([user_input])

        if cancer_prediction[0] == 1:
            cancer_diagnosis = "The person has Cancer disease"
        else:
            cancer_diagnosis = "The person does not have Cancer disease"

    st.success(cancer_diagnosis)

#for liver disease prediction
if selected == "Liver Disease Prediction":
  
    st.title('Liver Disease')
    st.markdown('Liver disease refers to any condition that affects the liver, a vital organ responsible for processing nutrients, filtering toxins, and producing important proteins. There are various types of liver diseases, including hepatitis (inflammation of the liver), liver cirrhosis (scarring of liver tissue), non-alcoholic fatty liver disease (accumulation of fat in the liver), autoimmune liver diseases, and liver cancer.')
    st.markdown('Common symptoms of liver disease include fatigue, jaundice (yellowing of the skin and eyes), abdominal pain or swelling, nausea, vomiting, dark urine, pale stools, itching, and easy bruising or bleeding. The specific symptoms and severity depend on the underlying cause and progression of the disease.')
    st.markdown('Treatment for liver disease varies based on the type and severity of the condition. It may involve lifestyle modifications (such as dietary changes and avoiding alcohol), medications to manage symptoms or address the underlying cause (such as antiviral drugs for hepatitis), and in advanced cases, liver transplantation.')

# Insert custom CSS to change the color 
    pg_bg_img='''     
    <style>
    [data-testid="stApp"]{
    background: rgb(182,233,218);
    background: linear-gradient(90deg, rgba(182,233,218,1) 0%, rgba(255,186,187,1) 100%);
        
    </style>
    '''
    st.markdown(pg_bg_img,unsafe_allow_html=True)

# Insert image    
    st.image('C:/Users/Ritik/Downloads/liver.jpg')   

    # page title
    st.subheader('Liver Disease Prediction')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Age')

    with col2:
        gender = st.text_input('Gender')

    with col3:
        total_bilirubin = st.text_input('Total Bilirubin')

    with col4:
        direct_bilirubin = st.text_input('Direct Bilirubin')


    with col1:
        alkaline_phosphotase = st.text_input('Alkaline Phosphotase')

    with col2:
        alamine_aminotransferase = st.text_input('Alamine Aminotranseferase')

    with col3:
        aspartate_aminotransferase = st.text_input('Aspartate Aminotranseferase')

    with col4:
        total_protiens = st.text_input('Total Protiens')


    with col1:
        albumin = st.text_input('Albumin')

    with col2:
        albumin_globulin_ratio = st.text_input('Albumin & Globumin Ratio')


    # code for Prediction
    liver_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Liver Test Result"):

        user_input = [age, gender, total_bilirubin, direct_bilirubin,
                      alkaline_phosphotase, alamine_aminotransferase,
                      aspartate_aminotransferase, total_protiens, albumin,
                      albumin_globulin_ratio]

        user_input = [float(x) for x in user_input]

        liver_prediction = liver_disease_model.predict([user_input])

        if liver_prediction[0] == 1:
            liver_diagnosis = "The person has Liver disease"
        else:
            liver_diagnosis = "The person does not have Liver disease"

    st.success(liver_diagnosis)
    
# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.markdown("Parkinson's disease is a progressive neurological disorder that affects movement. It is characterized by symptoms such as tremors (especially at rest), slowness of movement (bradykinesia), muscle stiffness (rigidity), and impaired balance. These symptoms result from a loss of dopamine-producing nerve cells in the brain.")
    st.markdown("The exact cause of Parkinson's disease is not known, but it is believed to involve a combination of genetic and environmental factors. Diagnosis is based on medical history, neurological examination, and assessment of symptoms. While there is no cure for Parkinson's disease, treatment aims to manage symptoms and improve quality of life.")
    st.markdown("Common treatments include medications that replenish dopamine levels in the brain, physical therapy to improve mobility and flexibility, and lifestyle adjustments. Parkinson's disease is a chronic condition that progresses over time, but with proper management and support, many individuals can lead fulfilling lives despite the challenges posed by the disease.")

# Insert custom CSS to change the color
    pg_bg_img='''     
    <style>
    [data-testid="stApp"]{
    background: rgb(182,233,218);
    background: linear-gradient(90deg, rgba(182,233,218,1) 0%, rgba(255,186,187,1) 100%);
    </style>
    '''
    st.markdown(pg_bg_img,unsafe_allow_html=True)
    
# Insert image    
    st.image('C:/Users/Ritik/Downloads/parkinsons.jpg')   

    # page title
    st.subheader("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
