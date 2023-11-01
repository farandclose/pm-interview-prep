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
    # set up variables for system and user
    system_message = 'You are an expert Product Leader in '+industry+' industry and you are interviewing a candidate for the role of Product Manager in your company. You have decided to give him a business case related to ' + case_type
    user_message = 'Please generate business case for the candidate.'
    # Set up OpenAI API authentication and call the API to generate the business case
    # Return the generated business case text
    openai.api_key = st.secrets["openai_api_key"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": system_message
            },            
            {
            "role": "user",
            "content": user_message
            }
        ],
        temperature=1,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']


if st.button("Generate Business Case"):
    business_case = generate_business_case(selected_industry, selected_case)
    st.subheader("Generated Business Case")
    st.write(business_case)
else:
    st.subheader("Generated Business Case")
    st.write("Click the button to generate a business case.")



st.subheader("Evaluation Parameters")
st.write("1. Parameter 1")
st.write("2. Parameter 2")
st.write("3. Parameter 3")

st.subheader("Your Solution")
user_solution = st.text_area("Enter your solution here", height=300)