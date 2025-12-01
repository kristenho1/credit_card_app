import streamlit as st
import pandas as pd
import pickle
import warnings
import numpy as np
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Predictions", page_icon = "🔍")

dt_pickle = open('decision_tree.pickle', 'rb')
dt_clf = pickle.load(dt_pickle) 
dt_pickle.close()

rf_pickle = open('randomforest.pickle', 'rb')
rf_clf = pickle.load(rf_pickle) 
rf_pickle.close()

ada_pickle = open('adaboost.pickle', 'rb')
ada_clf = pickle.load(ada_pickle) 
ada_pickle.close()

model_input = st.sidebar.radio("Choose model:", ["Decision Tree", "Random Forest", "AdaBoost"], key="model input")

default_df = pd.read_csv('Application_Data.csv')
default_df = default_df.dropna().reset_index(drop=True)
default_df = default_df.drop(columns = ['Applicant_ID', 'Status', 'Owned_Mobile_Phone'])
default_df = default_df.replace(r'^\s+|\s+$', '', regex=True)

if model_input == "Decision Tree":
    clf = dt_clf
elif model_input == "Random Forest":
    clf = rf_clf
else:
    clf = ada_clf


if "form_submitted" in st.session_state:
    user_df = pd.DataFrame({
    'Applicant_Gender': [st.session_state['Applicant_Gender']],
    'Applicant_Age': [st.session_state['Applicant_Age']],
    'Job_Title': [st.session_state['Job_Title']],
    'Years_of_Working': [st.session_state['Years_of_Working']],
    'Income_Type': [st.session_state['Income_Type']],
    'Total_Income': [st.session_state['Total_Income']],
    'Education_Type': [st.session_state['Education_Type']],
    'Owned_Car': [st.session_state['Owned_Car']],
    'Owned_Realty': [st.session_state['Owned_Realty']],
    'Total_Children': [st.session_state['Total_Children']],
    'Total_Family_Members': [st.session_state['Total_Family_Members']],
    'Family_Status': [st.session_state['Family_Status']],
    'Housing_Type': [st.session_state['Housing_Type']],
    'Owned_Work_Phone': [st.session_state['Owned_Work_Phone']],
    'Owned_Phone': [st.session_state['Owned_Phone']],
    'Owned_Email': [st.session_state['Owned_Email']],
    'Total_Bad_Debt': [st.session_state['Total_Bad_Debt']],
    'Total_Good_Debt': [st.session_state['Total_Good_Debt']],
    'form_submitted': [st.session_state['form_submitted']]
})
    encode_df = default_df.copy()
    user_df = user_df[encode_df.columns]
    encode_df = pd.concat([encode_df, user_df], axis = 0)
    cat_var = ["Applicant_Gender", "Owned_Car", "Owned_Realty", "Income_Type", "Education_Type", "Family_Status", "Housing_Type", "Owned_Work_Phone", "Owned_Phone", "Owned_Email", "Job_Title"]
    encode_dummy_df = pd.get_dummies(encode_df, columns = cat_var, drop_first=False)
    user_encoded_df = encode_dummy_df.tail(1)
    new_prediction = clf.predict(user_encoded_df)

    if new_prediction[0] == "Approved":
        result = 'Approved'
        color = 'green'
        suggestion = 'credit cards to apply to.'
        image = 'credit_card_approved.png'
        st.balloons() # i want to use balloons if someone is predicted to be accepted but idk how to do that
        
    else:
        result = 'Denied'
        color = 'red'
        suggestion = 'features to focus on.'
        image = 'credit_card_denied.png'

    st.markdown("<h1 style='text-align: center;'>Credit Card Application Prediction Result</h1>", unsafe_allow_html=True)
    st.image(image, width=700)
    with st.container(border=True):
            st.markdown("<h2 style='text-align: center;'>Prediction Result</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center; color: {color};'>Your predicted application result is <u>{result}</u></h3>", unsafe_allow_html=True)
            # for confidence probability use
            proba = clf.predict_proba(user_encoded_df)
            pred_label = new_prediction[0]
            classes = clf.classes_
            pred_idx = np.where(classes == pred_label)[0][0]      # finds the matching column
            confidence = float(proba[0, pred_idx]) * 100 
            st.markdown(f"<h4 style='text-align: center; color: gray;'>With a confidence of <b>{confidence:.2f}%</b></h4>", unsafe_allow_html=True)

    with st.container(border=True):
            st.markdown(f"<h3 style= 'text-align: center; color; black;' >Based on your results, see the suggestions below for <b>{suggestion}</b></h3>", unsafe_allow_html=True)
            if suggestion == 'credit cards to apply to.':
                with st.expander("🎓 Student Credit Cards"):
                    st.write("Below are links to apply to cards that are geared towards helping students start their credit card journey!")
                    st.link_button("Apply: Discover it® Student Cash Back", "https://www.discover.com/credit-cards/student-credit-card/it-card.html")
                    st.link_button("Apply: Capital One Quicksilver Student", "https://www.capitalone.com/credit-cards/quicksilver-student/")
                    st.link_button("Apply: BofA Unlimited Cash Rewards (Students)", "https://www.bankofamerica.com/credit-cards/products/unlimited-cash-back-student-credit-card/")
                with st.expander("💻 Second Credit Cards"):
                    st.write("Below are options for a second credit card. Each one has different beenfits depending on what you're looknig for.")
                    st.link_button("Apply: Citi® Double Cash Card","https://www.citi.com/credit-cards/citi-double-cash-credit-card")
                    st.link_button("Apply: Chase Freedom Unlimited®","https://creditcards.chase.com/cash-back-credit-cards/freedom/unlimited")
                    st.link_button("Apply: Wells Fargo Active Cash® Card","https://www.wellsfargo.com/credit-cards/active-cash/")
                with st.expander("⭐Premium Credit Cards"):
                    st.write("For those with a more extensive credit card history, below are premium credit card options that include more benefits.")
                    st.link_button("Apply: The Platinum Card® from American Express","https://www.americanexpress.com/us/credit-cards/card/platinum/")
                    st.link_button("Apply: Chase Sapphire Reserve®","https://creditcards.chase.com/travel/credit-cards/sapphire/reserve")
                    st.link_button("Apply: Capital One Venture X Rewards Credit Card","https://www.capitalone.com/credit-cards/venture-x/")
                    # used chat for link buttons and credit card suggestions above
            elif suggestion == 'features to focus on.':
                st.markdown("""
                            The most significant areas to focus on to improve your chances of being accepted are below:
                            - Total debt  
                            - Applicant age  
                            - Credit utilization  
                            - Payment history  
                            - Length of credit history  
                            - Recent credit inquiries  
                            """)
                st.write("✅ See Model Insights page to get further insight into the features that determine the outcome of the model!")
    # if accepted: give credit card suggestions to apply to
    # if rejected: based on model feature importance give insight into why they might be getting rejected (debt, age, etc)


else:
    st.image('credit_card_image_approve_deny.png', width=700)
    st.info("ℹ️ Please complete form to get a prediction.")
     