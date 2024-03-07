import streamlit as st 
from web_function import predict

def app(df, x, y):
    st.title("Halaman Prediksi")
    
    col1, col2, col3, = st.columns(3)
    
    with col1:
        bp = st.text_input('Nilai Input Blood Pressure')
    with col1:
        sg = st.text_input('Nilai Input Specific Gravity')
    with col1:
        al = st.text_input('Nilai Input Albumin')
    with col1:
        su = st.text_input('Nilai Input Sugar')
    with col1:
        rbc = st.text_input('Nilai Input Red Blood Cells')
    with col1:
        pc = st.text_input('Nilai Input Peripheral Circle')
    with col1:
        pcc = st.text_input('Nilai Input Peripheral Cell')
    with col1:
        ba = st.text_input('Nilai Input Basal Cell')
    with col2:
        bgr = st.text_input('Nilai Input Blood Glucose Random')
    with col2:
        bu = st.text_input('Nilai Input Blood Urea')
    with col2:
        sc = st.text_input('Nilai Input Serum Creatinine')
    with col2:
        sod = st.text_input('Nilai Input Sodium')
    with col2:
        pot = st.text_input('Nilai Input Potassium')
    with col2:
        hemo = st.text_input('Nilai Input Hemoglobin')
    with col2:
        pcv = st.text_input('Nilai Input Packed Cell Volume')
    with col2:
        wc = st.text_input('Nilai Input White Cell Count')
    with col3:
        rc = st.text_input('Nilai Input Red Cell Count')
    with col3:
        htn = st.text_input('Nilai Input Hypertension')
    with col3:
        dm = st.text_input('Nilai Input Diabetes Mellitus')
    with col3:
        cad = st.text_input('Nilai Input CAD')
    with col3:
        appet = st.text_input('Nilai Input Appetite')
    with col3:
        pe = st.text_input('Nilai Input Pedal Edema')
    with col3:
        ane = st.text_input('Nilai Input Anemia')
        
    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]
    
    if st.button('Prediksi'):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Prediksi Berhasil")   
    
        if (prediction == 1):
            st.warning("Orang Tersebut Rentan Terkena Penyakit Batu Ginjal")
        else:
            st.success("Orang Tersebut Tidak Terkena Penyakit Batu Ginjal")
        
        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")