import streamlit as st
from PIL import Image
import pytesseract
import json
import google.generativeai as genai

# Streamlit page settings
st.set_page_config(page_title="OCR Receipt Parser", layout="centered")
st.title("🧾 OCR-based Receipt Parser")

# API Key Input
st.sidebar.header("🔑 Gemini API Key")
api_key = st.sidebar.text_input(
    "Enter your Gemini API key",
    type="password",
    help="Your API key is used only in this session and never stored.",
)

if not api_key:
    st.warning("Please enter your Gemini API key in the sidebar to continue.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Prompt template
PROMPT_TEMPLATE = """
Extract the following fields from this restaurant bill: restaurant_name, date, total_amount, and items (as list of {name, qty, price}).
Return only valid JSON. Here's the bill text:

{bill_text}
"""

# OCR function
def extract_text_from_image(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)

# Gemini extraction
def extract_fields_using_gemini(bill_text: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(bill_text=bill_text)
    response = model.generate_content(prompt)
    try:
        return json.loads(response.text)
    except Exception as e:
        st.error("Failed to parse JSON from Gemini output.")
        st.text_area("Raw Output from Gemini", response.text)
        return {}

# File uploader
uploaded_file = st.file_uploader("Upload a restaurant receipt", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", use_column_width=True)

    if st.button("🔍 Extract Data"):
        with st.spinner("Extracting text and processing..."):
            text = extract_text_from_image(image)
            structured_data = extract_fields_using_gemini(text)

        st.subheader("📄 Extracted Structured Data")
        st.json(structured_data)

# Footer
st.markdown("---")
st.markdown(
    "🔓 This project is open source and does not store your API key. "
    "View the code on [GitHub](https://github.com/your-username/ocr-receipt-parser)."
)
