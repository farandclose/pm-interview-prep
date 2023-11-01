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
    "Critiquing Design",
    "Designing a Mobile App",
    "Pricing Strategy",
    "User Acquisition and Growth",
    "Product Optimization and A/B Testing",
    "Monetization and Revenue Models",
    "Competitive Analysis and Differentiation",
    "Customer Segmentation and Targeting",
    "Product Roadmap and Prioritization",
    "International Expansion and Localization",
]

pricing_strategy_few_shot_examples = (
    'Q1: How would you price the Kindle Fire HD?\n'
    'Q2: Assume you are the new product manager in our Amazon Prime business and are deciding pricing. The vice president would like to lower the price from $79.99 per year to $69.99 per year. Making your own assumptions, develop the financial projections for this decision.\n\n'
)

selected_industry = st.selectbox("Choose an Industry", industries)
selected_case = st.selectbox("Choose a Business Case", cases)




def generate_business_case(industry, case_type):
    # set up variables for system and user
    system_message = (
        'You are an expert Product Leader in '+industry+' industry and you are interviewing a candidate for the role of Product Manager in your company.' + case_type + '. Here are some of the earlier business problems that you have asked in previous interviews:\n\n'
        +pricing_strategy_few_shot_examples+
        'Your response always contain only questions (as shown in examples above) and do not contain anything else.'
        )
    user_message = 'Please generate a simulated business problem for the candidate that is related to the industry '+ industry + ' and pertaining to this topic '+ case_type
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