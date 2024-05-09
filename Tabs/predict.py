import streamlit as st
from web_function import predict

def app(df, x, y):
    st.title("Halaman Prediksi")
    
    # Membuat kolom input
    col1, col2, col3 = st.columns(3)
    
    # Kolom 1
    bp = col1.text_input('Nilai Input Blood Pressure')
    sg = col1.text_input('Nilai Input Specific Gravity')
    al = col1.text_input('Nilai Input Albumin')
    su = col1.text_input('Nilai Input Sugar')
    rbc = col1.text_input('Nilai Input Red Blood Cells')
    pc = col1.text_input('Nilai Input Peripheral Circle')
    pcc = col1.text_input('Nilai Input Peripheral Cell')
    ba = col1.text_input('Nilai Input Basal Cell')
    
    # Kolom 2
    bgr = col2.text_input('Nilai Input Blood Glucose Random')
    bu = col2.text_input('Nilai Input Blood Urea')
    sc = col2.text_input('Nilai Input Serum Creatinine')
    sod = col2.text_input('Nilai Input Sodium')
    pot = col2.text_input('Nilai Input Potassium')
    hemo = col2.text_input('Nilai Input Hemoglobin')
    pcv = col2.text_input('Nilai Input Packed Cell Volume')
    wc = col2.text_input('Nilai Input White Cell Count')
    
    # Kolom 3
    rc = col3.text_input('Nilai Input Red Cell Count')
    htn = col3.text_input('Nilai Input Hypertension')
    dm = col3.text_input('Nilai Input Diabetes Mellitus')
    cad = col3.text_input('Nilai Input CAD')
    appet = col3.text_input('Nilai Input Appetite')
    pe = col3.text_input('Nilai Input Pedal Edema')
    ane = col3.text_input('Nilai Input Anemia')
    
    # Kumpulan fitur untuk prediksi
    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]
    
    # Tombol prediksi
    if st.button('Prediksi'):
        if '' in features:
            st.error("Anda belum mengisi semua nilai. Silakan lengkapi semua nilai sebelum melakukan prediksi.")
        else:
            prediction, score = predict(x, y, features)
            st.info("Prediksi Berhasil")
            if prediction == 1:
                st.warning("Orang Tersebut Rentan Terkena Penyakit Batu Ginjal")
            else:
                st.success("Orang Tersebut Tidak Terkena Penyakit Batu Ginjal")
            
            st.write("Model yang digunakan memiliki tingkat akurasi ", (score * 100), "%")

