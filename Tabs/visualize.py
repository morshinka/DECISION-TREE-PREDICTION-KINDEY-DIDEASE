import warnings
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st 
from web_function import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualisasi Prediksi Batu Ginjal") 
    
    # if st.checkbox("Plot Confucion Matrix"):
    #     model, score = train_model(x,y)
    #     plt.figure(figsize = (10,5))
    #     confusion_matrix(model, x, y, values_format='d')
    
    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x, y)
        # Hitung confusion matrix
        cm = confusion_matrix(model.predict(x), y)

        plt.figure(figsize=(10, 5))
        sns.heatmap(cm, annot=True, fmt='d')  # Gunakan seaborn untuk heatmap dengan format integer
        plt.xlabel('Label Prediksi')
        plt.ylabel('Label Aktual')
        plt.title('Confusion Matrix')
        st.pyplot()  # Gunakan st.pyplot untuk menampilkan plot di Streamlit

        
    
    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x,y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True, feature_names=x.columns, class_names=['nockd', 'ckd']
        )
        
        st.graphviz_chart(dot_data)