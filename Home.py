import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "👋",
    # layout = "wide"
)

# Centered Title using HTML and Markdown
st.markdown("<h1 style='text-align: center;'>Credit Card Approval Predictor</h1>", unsafe_allow_html = True)

# Subtitle with styling
st.subheader("Check if you would be approved for a credit card based on your information.")

# Insert an image
st.image('credit_card.png', width = 700, 
         caption = "See if you’re in the credit card club 🎉")

with st.expander("**What can you do with this app?**"):
    st.write("**📝 Fill Out a Survey:** Complete survey with your information.")
    st.write("""**📊 Visualize Satisfaction Trends:** Analyze data and identify:
             \n- Areas affecting your credit card approval.
             \n- Main factors influencing approval decisions.
             \n- How to improve your chances of approval.
             """)
    st.write("**🌟 Make Data-Driven Decisions:** Use insights to guide what to improve to gain approval")
    st.write("**🛠️ Interactive Features:** Explore data with fully interactive charts and summaries.")

st.markdown("---")

st.sidebar.subheader("🔍Navigate the App")
st.sidebar.write("""- **Home:** Start here to learn about the app and its features. 
                 \n- **Understanding Models:** Learn about the machine learning models you will use for predictions. 
                 \n- **Upload Data:** Upload your dataset or fill out a form for analysis and predictions. 
                 \n- **Predictions:** View predictions based on the selected model and uploaded data.
                 \n- **Model Insights:** Explore insights from the various models, such as performance metrics and visualizations.
                 """)
st.sidebar.info("**Select page above to get started!**")