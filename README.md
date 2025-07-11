# 🧾 OCR-based Receipt Parser

A Streamlit-based app that extracts structured data from restaurant receipts using OCR and Gemini Flash API. The app outputs clean JSON containing fields like restaurant name, total amount, date, and a list of purchased items.

---

## 🚀 Features

- Upload receipt images (`.jpg`, `.png`, `.jpeg`)
- OCR extraction using Tesseract
- Structured field extraction using Gemini Flash (Google Generative AI)
- Outputs JSON with:
  - Restaurant name
  - Date
  - Total amount
  - Itemized list (`name`, `qty`, `price`)
- Secure input of Gemini API key (not stored)
- Fully open source and extendable

---