import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI-Powered Research Report Generator", layout="wide")

# Sidebar for API Key Upload
st.sidebar.title("🔑 Upload API Key")
st.sidebar.markdown("""
- [Get Google Gemini API Key](https://aistudio.google.com/app/apikey)  
""")

# API Key Input
gemini_api_key = st.sidebar.text_input("Google Gemini API Key", type="password")

# Ensure API key is provided
if not gemini_api_key:
    st.sidebar.warning("Please enter your API key to proceed.")
    st.stop()

# Initialize Gemini API
genai.configure(api_key=gemini_api_key)

# Streamlit App Main Interface
st.title("📑 AI-Powered Research Report Generator")
st.subheader("Generate detailed research reports in seconds!")

# User Input
research_topic = st.text_area("Enter Research Topic:", "Impact of AI on Healthcare")
include_sources = st.checkbox("Include References & URLs")

# Function to generate research report
def generate_research_report(topic, include_sources):
    prompt = f"""
    Generate a detailed research report on: "{topic}".
    Include key insights, statistics, challenges, and future trends.
    {"Provide references and URLs for further reading." if include_sources else ""}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "Sorry, I couldn't generate the report."

# Generate Report
if st.button("Generate Report"):
    with st.spinner("Generating research report..."):
        report = generate_research_report(research_topic, include_sources)
    
    # Display Research Report
    st.subheader("📄 Research Report")
    st.write(report)

    # Download Report as Text File
    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name=f"{research_topic.replace(' ', '_')}_report.txt",
        mime="text/plain",
    )


