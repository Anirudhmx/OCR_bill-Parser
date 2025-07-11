import os
import google.generativeai as genai

# Setup Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

PROMPT_TEMPLATE = """
Extract the following fields from this restaurant bill: restaurant_name, date, total_amount, items (as list of {name, qty, price}).
Return a JSON. Here's the text:

{bill_text}
"""

def extract_fields_using_gemini(bill_text: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(bill_text=bill_text)
    response = model.generate_content(prompt)
    return response.text
