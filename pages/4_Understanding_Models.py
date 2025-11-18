import streamlit as st
import pandas as pd


st.title("Understanding Models")
st.write("Compare the available machine learning models for predicting customer satisfaction "
           "and choose the best one for your needs")


st.sidebar.header("Why Learn about the Models")
st.sidebar.write("In the next step, you'll be selecting a machine learning model"
       " for analying customer satisfaction data. It's important to understand"
       " the stregths and trade-offs of each model to make the best choice.")
st.sidebar.write("Here's what you'll find on this page:")
st.sidebar.markdown("- **Model Explanations**: Learn about Decision Tree, Random Forest, AdaBoost, and the Soft Voting Classifer")
st.sidebar.markdown("- **Visual Results**: Examine confusion matrices for each model.")
st.sidebar.markdown("- **Reports**: Download classification reports for deeper analysis.")


st.header("About the Models")
with st.expander("Decision Tree"):
   st.markdown("- A simple, interpretable model that split data into branches based on features.")
   st.markdown("- Works well with small datasets and is easy to visualize.")
   st.markdown("- **Why use it?** When interpretability and simplicity are more important than accuracy.")


with st.expander("Random Forest"):
   st.markdown("- Combines multiple decision trees to improve accuracy and reduce overfitting.")
   st.markdown("- Handles large datasets effecitively and provides feature importance.")
   st.markdown("- **Why use it?** When you need a balance of accuracy and generalization.")


with st.expander("AdaBoost"):
   st.markdown("- A boosting technique that builds models iteratively, focusing on difficult-to-predict sampels.")
   st.markdown("- Improves performance for imbalanced datasets.")
   st.markdown("- **Why use it?** When your data has significant class imbalances or needs better handling of misclassifications.")



st.header("Choosing the Right Model")
st.markdown("- Use **Decision Tree** for quick analysis or when interpretability is crucial.")
st.markdown("- Use **Random Forest** for a robust balance of accuracy and generalization.")
st.markdown("- Use **AdaBoost** for imbalanced datasets or when misclassificatioin costs are high.")


st.caption("Explore the models and select the one that aligns with your project goals!")