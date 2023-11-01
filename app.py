import streamlit as st
import openai

st.set_page_config(page_title="PM Interview Practice",layout="wide")

st.title("Product Manager Interview Practice")
st.write("Select the industry and type of business case to practice.")

industries = [
    "E-commerce and Retail",
    "Financial Services and Fintech",
    "Healthtech and Digital Health",
    "Edtech and Online Learning",
    "Social Media and Networking",
    "Software as a Service (SaaS)",
    "Gaming and Entertainment",
    "Travel and Hospitality",
    "Marketing and Advertising Technology",
    "Telecommunications and Networking",
    "Cybersecurity and Data Privacy",
    "Artificial Intelligence and Machine Learning",
    "Internet of Things (IoT) and Smart Devices",
    "Blockchain and Cryptocurrency",
    "Logistics and Supply Chain Management",
]
cases = [
    "Market Entry Strategy",
    "Product Launch Strategy",
    "Pricing Strategy",
    "User Acquisition and Growth",
    "Product Optimization and A/B Testing",
    "Monetization and Revenue Models",
    "Competitive Analysis and Differentiation",
    "Customer Segmentation and Targeting",
    "Product Roadmap and Prioritization",
    "International Expansion and Localization",
]

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