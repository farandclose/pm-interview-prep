import streamlit as st
import openai

st.set_page_config(page_title="PM Interview Practice",layout="wide")

st.title("Product Manager Interview Practice")
st.write("Select the industry and type of business case to practice.")

industries = ["Industry 1", "Industry 2", "Industry 3"]
cases = ["Case 1", "Case 2", "Case 3"]

selected_industry = st.selectbox("Choose an Industry", industries)
selected_case = st.selectbox("Choose a Business Case", cases)

def generate_business_case(industry, case_type):
    # Set up OpenAI API authentication and call the API to generate the business case
    # Return the generated business case text

    return "Generated business case text"

business_case = generate_business_case(selected_industry, selected_case)
st.subheader("Generated Business Case")
st.write(business_case)

st.subheader("Evaluation Parameters")
st.write("1. Parameter 1")
st.write("2. Parameter 2")
st.write("3. Parameter 3")

st.subheader("Your Solution")
user_solution = st.text_area("Enter your solution here", height=300)