import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Model Insights", page_icon = "📊")

if "form_submitted" in st.session_state:
    model_name = st.sidebar.radio(
    "Choose a Model",
    ('Decision Tree (DT)', 'Random Forest (RF)', 'AdaBoost (Ada)')
    )


    st.header(f"{model_name}")
    tab1, tab2, tab3 = st.tabs(["Confusion Matrix", "Classification Report", "Feature Importance"])


    # Tab 1: Confusion Matrix
    with tab1:
        st.write("Confusion Matrix")
        if model_name == "Decision Tree (DT)":
            st.image('dt_confusion_mat.svg')
        elif model_name == "Random Forest (RF)":
            st.image('rf_confusion_matrix.svg')
        elif model_name == "AdaBoost (Ada)":
            st.image('ab_confusion_mat.svg')


    # Tab 2: Classification Report
    with tab2:
        st.write("Classification Report")
        if model_name == "Decision Tree (DT)":
            df = pd.read_csv("dt_class_report.csv", index_col=0)
            st.write(df.style.background_gradient(cmap='Purples'))
        elif model_name == "Random Forest (RF)":
            df = pd.read_csv("rf_class_report.csv", index_col=0)
            st.write(df.style.background_gradient(cmap='Oranges'))
        elif model_name == "AdaBoost (Ada)":
            df = pd.read_csv("ab_class_report.csv", index_col=0)
            st.write(df.style.background_gradient(cmap='Reds'))



    # Tab 3: Feature Importance
    with tab3:
        st.write("Feature Importance")
        if model_name == "Decision Tree (DT)":
            st.image('dt_feature_imp.svg')
        elif model_name == "Random Forest (RF)":
            st.image('rf_feature_imp.svg')
        elif model_name == "AdaBoost (Ada)":
            st.image('ab_feature_imp.svg')

else:
    st.info("ℹ️ Please complete form to get a prediction.")



